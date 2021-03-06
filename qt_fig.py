###########################################################################
#
# Copyright 2015-2016 Robert B. Lowrie (http://github.com/lowrie)
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
Contains the Qt functionality for drawing the template and boards.
'''
from __future__ import print_function
from __future__ import division
from future.utils import lrange

import router
import utils

from PyQt4 import QtCore, QtGui
#from PySide import QtCore, QtGui

def paint_text(painter, text, coord, flags, shift=(0, 0), angle=0, fill=None):
    '''
    Puts text at coord with alignment flags.

    painter: QPainter object
    text: The text to print.
    coord: The coordinate at which to place the text
    flags: QtCore.Qt alignment flags
    shift: Adjustments in coord, in pixels
    angle: Rotation angle
    fill: If not None, a QBrush that fills the bounding rectangle behind the text.
    '''
    # Save the current transform, then switch to transform that places the origin
    # at coord and rotated by angle.
    transform = painter.transform()
    (x, y) = transform.map(coord[0], coord[1])
    x += shift[0]
    y += shift[1]
    painter.resetTransform()
    painter.translate(x, y)
    painter.rotate(angle)
    # Create a large rectangle and use it to find the bounding rectangle around the text.
    # Find the origin of the rectangle based on the alignment.
    big = 5000
    xorg = 0
    yorg = 0
    if flags & QtCore.Qt.AlignRight:
        xorg = -big
    elif flags & QtCore.Qt.AlignHCenter:
        xorg = -big // 2
    if flags & QtCore.Qt.AlignBottom:
        yorg = -big
    elif flags & QtCore.Qt.AlignVCenter:
        yorg = -big // 2
    rect = QtCore.QRect(xorg, yorg, big, big)
    rect = painter.boundingRect(rect, flags, text)
    # Draw the text
    if fill is not None:
        painter.fillRect(rect, fill)
    painter.drawText(rect, flags, text)
    # restore the original transform
    painter.setTransform(transform)

class Qt_Fig(object):
    '''
    Interface to the qt_driver, using Qt to draw the boards and template.
    '''
    def __init__(self, template, boards, config):
        self.canvas = Qt_Plotter(template, boards, config)
        self.transform = None

    def draw(self, template, boards, bit, spacing, woods):
        '''
        Draws the template and boards
        '''
        self.canvas.draw(template, boards, bit, spacing, woods)

    def print(self, template, boards, bit, spacing, woods):
        '''
        Prints the figure
        '''
        return self.canvas.print_fig(template, boards, bit, spacing, woods)

    def image(self, template, boards, bit, spacing, woods, min_width):
        '''
        Prints the figure to an image
        '''
        return self.canvas.image_fig(template, boards, bit, spacing, woods, min_width)

class Qt_Plotter(QtGui.QWidget):
    '''
    Plots the template and boards using Qt.
    '''
    def __init__(self, template, boards, config):
        QtGui.QWidget.__init__(self)
        self.config = config
        self.fig_width = -1
        self.fig_height = -1
        self.set_fig_dimensions(template, boards)
        # if subsequent passes are less than this value, don't label
        # the pass (in increments)
        #self.sep_annotate = 4
        self.sep_annotate = 0
        self.geom = None
        (r, g, b) = config.background_color
        self.background = QtGui.QBrush(QtGui.QColor(r, g, b))
        self.current_background = self.background
        self.labels = ['B', 'C', 'D', 'E', 'F']
        # font sizes are in 1/32" of an inch
        self.font_size = {'title':4, 'fingers':3, 'template':2, 'boards':4, 'template_labels':3}

    def minimumSizeHint(self):
        '''
        Minimum size for this widget
        '''
        return QtCore.QSize(100, 100)

    def sizeHint(self):
        '''
        Size hint for this widget
        '''
        return QtCore.QSize(self.window_width, self.window_height)

    def set_fig_dimensions(self, template, boards):
        '''
        Computes the figure dimension attributes, fig_width and fig_height, in
        increments.
        Returns True if the dimensions changed.
        '''
        # Try default margins, but reset if the template is too small for margins
        self.margins = utils.Margins(8, self.config.separation,\
                                     self.config.left_margin,\
                                     self.config.right_margin,\
                                     self.config.bottom_margin,\
                                     self.config.top_margin)

        # Set the figure dimensions
        fig_width = template.length + self.margins.left + self.margins.right
        fig_height = template.height + self.margins.bottom + self.margins.top
        for i in lrange(4):
            if boards[i].active:
                fig_height += boards[i].height + self.margins.sep

        if boards[3].active:
            fig_height += template.height + self.margins.sep

        if template.do_caul:
            fig_height += template.height + self.margins.sep

        min_width = 64
        if fig_width < min_width:
            fig_width = min_width
            self.margins.left = (fig_width - template.length) // 2
            self.margins.right = self.margins.left
            fig_width = template.length + self.margins.left + self.margins.right

        dimensions_changed = False
        if fig_width != self.fig_width:
            self.fig_width = fig_width
            dimensions_changed = True
        if fig_height != self.fig_height:
            self.fig_height = fig_height
            dimensions_changed = True

        # The 1200 here is effectively a dpi for the screen
        scale = 1200 * boards[0].units.increments_to_inches(1)
        self.window_width = int(scale * fig_width)
        self.window_height = int(scale * fig_height)

        return dimensions_changed

    def draw(self, template, boards, bit, spacing, woods):
        '''
        Draws the figure
        '''
        # Generate the new geometry layout
        self.set_fig_dimensions(template, boards)
        self.woods = woods
        self.geom = router.Joint_Geometry(template, boards, bit, spacing, self.margins,\
                                          self.config.caul_trim)
        self.current_background = self.background
        self.update()

    def print_fig(self, template, boards, bit, spacing, woods):
        '''
        Prints the figure
        '''
        self.woods = woods
        self.current_background = None

        # Generate the new geometry layout
        self.set_fig_dimensions(template, boards)
        self.geom = router.Joint_Geometry(template, boards, bit, spacing, self.margins,\
                                          self.config.caul_trim)

        # Print through the preview dialog
        printer = QtGui.QPrinter(QtGui.QPrinter.HighResolution)
        printer.setOrientation(QtGui.QPrinter.Landscape)
        printer.setPageMargins(0, 0, 0, 0, QtGui.QPrinter.Inch)
        pdialog = QtGui.QPrintPreviewDialog(printer)
        pdialog.setModal(True)
        pdialog.paintRequested.connect(self.preview_requested)
        return pdialog.exec_()

    def image_fig(self, template, boards, bit, spacing, woods, min_width):
        '''
        Prints the figure to a QImage object
        '''
        self.woods = woods
        self.set_fig_dimensions(template, boards)
        self.geom = router.Joint_Geometry(template, boards, bit, spacing, self.margins,\
                                          self.config.caul_trim)
        self.current_background = self.background

        s = self.size()
        window_ar = float(s.width()) / s.height()
        fig_ar = float(self.fig_width) / self.fig_height
        if window_ar < fig_ar:
            w = max(min_width, s.width())
        else:
            w = max(min_width, int(s.height() * fig_ar))
        h = utils.my_round(w / fig_ar)
        sNew = QtCore.QSize(w, h)

        image = QtGui.QImage(sNew, QtGui.QImage.Format_RGB32)
        painter = QtGui.QPainter()
        painter.begin(image)
        size = image.size()
        painter.fillRect(0, 0, size.width(), size.height(), self.background)
        self.paint_all(painter)
        painter.end()
        return image

    def preview_requested(self, printer):
        '''
        Handles the print preview action.
        '''
        dpi = printer.resolution()
        painter = QtGui.QPainter()
        painter.begin(printer)
        self.paint_all(painter, dpi)
        painter.end()

    def paintEvent(self, event):
        '''
        Handles the paint event, which draws to the screen
        '''
        if self.geom is None:
            return

        painter = QtGui.QPainter(self)
        size = self.size()
        # on the screen, we add a background color:
        painter.fillRect(0, 0, size.width(), size.height(), self.background)
        # paint all of the objects
        self.window_width, self.window_height = self.paint_all(painter)
        # on the screen, highlight the active cuts
        self.draw_active_cuts(painter)
        painter.end()

    def set_font_size(self, painter, param):
        '''
        Sets the font size for type param
        '''
        font_inches = self.font_size[param] / 32.0 * self.geom.bit.units.increments_per_inch
        font = painter.font()
        xx = self.transform.map(font_inches, 0)[0] - self.transform.dx()
        font.setPixelSize(utils.my_round(xx))
        painter.setFont(font)

    def paint_all(self, painter, dpi=None):
        '''
        Paints all the objects.

        painter: A QPainter object
        dpi: The resolution of the painter, in dots-per-inch.  If None, then
             the image is maximized in the window, but maintaining aspect ratio.
        '''
        rw = painter.window()
        window_width = rw.width()
        window_height = rw.height()
        units = self.geom.bit.units

        if dpi is None:
            # transform the painter to maintain the figure aspect ratio in the current
            # window
            window_ar = float(window_width) / window_height
            fig_ar = float(self.fig_width) / self.fig_height
            if fig_ar < window_ar:
                w = utils.my_round(fig_ar * window_height)
                painter.translate((window_width - w) // 2, window_height)
                scale = float(window_height) / self.fig_height
            else:
                h = utils.my_round(window_width / fig_ar)
                painter.translate(0, (window_height + h) // 2)
                scale = float(window_width) / self.fig_width
        else:
            # Scale so that the image is the correct size on the page
            painter.translate(0, window_height)
            scale = float(dpi) / units.increments_per_inch
        painter.scale(scale, -scale)
        self.transform = painter.transform()

        painter.setPen(QtCore.Qt.black)

        # draw the objects
        self.draw_boards(painter)
        self.draw_template(painter)
        self.draw_title(painter)
        self.draw_cut_sizes(painter)

        return (window_width, window_height)

    def draw_passes(self, painter, blabel, cuts, y1, y2, flags, xMid):
        '''
        Draws and labels the router passes on a template or board.
        '''
        board_T = self.geom.board_T
        # brush = QtGui.QBrush(QtCore.Qt.white)
        brush = None
        ip = 0
        if y1 > y2:
            shift = (0, -2)
        else:
            shift = (0, 2)
        passMid = None
        self.set_font_size(painter, 'template')
        for c in cuts[::-1]:
            for p in lrange(len(c.passes) - 1, -1, -1):
                xp = c.passes[p] + board_T.xL()
                ip += 1
                label = '%d%s' % (ip, blabel)
                if xp == xMid:
                    passMid = label
                painter.drawLine(xp, y1, xp, y2)
                if p == 0 or c.passes[p] - c.passes[p-1] > self.sep_annotate:
                    paint_text(painter, label, (xp, y1), flags, shift, -90, fill=brush)
        return passMid

    def draw_alignment(self, painter):
        '''
        Draws the alignment lines on all templates
        '''
        board_T = self.geom.board_T
        board_TDD = self.geom.board_TDD
        board_caul = self.geom.board_caul

        # draw the alignment lines on both templates
        #x = board_T.xL() + passes[iMax] - pMax // 2
        x = board_T.xR() + self.geom.bit.width // 2
        painter.setPen(QtCore.Qt.SolidLine)
        self.set_font_size(painter, 'template')
        label = 'ALIGN'
        flags = QtCore.Qt.AlignTop | QtCore.Qt.AlignHCenter
        for b in [board_T, board_TDD, board_caul]:
            if b is not None:
                y1 = b.yB()
                y2 = b.yT()
                painter.drawLine(x, y1, x, y2)
                paint_text(painter, label, (x, (y1 + y2) // 2), flags, (0, 0), -90)

    def draw_template_rectangle(self, painter, r, b):
        '''
        Draws the geometry of a template
        '''
        # Fill the entire template as white
        painter.fillRect(r.xL(), r.yB(), r.width, r.height, QtCore.Qt.white)

        # Fill the template margins with a grayshade
        brush = QtGui.QBrush(QtGui.QColor(220, 220, 220))
        painter.fillRect(r.xL(), r.yB(), b.xL() - r.xL(), r.height, brush)
        painter.fillRect(b.xR(), r.yB(), r.xR() - b.xR(), r.height, brush)

        # Draw the template bounding box
        painter.drawRect(r.xL(), r.yB(), r.width, r.height)

    def draw_template(self, painter):
        '''
        Draws the Incra templates
        '''
        rect_T = self.geom.rect_T
        board_T = self.geom.board_T
        boards = self.geom.boards

        xMid = board_T.xMid()
        centerline = []
        centerline_TDD = []

        self.draw_template_rectangle(painter, rect_T, board_T)
        if boards[3].active:
            rect_TDD = self.geom.rect_TDD
            board_TDD = self.geom.board_TDD
            self.draw_template_rectangle(painter, rect_TDD, board_TDD)
            rect_top = rect_TDD
        else:
            rect_top = rect_T

        flagsL = QtCore.Qt.AlignLeft | QtCore.Qt.AlignVCenter
        flagsR = QtCore.Qt.AlignRight | QtCore.Qt.AlignVCenter

        frac_depth = 0.95 * self.geom.bit.depth
        # Draw the router passes
        # ... do the top board passes
        y1 = boards[0].yB()
        y2 = y1 + frac_depth
        self.draw_passes(painter, 'A', boards[0].bottom_cuts, rect_top.yMid(),\
                         rect_top.yT(), flagsR, xMid)
        pm = self.draw_passes(painter, 'A', boards[0].bottom_cuts, y1, y2, flagsR, xMid)
        if pm is not None:
            if boards[3].active:
                centerline_TDD.append(pm)
            else:
                centerline.append(pm)
        label_bottom = 'A,B'
        label_top = None
        i = 0
        # Do double-double passes
        if boards[3].active:
            painter.setPen(QtCore.Qt.DashLine)
            y1 = boards[3].yT()
            y2 = y1 - frac_depth
            self.draw_passes(painter, self.labels[i], boards[3].top_cuts, rect_TDD.yMid(), \
                             rect_TDD.yT(), flagsR, xMid)
            pm = self.draw_passes(painter, self.labels[i], boards[3].top_cuts, y1, y2, flagsL, xMid)
            if pm is not None:
                centerline_TDD.append(pm)
            painter.setPen(QtCore.Qt.SolidLine)
            y1 = boards[3].yB()
            y2 = y1 + frac_depth
            self.draw_passes(painter, self.labels[i + 1], boards[3].bottom_cuts, rect_TDD.yMid(), \
                             rect_TDD.yB(), flagsL, xMid)
            pm = self.draw_passes(painter, self.labels[i + 1], boards[3].bottom_cuts, y1, y2, flagsR, xMid)
            if pm is not None:
                centerline_TDD.append(pm)
            label_bottom = 'D,E,F'
            label_top = 'A,B,C'
            i += 2
        # Do double passes
        if boards[2].active:
            painter.setPen(QtCore.Qt.DashLine)
            y1 = boards[2].yT()
            y2 = y1 - frac_depth
            self.draw_passes(painter, self.labels[i], boards[2].top_cuts, rect_T.yMid(), \
                             rect_T.yT(), flagsR, xMid)
            pm = self.draw_passes(painter, self.labels[i], boards[2].top_cuts, y1, y2, flagsL, xMid)
            if pm is not None:
                centerline.append(pm)
            y1 = boards[2].yB()
            y2 = y1 + frac_depth
            self.draw_passes(painter, self.labels[i + 1], boards[2].bottom_cuts, rect_T.yMid(), \
                             rect_T.yB(), flagsL, xMid)
            pm = self.draw_passes(painter, self.labels[i + 1], boards[2].bottom_cuts, y1, y2, flagsR, xMid)
            if pm is not None:
                centerline.append(pm)
            painter.setPen(QtCore.Qt.SolidLine)
            if not boards[3].active:
                label_bottom = 'A,B,C,D'
            i += 2

        # ... do the bottom board passes
        y1 = boards[1].yT()
        y2 = y1 - frac_depth
        self.draw_passes(painter, self.labels[i], boards[1].top_cuts, rect_T.yMid(), \
                         rect_T.yB(), flagsL, xMid)
        pm = self.draw_passes(painter, self.labels[i], boards[1].top_cuts, y1, y2, flagsL, xMid)
        if pm is not None:
            centerline.append(pm)

        # ... draw the caul template and do its passes
        if self.geom.template.do_caul:
            rect_caul = self.geom.rect_caul
            board_caul = self.geom.board_caul
            top = self.geom.caul_top
            bottom = self.geom.caul_bottom
            self.draw_template_rectangle(painter, rect_caul, board_caul)
            centerline_caul = []
            pm = self.draw_passes(painter, 'A', top, rect_caul.yMid(), rect_caul.yT(), flagsR, xMid)
            if pm is not None:
                centerline_caul.append(pm)
            pm = self.draw_passes(painter, self.labels[i], bottom, rect_caul.yMid(),\
                                  rect_caul.yB(), flagsL, xMid)
            if pm is not None:
                centerline_caul.append(pm)
            self.set_font_size(painter, 'template_labels')
            label = 'Cauls'
            if len(centerline_caul) > 0:
                label += '\nCenter: ' + centerline_caul[0]
            else:
                painter.setPen(QtCore.Qt.DashLine)
                painter.drawLine(xMid, rect_caul.yB(), xMid, rect_caul.yT())
            paint_text(painter, label, (rect_caul.xL(), rect_caul.yMid()), flagsL, (5, 0))
            paint_text(painter, label, (rect_caul.xR(), rect_caul.yMid()), flagsR, (-5, 0))

        # Label the templates
        self.set_font_size(painter, 'template_labels')
        if len(centerline) > 0:
            label_bottom += '\nCenter: ' + centerline[0]
        else:
            painter.setPen(QtCore.Qt.DashLine)
            painter.drawLine(xMid, rect_T.yB(), xMid, rect_T.yT())
        paint_text(painter, label_bottom, (rect_T.xL(), rect_T.yMid()), flagsL, (5, 0))
        paint_text(painter, label_bottom, (rect_T.xR(), rect_T.yMid()), flagsR, (-5, 0))
        if label_top is not None:
            if len(centerline_TDD) > 0:
                label_top += '\nCenter: ' + centerline_TDD[0]
            else:
                painter.setPen(QtCore.Qt.DashLine)
                painter.drawLine(xMid, rect_TDD.yB(), xMid, rect_TDD.yT())
            paint_text(painter, label_top, (rect_TDD.xL(), rect_TDD.yMid()), flagsL, (5, 0))
            paint_text(painter, label_top, (rect_TDD.xR(), rect_TDD.yMid()), flagsR, (-5, 0))

        self.draw_alignment(painter)

    def draw_one_board(self, painter, board, bit):
        '''
        Draws a single board
        '''
        if not board.active:
            return
        (x, y) = board.perimeter(bit)
        painter.save()
        pen = QtGui.QPen(QtCore.Qt.black)
        pen.setWidthF(0)
        painter.setPen(pen)
        icon = self.woods[board.wood]
        if isinstance(icon, str):
            brush = QtGui.QBrush(QtGui.QPixmap(icon))
        else:
            brush = QtGui.QBrush(QtCore.Qt.black, icon)
        (inverted, invertable) = self.transform.inverted()
        brush.setMatrix(inverted.toAffine())
        painter.setBrush(brush)
        n = len(x)
        poly = QtGui.QPolygonF()
        for i in lrange(n):
            poly.append(QtCore.QPointF(x[i], y[i]))
        painter.drawPolygon(poly)
        painter.restore()

    def draw_boards(self, painter):
        '''
        Draws all the boards
        '''

        # Draw the A and B boards
        for i in lrange(4):
            self.draw_one_board(painter, self.geom.boards[i], self.geom.bit)

        # Label the boards
        painter.setPen(QtCore.Qt.SolidLine)
        x1 = self.geom.boards[0].xL() - self.geom.bit.width // 2
        x2 = self.geom.boards[0].xL() - self.geom.bit.width // 4
        flags = QtCore.Qt.AlignRight | QtCore.Qt.AlignVCenter
        self.set_font_size(painter, 'boards')

        y = self.geom.boards[0].yB()
        p = (x1, y)
        paint_text(painter, 'A', p, flags, (-3, 0))
        painter.drawLine(x1, y, x2, y)

        i = 0 # index in self.labels

        if self.geom.boards[3].active:
            y = self.geom.boards[3].yT()
            p = (x1, y)
            paint_text(painter, 'B', p, flags, (-3, 0))
            painter.drawLine(x1, y, x2, y)
            y = self.geom.boards[3].yB()
            p = (x1, y)
            paint_text(painter, 'C', p, flags, (-3, 0))
            painter.drawLine(x1, y, x2, y)
            i = 2
        if self.geom.boards[2].active:
            y = self.geom.boards[2].yT()
            p = (x1, y)
            paint_text(painter, self.labels[i], p, flags, (-3, 0))
            painter.drawLine(x1, y, x2, y)
            y = self.geom.boards[2].yB()
            p = (x1, y)
            paint_text(painter, self.labels[i + 1], p, flags, (-3, 0))
            painter.drawLine(x1, y, x2, y)
            i += 2

        y = self.geom.boards[1].yT()
        p = (x1, y)
        paint_text(painter, self.labels[i], p, flags, (-3, 0))
        painter.drawLine(x1, y, x2, y)

    def cut_polygon(self, c):
        '''
        Forms the polygon for the cut corresponding to the cut c
        '''
        boards = self.geom.boards
        xLT = boards[0].xL() + c.xmin
        xRT = boards[0].xL() + c.xmax
        xLB = xLT
        xRB = xRT
        if c.xmin > 0:
            xLB += self.geom.bit.offset
        if c.xmax < self.geom.boards[0].width:
            xRB -= self.geom.bit.offset
        yB = boards[0].yB()
        yT = yB + self.geom.bit.depth
        poly = QtGui.QPolygonF()
        poly.append(QtCore.QPointF(xLT, yT))
        poly.append(QtCore.QPointF(xRT, yT))
        poly.append(QtCore.QPointF(xRB, yB))
        poly.append(QtCore.QPointF(xLB, yB))
        poly.append(QtCore.QPointF(xLT, yT))
        return poly

    def draw_active_cuts(self, painter):
        '''
        If the spacing supports it, highlight the active cuts and
        draw their limits
        '''
        # draw the perimeter of the cursor cut
        f = self.geom.spacing.cursor_cut
        if f is None:
            return
        poly = self.cut_polygon(self.geom.boards[0].bottom_cuts[f])
        painter.save()
        pen = QtGui.QPen(QtCore.Qt.blue)
        pen.setWidth(1)
        painter.setPen(pen)
        painter.drawPolyline(poly)
        painter.restore()

        # initialize limits
        xminG = self.geom.boards[0].width
        xmaxG = 0

        # draw the active cuts filled, and track the limits
        painter.save()
        brush = QtGui.QBrush(QtGui.QColor(255, 0, 0, 75))
        painter.setBrush(brush)
        for f in self.geom.spacing.active_cuts:
            poly = self.cut_polygon(self.geom.boards[0].bottom_cuts[f])
            painter.drawPolygon(poly)
            # keep track of the limits
            (xmin, xmax) = self.geom.spacing.get_limits(f)
            xminG = min(xminG, xmin)
            xmaxG = max(xmaxG, xmax)
        painter.restore()

        # draw the limits
        painter.save()
        xminG += self.geom.boards[0].xL()
        xmaxG += self.geom.boards[0].xL()
        yB = self.geom.boards[0].yB()
        yT = self.geom.boards[0].yT()
        painter.setPen(QtCore.Qt.green)
        painter.drawLine(xminG, yB, xminG, yT)
        painter.drawLine(xmaxG, yB, xmaxG, yT)
        painter.restore()

    def draw_title(self, painter):
        '''
        Draws the title
        '''
        self.set_font_size(painter, 'title')
        units = self.geom.bit.units
        title = self.geom.spacing.description
        title += '\nBoard width: '
        title += units.increments_to_string(self.geom.boards[0].width, True)
        if self.geom.boards[2].active:
            title += '   Double Thickness: '
            title += units.increments_to_string(self.geom.boards[2].dheight, True)
            if self.geom.boards[3].active:
                title += ', '
                title += units.increments_to_string(self.geom.boards[2].dheight, True)
        title += '    Bit: '
        if self.geom.bit.angle > 0:
            title += '%.1f deg. dovetail' % self.geom.bit.angle
        else:
            title += 'straight'
        title += ', width: '
        title += units.increments_to_string(self.geom.bit.width, True)
        title += ', depth: '
        title += units.increments_to_string(self.geom.bit.depth, True)
        flags = QtCore.Qt.AlignHCenter | QtCore.Qt.AlignTop
        p = (self.geom.board_T.xMid(), self.margins.bottom)
        paint_text(painter, title, p, flags, (0, 5))

    def draw_cut_sizes(self, painter):
        '''
        Annotates the cut sizes on each board
        '''
        self.set_font_size(painter, 'fingers')
        # Determine the cuts that are adjacent to board-A and board-B
        acuts = self.geom.boards[1].top_cuts
        bcuts = self.geom.boards[0].bottom_cuts
        if self.geom.boards[2].active:
            bcuts = self.geom.boards[2].bottom_cuts
            if self.geom.boards[3].active:
                acuts = self.geom.boards[3].top_cuts
            else:
                acuts = self.geom.boards[2].top_cuts
        # Draw the router passes
        # ... do the B cuts
        flags = QtCore.Qt.AlignHCenter | QtCore.Qt.AlignTop
        shift = (0, 8)
        for c in bcuts:
            x = self.geom.boards[1].xL() + (c.xmin + c.xmax) // 2
            y = self.geom.boards[1].yT()
            label = '%d' % (c.xmax - c.xmin)
            p = (x, y)
            paint_text(painter, label, p, flags, shift, fill=self.current_background)
        # ... do the A cuts
        flags = QtCore.Qt.AlignHCenter | QtCore.Qt.AlignBottom
        shift = (0, -8)
        for c in acuts:
            x = self.geom.boards[0].xL() + (c.xmin + c.xmax) // 2
            y = self.geom.boards[0].yB()
            label = '%d' % (c.xmax - c.xmin)
            p = (x, y)
            paint_text(painter, label, p, flags, shift, fill=self.current_background)

