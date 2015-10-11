---
title: Documentation
---

Intervals
=========

pyRouterJig does all of its computations in terms of what pyRouterJig refers
to as \"intervals.\"  By default, 1 interval is 1/32\" for English units and 1
mm for metric.  An interval is the resolution of pyRouterJig.  All dimensions
used by pyRouterJig, such as the router-bit width, are rounded to the nearest
number of intervals.  The reason for the default choices above is that these
are the resolutions of the respective Incra LS Positioner fence.  By using
intervals, we ensure that it\'s possible to position the fence at the exact
location desired.  More generally, using intervals (or \"integer arithmetic\")
means that pyRouterJig does not need to be worried about floating-point
errors.

Input Parameters
================

Throughout the documentation of pyRouterJig, we refer to a \"finger\" not
only as the traditional finger of a box joint, but also generically to refer to a
pin or tail of a dovetail joint.

pyRouterJig has the following input parameters, for any finger spacing
algorithm:

* <b>Board Width [inches or mm]:</b> The width of the board for the joint.
* <b>Bit Width [inches or mm]:</b>  The maximum cutting width of the router bit.
* <b>Bit Depth [inches or mm]:</b> The cutting depth of the router bit.
* <b>Bit Angle [degrees]:</b> The angle of the router bit.  Zero indicates
  a straight bit (box joint).  Fractional values must be input as a
  floating-point number, such as \"7.5\".

These parameters are changed by entering text for the dimension in their
respective text boxes.  Moving outside the text box will automatically update
the value and redraw the figure with the new value.

The \"inches\" length may be specified as either a fraction or decimal.  For example,
the following are equivalent (an underscore here indicates a space):

* 7_1/2
* 7.5
* 7_1_/_2
* 7_1_/2
* 7_1/_2

There are currently two finger spacing algorithms:

* <b>Equal:</b> In this case, the fingers are equally spaced.
  There are three inputs that affect this algorithm:

  1. <b>B-spacing:</b> This slider allows you to specify additional spacing between
    the Board-B fingers.
  2. <b>Width:</b> This slider allows you to specify additional width added
    to both Board-A and Board-B fingers.
  3. <b>Centered:</b> This input is only available for straight bits (bit
    angle = 0).  If this box is checked, a finger is always centered on
    the board.  Otherwise, a full finger is started on the left edge, which
    will result in a centerd finger only if the finger width divides into the
    board width an odd number of times.

* <b>Variable:</b> In this case a large finger is centered on the board,
  and the fingers decrease in size proportional to the distance to the center.
  There is one input that affects this algorithm:

  1. <b>Fingers:</b> This slider allows you to specify the number of
    fingers.  At its minimum value, the width of the center finger is maximized. At
    its maximum value, the width of the center finger is minimized, and the result is
    the same as equally-spaced with, zero \"B-spacing\", zero \"Width\", and
    the \"Centered\" option checked.


Improvements Needed
===================

I am looking for help to make the improvements outlined in this section.  I
will certainly give credit to those who help make improvements.

Windows and Linux Support
-------------------------

If you can help test and improve pyRouterJig on any platform, particularly
Windows and Linux, please contact me.  Ideally, you know Python and can send
me proposed patches (or pull requests on Github).

Known Bugs
----------

1. The redraw after changing a parameter does not resize the figure in the
same manner as resizing the window with your mouse.  In particular, if you
can\'t see all of the figure, try resizing your window.

Features
--------

I\'m working on the following features, but would appreciate help:

* Cleaning up and beautifying these web pages.
* Define the option for \"fold-over templates\" that are appropriate for
  hand-cut joints.  This would be an alternative to the Incra template.
* More friendly error messages and handling.
* Get rid of the dependence on matplotlib and use PyQt drawing
  directly.  Accurate printing is needed.
* More spacing options.
* An interactive GUI to allow manual adjustment of fingers positions and
  widths.
* Consider relaxing the requirement that board and bit dimensions be exact multiples
of intervals.


