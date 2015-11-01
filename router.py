###########################################################################
#
# Copyright 2015 Robert B. Lowrie (http://github.com/lowrie)
#
# This file is part of pyRouterJig.
#
# pyRouterJig is free software: you can redistribute it and/or modify it under
# the terms of the GNU General Public License as published by the Free Software
# Foundation, either version 3 of the License, or (at your option) any later
# version.
#
# pyRouterJig is distributed in the hope that it will be useful, but WITHOUT ANY
# WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR
# A PARTICULAR PURPOSE.  See the GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License along with
# pyRouterJig; see the file LICENSE. If not, see <http://www.gnu.org/licenses/>.
#
###########################################################################

'''
Contains the router, board, template and their geometry properties.
'''
from __future__ import division
from future.utils import lrange

import math
from copy import deepcopy
from utils import my_round

class Router_Exception(Exception):
    '''
    Exception handler for all routerJig
    '''
    def __init__(self, msg):
        Exception.__init__(self, msg)
        self.msg = msg
    def __str__(self):
        return self.msg

class Incra_Template(object):
    '''
    Contains properties of an incra template

    Attributes:

    height: Dimension in y-coordinate
    margin: Dimension in x-coordinate placed on each end of template
    length: total length of template
    '''
    def __init__(self, units, board, margin=None, length=None):
        # incra uses 1/2" high templates
        self.height = units.inches_to_intervals(0.5)
        if margin is None:
            self.margin = units.inches_to_intervals(1.0)
        else:
            self.margin = margin
        if length is None:
            self.length = board.width + 2 * self.margin
        else:
            self.length = length

class Router_Bit(object):
    '''
    Stores properties of dovetail and straight router bits.

    Input attributes (after creation, use setter functions to set these)

    angle: measured from y-axis, in degrees, following dovetail bit
           standard. Zero for straight bit.

    width: max cutting width.  This is the bottom of a dovetail bit.
           For now, this must be an even number.

    depth: cutting depth. Equals board thickness for through dovetails
            and box joints.

    Computed attributes:

    offset: x-dimension between max-width point and point at board's
            surface.  Zero for angle=0.

    neck: width of bit at board surface.

    halfwidth: half of width
    '''
    def __init__(self, units, width, depth, angle=0):
        self.units = units
        self.width = width
        self.depth = depth
        self.angle = angle
        self.reinit()
    def set_width_from_string(self, s):
        '''
        Sets the width from the string s, following requirements from units.string_to_intervals().
        '''
        msg = 'Bit width is "%s".  Set to a postive value.'
        try:
            self.width = self.units.string_to_intervals(s)
        except ValueError as e:
            msg = 'ValueError setting bit width: %s\n' % (e) + \
                  msg % s
            raise Router_Exception(msg)
        except:
            raise
        if self.width <= 0:
            raise Router_Exception(msg % s)
        self.reinit()
    def set_depth_from_string(self, s):
        '''
        Sets the depth from the string s, following requirements from units.string_to_intervals().
        '''
        msg = 'Bit depth is "%s".  Set to a postive value.'
        try:
            self.depth = self.units.string_to_intervals(s)
        except ValueError as e:
            msg = 'ValueError setting bit depth: %s\n' % (e) + \
                  msg % s
            raise Router_Exception(msg)
        except:
            raise
        if self.depth <= 0:
            raise Router_Exception(msg % s)
        self.reinit()
    def set_angle_from_string(self, s):
        '''
        Sets the angle from the string s, where s represents a floating point number.
        '''
        msg = 'Bit angle is "%s".  Set to zero or a postive value.'
        try:
            self.angle = float(s)
        except ValueError as e:
            msg = 'ValueError setting bit angle: %s\n' % (e) + \
                  msg % s
            raise Router_Exception(msg)
        except:
            raise
        if self.angle < 0:
            raise Router_Exception(msg % s)
        self.reinit()
    def reinit(self):
        '''
        Reinitializes internal attributes that are dependent on width
        and angle.
        '''
        self.halfwidth = self.width // 2
        if 2 * self.halfwidth != self.width:
            raise Router_Exception('Router-bit width must be an even number of intervals!')
        self.offset = 0 # ensure exactly 0 for angle == 0
        if self.angle > 0:
            self.offset = self.depth * math.tan(self.angle * math.pi / 180)
        self.neck = self.width - 2 * self.offset
    def scale(self, s):
        '''Scales dimensions by the factor s'''
        self.width = my_round(self.width * s)
        self.width += self.width % 2
        self.depth = my_round(self.depth * s)
        self.reinit()
    def change_units(self, new_units):
        '''Changes units to new_units'''
        s = self.units.get_scaling(new_units)
        if s == 1:
            return
        self.width = my_round(self.width * s)
        self.width += self.width % 2
        self.depth = my_round(self.depth * s)
        self.units = new_units
        self.reinit()

