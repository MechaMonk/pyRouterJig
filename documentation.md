---
layout: default
title: pyRouterJig Documentation
---

Using pyRouterJig
==================

Note that pyRouterJig is in it\'s early development stage.  Many bugs likely
still exist.  I know how frustrating it can be to try to get software to
work.  If you contact me, I\'ll try to help, but please keep in mind that I also have a day job.

When you start pyRouterJig, you should see something like the image below (the
window may need to be resized in order to look exactly like this image):

<figure>
<img src="{{ site.baseurl }}/opening_screen_shot.png" alt="Opening screenshot with tooltip on Bit Width">
<figcaption>
<b>Figure 1.</b>  Opening screen shot.  The mouse cursor is located over the Bit Width
text box, so that its tooltip appears.
</figcaption>
</figure>

The default joint is a box joint, with the fingers equally spaced, over a
width of 7 1/2\".  The upper portion of the window draws the current joint,
with the labels \"Board-A\" and \"Board-B\" on the boards of the joint.  Below
the boards is the corresponding Incra template.  This template may be cut out
and used in an Incra LS Positioner.  Below the template is a concise title
that summarizes the properties of the joint.  A vertical dashed line denotes
the center of the boards.   The figure containing the
boards, template, and title may be saved to a file by hitting the <b>Save</b>
button on the lower left of the window, finding the <b>Save</b> option in the
pull-down menus, or pressing the key combination `Ctrl-S`.

The lower part of the window allows you to interactively change the parameters
for the joint.  The figure is re-drawn after each change.  At the lower left,
you can see the following input parameters, which are available for any
finger-spacing algorithm:

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

Also shown in Fig. 1 is a \"tooltip\", which is a small window that appears when
you hover the mouse over an available parameter.  In the case above, the mouse
is hovering above the <b>Bit Width</b> parameter.

As an example, if we change <b>Bit Angle</b> to 7 degrees, we obtain the
dovetail joint shown in Figure 2 below:

<figure>
<img src="{{ site.baseurl }}/dovetail_screen_shot.png" alt="Dovetail
example.">
<figcaption>
<b>Figure 2.</b>  Dovetail example.  Compared to Fig. 1, the <b>Bit Angle</b>
has been changed to 7 degrees.
</figcaption>
</figure>

Throughout the documentation of pyRouterJig, we refer to a \"finger\" not only
as the traditional finger of a box joint, but also generically to refer to a
pin or tail of a dovetail joint.  There are currently two finger-spacing
algorithms:

* <b>Equal:</b> In this case, the fingers are equally spaced.  Figures 1 and 2
  are examples.
  There are three inputs that affect this algorithm:

  1. <b>B-spacing:</b> This slider allows you to specify additional spacing between
    the Board-B fingers.  Figure 3 shows an example of increasing this parameter.
  2. <b>Width:</b> This slider allows you to specify additional width added
    to both Board-A and Board-B fingers.  
    Figure 4 shows an example of increasing this parameter.
  3. <b>Centered:</b> This input is only available for straight bits (bit
    angle = 0).  If this box is checked, a finger is always centered on
    the board.  Otherwise, a full finger is started on the left edge, which
    will result in a centerd finger only if the finger width divides into the
    board width an odd number of times.
    Figure 5 shows an example of a non-centered pattern.

* <b>Variable:</b> In this case a large finger is centered on the board,
  and the fingers decrease in size proportional to the distance to the center.
  There is one input that affects this algorithm:

  1. <b>Fingers:</b> This slider allows you to specify the number of
    fingers.  At its minimum value, the width of the center finger is maximized. At
    its maximum value, the width of the center finger is minimized, and the result is
    the same as equally-spaced with, zero \"B-spacing\", zero \"Width\", and
    the \"Centered\" option checked.

Figure 6 shows an example of a Variable-spaced box joint.

<figure>
<img src="{{ site.baseurl }}/bspacing_screen_shot.png" alt="B-spacing example">
<figcaption>
<b>Figure 3.</b>  Effect of B-spacing option.  Compared to Fig. 1, the <b>B-spacing</b>
slider been moved to a value of 1 17/32".
</figcaption>
</figure>

