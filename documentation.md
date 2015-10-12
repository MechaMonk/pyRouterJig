---
title: Documentation
---

Using pyRouterJig
==================

When you start pyRouterJig, you should see something like the image below (the
window may need to be resized in order to look exactly like this image):

![Opening screenshot with tooltip on Bit Width]({{ site.baseurl }}/opening_screen_shot.png "Opening screenshot with tooltip on Bit Width")

The default joint is a box joint, with the fingers equally spaced, over a
width of 7 1/2\".  The upper portion of the window draws the current joint,
with the labels \"Board-A\" and \"Board-B\" on the boards of the joint.  Below
the boards is the corresponding Incra template.  This template may be cut out
and used in an Incra LS Positioner.  Below the template is a concise title
that summarizes the properties of the joint.  The figure containing the
boards, template, and title may be saved to a file by hitting the <b>Save</b>
button on the lower left of the window, finding the <b>Save</b> option in the
pull-down menus, or pressing the key combination `Ctrl-S`.

Alos on the lower left of the window, you can see the following input parameters, 
which are available for any finger-spacing algorithm:

* <b>Board Width [inches|mm]:</b> The board width of the joint.
* <b>Bit Width [inches|mm]:</b>  The maximum cutting width of the router bit.
* <b>Bit Depth [inches|mm]:</b> The cutting depth of the router bit.
* <b>Bit Angle [degrees]:</b> The angle of the router bit.  Zero indicates
  a straight bit (box joint).  Fractional values must be input as a
  floating-point number, such as \"7.5\".

These parameters are changed by entering text for the dimension in their
respective text boxes, shown in the image above.  Moving the cursor outside
the text box, or hitting the Enter key, will automatically update the value
and redraw the figure with the new value.  For English units, the length
values are in inches and may be specified as either a fraction or decimal.
For example, the following are equivalent:

* `7 1/2`
* `7.5`
* `7 1 / 2`
* `7 1 /2`
* `7 1/ 2`

Note that the whitespace around the \"`/`\" is ignored. Fractional values are not
available for metric units.

Also shown above is a \"tooltip\", which is a small window that appears when
you hover the mouse over an available parameter.  In the case above, the mouse
is hovering above the <b>Bit Width</b> parameter.

Throughout the documentation of pyRouterJig, we refer to a \"finger\" not only
as the traditional finger of a box joint, but also generically to refer to a
pin or tail of a dovetail joint.  There are currently two finger-spacing
algorithms:

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

Intervals
=========

pyRouterJig does all of its computations in terms of what we refer
to as \"intervals.\"  By default,

* 1 interval = 1/32\" (English units)
* 1 interval = 1 mm (metric units)

An interval is the resolution of pyRouterJig.  All dimensions used by
pyRouterJig, such as the router-bit width, are rounded to the nearest number
of intervals.  The reason for the default choices above is that these are the
resolutions of the respective [Incra LS Positioner
fence](http://www.incra.com/router_table_fences-ls_positiners.html).  By using
intervals, we ensure that it\'s possible to position the fence at the exact
location desired.  More generally, using intervals (or \"integer arithmetic\")
means that pyRouterJig does not need to be worried about floating-point
errors.

Options File
============

The options file
[options.py](https://github.com/lowrie/pyRouterJig/blob/master/options.py)
specifies advanced options and is located in the source directory.  The file
describes the various options, in detail.
pyRouterJig is still under very active developemnt.  The options described in
[options.py](https://github.com/lowrie/pyRouterJig/blob/master/options.py) and
in a future release may change, be deleted, or be made available in a more
user-friendly manner.  Setting these options requires a basic knowledge of
Python.  Also, if you change
[options.py](https://github.com/lowrie/pyRouterJig/blob/master/options.py)
while pyRouterJig is running, the options will not take effect until you quit
and restart pyRouterJig.

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
* Move