class My_Rectangle(object):
    '''
    Stores a rectangle geometry
    '''
    def __init__(self, xL, yB, width, height):
        '''
        xL: left x-coordinate
        yB: bottom y-coordinate
        width: Extent in s
        height: Extent in y
        '''
        self.xL = xL
        self.yB = yB
        self.width = width
        self.height = height
    def xMid(self):
        '''Returns the x-coordinate of the midpoint.'''
        return self.xL + self.width // 2
    def yMid(self):
        '''Returns the y-coordinate of the midpoint.'''
        return self.yB + self.height // 2
    def xAll(self):
        '''Returns the x-coordinates of a closed polygon of the rectangle.'''
        return (self.xL, self.xR(), self.xR(), self.xL, self.xL)
    def yAll(self):
        '''Returns the y-coordinates of a closed polygon of the rectangle.'''
        return (self.yB, self.yB, self.yT(), self.yT(), self.yB)
    def xR(self):
        '''Returns the right (max) x-coordindate'''
        return self.xL + self.width
    def yT(self):
        '''Returns the top (max) y-coordindate'''
        return self.yB + self.height
    def shift(self, xs, ys):
        '''Shift the rectangle by the distances xs and ys'''
        self.xL += xs
        self.yB += ys

class Board(My_Rectangle):
    '''
    Board of wood description.

    width:  Dimension of routed edge (along x-axis)
    height: Dimension perpendicular to routed edge (along y-axis)
    thickness: Dimension into paper or screen.
    icon: Icon image used for fill

    Dimentions are in interval units.
    '''
    def __init__(self, units, width, height=32, thickness=32, icon=None):
        My_Rectangle.__init__(self, 0, 0, width, height)
        self.units = units
        self.thickness = thickness
        self.icon = icon
    def set_width_from_string(self, s):
        '''
        Sets the width from the string s, following requirements from units.string_to_intervals().
        '''
        msg = 'Board width is "%s".  Set to a postive value.'
        try:
            self.width = self.units.string_to_intervals(s)
        except ValueError as e:
            msg = 'ValueError setting board width: %s\n' % (e) + \
                  msg % s
            raise Router_Exception(msg)
        except:
            raise
        if self.width <= 0:
            raise Router_Exception(msg % s)
    def set_height_from_string(self, s):
        '''
        Sets the height from the string s, following requirements from units.string_to_intervals().
        '''
        msg = 'Board height is "%s".  Set to a postive value.'
        try:
            self.height = self.units.string_to_intervals(s)
        except ValueError as e:
            msg = 'ValueError setting board height: %s\n' % (e) + \
                  msg % s
            raise Router_Exception(msg)
        except:
            raise
        if self.height <= 0:
            raise Router_Exception(msg % s)
    def change_units(self, new_units):
        '''Changes units to new_units'''
        s = self.units.get_scaling(new_units)
        if s == 1:
            return
        self.width = my_round(self.width * s)
        self.height = my_round(self.height * s)
        self.thickness = my_round(self.thickness * s)