<figure>
<img src="{{ site.baseurl }}/width_screen_shot.png" alt="Width example.">
<figcaption>
<b>Figure 4.</b>  Effect of Width option.  Compared to Fig. 1, the <b>Width</b>
slider been moved to a value of 27/32".
</figcaption>
</figure>

<figure>
<img src="{{ site.baseurl }}/centered_screen_shot.png" alt="Centered example.">
<figcaption>
<b>Figure 5.</b>  Effect of Centered option.  Compared to Fig. 1, the <b>Board
Width</b> has been changed to 7" and the <b>Centered</b> option unclicked.
</figcaption>
</figure>

<figure>
<img src="{{ site.baseurl }}/variable_screen_shot.png" alt="Variable spacing example.">
<figcaption>
<b>Figure 6.</b>  Variable spacing option.  Compared to Fig. 1, the
<b>Variable</b> tab has been clicked and the <b>Fingers</b> slider moved to a
value of 5.
</figcaption>
</figure>

The sliders can be moved by using either dragging the mouse, or my clicking on the
slider and using the left and right arrow keys for small changes and Page Up
and Page Down for large changes.

Printing
========

For now, pyRouterJig does not have the capability to print the figure
directly.  Instead, you must save the figure (described above) to a
supported image format, and then print the image using another applicaiton.
On the Mac, I prefer to save as a PDF file and use <b>Preview.app</b> to
print.  For the Incra template, it\'s important that these operations maintain
the true dimensions of the template on the printed page.  I\'m still working
on methods to make this operation more reliable and to work on all computing platforms.

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

Incra Template
==============

As mentioned abvoe, the Incra template may be cut out and used in a Incra LS
Positioner fence.  Referring to any of the figures above, the template needs
some explaination:

* I don\'t have a color printer.  So I decided to put the Board-A router passes on the
  upper half of the template and the Board-A passes on the lower half.
* The router passes are labeled with their ordering and the Board letter (A or B), unless
  consecutve cuts are too close together.  An example is shown in Figure 6,
  where the passes 3A, 9A, 2B, 3B, 11B, and 12B are not labeled. You should be able to figure out
  the ordering from a neighboring pass that is labeled.
* For cuts that are wider than the <b>Bit Width</b>, the passes are made
  symmetric on the cut.  That is, at a minimum a pass is always placed
  at the center and at least one more pass on either side of the center pass.
  I assume this makes for more symmetric fingers, but I haven\'t tested this
  extensively, and it does add to the number of passes you have to do.
  Currently, there\'s no way to turn this "feature" off.
* The gray regions are margins for the template, outside the board\'s width.
  It\'s possible for a pass to be placed in the gray region, if the outer
  fingers are narrower than the <b>Bit Width</b>.
* Of course, it\'s critical that your printer not distort the template when
  printing the template on paper.  I have a cheap inkjet printer that
  consistently distorts the template about 1/32" over 4".  This is well
  outside the accuracy of Incra fence.  Fortunately for me, a friend\'s laser printer
  is very accurate.  After printing, make sure you check the dimensions of the template.


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
will certainly give credit to those who help make these or any other
improvements!  If you\'re thinking of contributing, let me know, because I may
have already started on some of these.

* Windows and Linux Support.  If you can help test and improve pyRouterJig on
any platform, particularly Windows and Linux, please contact me.  Ideally, you
know Python and can send me proposed patches (or pull requests on Github).
* Known Bugs.
  1. The redraw after changing a parameter does not resize the figure in the
  same manner as resizing the window with your mouse.  In particular, if you
  can\'t see all of the figure, try resizing your window.
* Features. I\'m working on the following features, but would appreciate help:
  * Cleaning up and beautifying these web pages.
  * Define the option for \"fold-over templates\" that are appropriate for
    hand-cut joints.  This would be an alternative to the Incra template.
  * More friendly error messages and handling.
  * Get rid of the dependence on matplotlib and use PyQt drawing
    directly.  Accurate printing is needed.
  * Allow one to print the figure directly, without having to save to a file
    first and open the file in another application that is able to print it.
    This is apparently a limitation of matplotlib.
  * More spacing options.
  * An interactive GUI to allow manual adjustment of finger positions and
    widths.
  * Consider relaxing the requirement that board and bit dimensions be exact multiples
    of intervals.
  * Double-joint support.