class Cut(object):
    '''
    Cut description.

    Attributes:

    xmin: min x-location of cut.
    xmax: max x-location of cut.
    passes: Array of router passes to make the cut, indicating the center of the bit
    midPass: The particle pass in passes that is centered (within an interval)
             on the cut
    '''
    def __init__(self, xmin, xmax):
        self.xmin = xmin
        self.xmax = xmax
        self.passes = []
    def validate(self, bit, board):
        '''
        Checks whether the attributes of the cut are valid.
        '''
        if self.xmin >= self.xmax:
            raise Router_Exception('cut xmin = %d, xmax = %d: '\
                                   'Must have xmax > xmin!' % (self.xmin, self.xmax))
        if self.xmin < 0:
            raise Router_Exception('cut xmin = %d, xmax = %d: '\
                                   'Must have xmin >=0!' % (self.xmin, self.xmax))
        if self.xmax > board.width:
            raise Router_Exception('cut xmin = %d, xmax = %d:'
                                   ' Must have xmax < board width (%d)!'\
                                   % (self.xmin, self.xmax, board.width))
        if self.xmax - self.xmin < bit.width and self.xmin > 0 and self.xmax < board.width:
            raise Router_Exception('cut xmin = %d, xmax = %d: '\
                                   'Bit width (%d) too large for this cut!'\
                                   % (self.xmin, self.xmax, bit.width))
    def make_router_passes(self, bit, board):
        '''Computes passes for the given bit.'''
        # The logic below assumes bit.width is even
        if bit.width % 2 != 0:
            Router_Exception('Router-bit width must be even!')
        self.validate(bit, board)
        # Make the middle pass, centered (within an interval) on the cut
        if self.xmin == 0:
            mid_pass = self.xmax - bit.halfwidth
            xL = max(0, self.xmax - bit.width)
            xR = self.xmax
        elif self.xmax == board.width:
            mid_pass = self.xmin + bit.halfwidth
            xL = self.xmin
            xR = min(board.width, self.xmin + bit.width)
        else:
            mid_pass = (self.xmin + self.xmax) // 2
            xL = mid_pass - bit.halfwidth
            if xL < self.xmin: # cut width must be odd
                xL = self.xmin
                mid_pass = self.xmin + bit.halfwidth
            xR = min(xL + bit.width, board.width)
        if xL < self.xmin and self.xmin > 0:
            Router_Exception('Exceeded left part of a cut!')
        if xR > self.xmax and self.xmax < board.width:
            Router_Exception('Exceeded right part of a cut!')
        self.passes = [mid_pass]
        # Finish passes to left of the middle pass
        while xL > self.xmin:
            xL = max(xL - bit.width, self.xmin)
            self.passes.append(xL + bit.halfwidth)
        # Finish passes to right of the middle pass
        while xR < self.xmax:
            xR = min(xR + bit.width, self.xmax)
            self.passes.append(xR - bit.halfwidth)
        # Sort the passes
        self.passes = sorted(self.passes)

def adjoining_cuts(cuts, bit, board):
    '''
    Given the cuts on an edge, computes the cuts on the adjoining edge.

    cuts: An array of Cut objects

    Returns an array of Cut objects
    '''
    nc = len(cuts)
    adjCuts = []
    # if the left-most input cut does not include the left edge, add an
    # adjoining cut that includes the left edge
    if cuts[0].xmin > 0:
        left = 0
        right = my_round(cuts[0].xmin + bit.offset)
        adjCuts = [Cut(left, right)]
    # loop through the input cuts and form an adjoining cut, formed
    # by looking where the previous cut ended and the current cut starts
    for i in lrange(1, nc):
        left = my_round(cuts[i-1].xmax - bit.offset)
        right = max(left + bit.width, my_round(cuts[i].xmin + bit.offset))
        adjCuts.append(Cut(left, right))
    # if the right-most input cut does not include the right edge, add an
    # adjoining cut that includes this edge
    if cuts[-1].xmax < board.width:
        left = my_round(cuts[-1].xmax - bit.offset)
        right = board.width
        adjCuts.append(Cut(left, right))
    return adjCuts

def board_coords(board, cuts, bit, joint_edge):
    '''
    Compute the perimeter coordinates of a board with a routed edge.

    board: A board object
    cuts: An array of Cut objects, representing the routed edge.
    bit: A Router_Bit object.
    joint_edge: Edge that is routed.  So far, valid values are 'top'
                and 'bottom'.
    '''
    # Set the starting point (xOrg, yOrg) as the lower-left coordinate
    # the joint on the top and the upper-right for the botoom.
    # sign is used so that this algorithm works for both 'top' and 'bottom'
    # For sign+, we'll go clockwise and sign-, counter-clockwise.
    # The idea is to traverse the routed edge always in the +x direction.
    xOrg = board.xL
    if joint_edge == 'top':
        sign = 1
        yOrg = board.yB
    else:
        sign = -1
        yOrg = board.yT()
    # determine the 2 left-edge points, accounting for whether the first cut
    # includes this edge or not.
    x = [xOrg, xOrg]
    y = [yOrg]
    yNocut = y[0] + sign * board.height # y-location of uncut edge
    yCut = yNocut - sign * bit.depth   # y-location of routed edge
    if cuts[0].xmin > 0:
        y.append(yNocut)
    else:
        y.append(yCut)
    # loop through the cuts and add them to the perimeter
    for c in cuts:
        if c.xmin > 0:
            # on the surface, start of cut
            x.append(c.xmin + xOrg + bit.offset)
            y.append(yNocut)
        # at the cut depth, start of cut
        x.append(c.xmin + xOrg)
        y.append(yCut)
        # at the cut depth, end of cut
        x.append(c.xmax + xOrg)
        y.append(yCut)
        if c.xmax < board.width:
            # at the surface, end of cut
            x.append(c.xmax + xOrg - bit.offset)
            y.append(yNocut)
    # add the last point on the top and bottom, at the right edge,
    # accounting for whether the last cut includes this edge or not.
    if cuts[-1].xmax < board.width:
        x.append(xOrg + board.width)
        y.append(yNocut)
    # add the right-most corner point, on the unrouted edge
    x.append(xOrg + board.width)
    y.append(y[0])
    # close the polygon by adding the first point
    x.append(x[0])
    y.append(y[0])
    return (x, y)

class Joint_Geometry(object):
    '''
    Computes and stores all of the geometry attributes of the joint.
    '''
    def __init__(self, template, board, bit, spacing, margins):
        self.template = template
        self.board = board
        self.bit = bit
        self.spacing = spacing

        # determine b-cuts from the a-cuts
        self.aCuts = spacing.cuts
        self.bCuts = adjoining_cuts(self.aCuts, bit, board)

        # determine the router passes for the cuts
        for c in self.aCuts:
            c.make_router_passes(bit, board)
        for c in self.bCuts:
            c.make_router_passes(bit, board)

        # Create the corners of the template
        self.rect_T = My_Rectangle(margins.left, margins.bottom,
                                   template.length, template.height)

        # The sub-rectangle in the template of the board's width
        # (no template margines)
        self.board_T = My_Rectangle(self.rect_T.xL + template.margin, self.rect_T.yB, \
                                    board.width, template.height)

        # Determine board-B coordinates
        self.board_B = deepcopy(board)
        self.board_B.shift(self.board_T.xL, self.rect_T.yT() + margins.sep)
        (self.xB, self.yB) = board_coords(self.board_B, self.bCuts, bit, 'top')

        # Determine board-A coordinates
        self.board_A = deepcopy(self.board_B)
        self.board_A.shift(0, board.height + margins.sep)
        (self.xA, self.yA) = board_coords(self.board_A, self.aCuts, bit, 'bottom')
