---
layout: default
title: pyRouterJig Documentation
---

Note that {{ site.codename }} is in its early development stage.  Many bugs likely
still exist.  I know how frustrating it can be to try to get broken software
to work.  If you contact me, I\'ll try to help, but please keep in mind that I
also have a day job.

<a name="page-index"></a>

This page is split into the following sections ("Return to index" link at the
bottom of each section returns to this location):

* [Overview of Features](#overview-of-features)
* [Finger Spacing Options](#finger-spacing-options)
* [Drop-Down Menus](#drop-down-menus)
* [Printing](#printing)
* [Intervals Explained](#intervals-explained)
* [Incra Template Details](#incra-template-details)
* [Options File](#options-file)
* [Needed Improvements](#needed-improvements)

<a name="overview-of-features"></a>

Overview of Features
====================

When you start {{ site.codename }}, you should see something like the image below (the
window may need to be resized in order to look exactly like this image):

<figure>
<a name="figure1"></a>
<img src="{{ site.baseurl }}/opening_screen_shot.png" alt="Opening screenshot with tooltip on Bit Width">
<figcaption>
<b>Figure 1.</b>  Opening screen shot.  The screen shot doesn\'t show the
mouse pointer, which is located over the <b>Bit Width</b> text box so that its tooltip appears.
</figcaption>
</figure>

The default joint is a box joint, with the fingers equally spaced, over a
width of 7 1/2\".  The upper portion of the window draws the current joint,
with the labels \"Board-A\" and \"Board-B\" on the boards of the joint.  Below
the boards is the corresponding Incra template.  This template may be cut out
and used in an Incra LS Positioner.  Below the template is a concise title
that summarizes the properties of the joint.  A vertical dashed line denotes
the center of the boards.   The graphics containing the
boards, template, and title may be saved to a file by hitting the <b>Save</b>
button on the lower left of the window, finding the <b>Save</b> option in the
pull-down menu, or pressing the key combination `Ctrl-S` (`Command-S` on Mac).

The lower part of the window allows you to interactively change the parameters
for the joint.  The joint is re-drawn after each change.  At the lower left,
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
and redraw the joint with the new value.  For English units, the length
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
dovetail joint shown in [Figure 2](#figure2) below:

<figure>
<a name="figure2"></a>
<img src="{{ site.baseurl }}/dovetail_screen_shot.png" alt="Dovetail
example.">
<figcaption>
<b>Figure 2.</b>  Dovetail example.  Compared to Fig. 1, the <b>Bit Angle</b>
has been changed to 7 degrees.
</figcaption>
</figure>

[Return to index](#page-index)

<a name="finger-spacing-options"></a>

Finger Spacing Options
======================

Throughout the documentation of {{ site.codename }}, we refer to a \"finger\" not only
as the traditional finger of a box joint, but also generically to refer to a
pin or tail of a dovetail joint.  There are currently two finger-spacing
algorithms:

* <b>Equal:</b> In this case, the fingers are equally spaced.  
  Figures [1](#figure1) and [2](#figure2) are examples.
  There are three inputs that affect this algorithm:

  1. <b>B-spacing:</b> This slider allows you to specify additional spacing between
    the Board-B fingers.  [Figure 3](#figure3) shows an example of increasing this parameter.
  2. <b>Width:</b> This slider allows you to specify additional width added
    to both Board-A and Board-B fingers.  
    [Figure 4](#figure4) shows an example of increasing this parameter.
  3. <b>Centered:</b> This input is only available for straight bits (bit
    angle = 0).  If this box is checked, a finger is always centered on
    the board.  Otherwise, a full finger is started on the left edge, which
    will result in a centered finger only if the finger width divides into the
    board width an odd number of times.
    [Figure 5](#figure5) shows an example of a non-centered pattern.

* <b>Variable:</b> In this case a large finger is centered on the board,
  and the fingers decrease in size proportional to the distance to the center.
  There is one input that affects this algorithm:

  1. <b>Fingers:</b> This slider allows you to specify the number of
    fingers.  At its minimum value, the width of the center finger is maximized. At
    its maximum value, the width of the center finger is minimized, and the result is
    the same as equally-spaced with, zero \"B-spacing\", zero \"Width\", and
    the \"Centered\" option checked.

[Figure 6](#figure6) shows an example of a Variable-spaced box joint.

<figure>
<a name="figure3"></a>
<img src="{{ site.baseurl }}/bspacing_screen_shot.png" alt="B-spacing example">
<figcaption>
<b>Figure 3.</b>  Effect of B-spacing option.  Compared to Fig. 1, the <b>B-spacing</b>
slider been moved to a value of 1 17/32".
</figcaption>
</figure>

<figure>
<a name="figure4"></a>
<img src="{{ site.baseurl }}/width_screen_shot.png" alt="Width example.">
<figcaption>
<b>Figure 4.</b>  Effect of Width option.  Compared to Fig. 1, the <b>Width</b>
slider been moved to a value of 27/32".
</figcaption>
</figure>

<figure>
<a name="figure5"></a>
<img src="{{ site.baseurl }}/centered_screen_shot.png" alt="Centered example.">
<figcaption>
<b>Figure 5.</b>  Effect of Centered option.  Compared to Fig. 1, the <b>Board
Width</b> has been changed to 7" and the <b>Centered</b> option unclicked.
</figcaption>
</figure>

<figure>
<a name="figure6"></a>
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

[Return to index](#page-index)

<a name="drop-down-menus"></a>

Drop-Down Menus
===============

Drop-down menus are located at the top of the window.  There are three menus
available:

1. <b>File</b>
* <b>Save (Ctrl-S)</b> Allows you to save the joint diagram to a file.
* <b>Screenshot (Ctrl-W)</b> Saves a screenshot of the window.
* <b>Quit (Ctrl-Q)</b> Quits {{ site.codename}}.  If you\'ve made any changes
to the joint and haven\'t saved it, then you\'ll be warned.
1. <b>Units</b>
1. <b>Help</b> Very limited, for now:
* <b>About (Ctrl-A)</b> Pops up a window showing the version and license.

On the Mac, for the keyboard shortcuts use the `Command` key rather than `Ctrl`.

[Return to index](#page-index)

<a name="printing"></a>

Printing
========

For now, {{ site.codename }} does not have the capability to print the joint
directly.  Instead, you must save the joint (described in the previous section) to a
supported image format, and then print the image using another application.
On the Mac, I prefer to save as a PDF file and use `Preview.app` to
print.  For the Incra template, it\'s important that these operations maintain
the true dimensions of the template on the printed page.  I\'m still working
on methods to make this operation more reliable and to work on all computing platforms.

[Return to index](#page-index)

<a name="intervals-explained"></a>

Intervals Explained
===================

{{ site.codename }} does all of its computations in terms of what we refer
to as \"intervals.\"  By default,

* 1 interval = 1/32\" (English units)
* 1 interval = 1 mm (metric units)

An interval is the resolution of {{ site.codename }}.  All dimensions used by
{{ site.codename }}, such as the router-bit width, are rounded to the nearest number
of intervals.  The reason for the default choices above is that these are the
resolutions of the respective [Incra LS Positioner
fence](http://www.incra.com/router_table_fences-ls_positiners.html).  By using
intervals, we ensure that it\'s possible to position the fence at the exact
location desired.  More generally, using intervals (or \"integer arithmetic\")
means that {{ site.codename }} does not need to be worried about floating-point
errors.

[Return to index](#page-index)

<a name="incra-template-details"></a>

Incra Template Details
======================

As mentioned above, the Incra template may be cut out and used in a Incra LS
Positioner fence.  Referring to any of the figures above, the template needs
some explanation:

* I don\'t have a color printer.  So I decided to put the Board-A router passes on the
  upper half of the template and the Board-A passes on the lower half.
* The router passes are labeled with their ordering and the Board letter (A or B), unless
  consecutive cuts are too close together.  An example is shown in [Figure 6](#figure6),
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
  fingers are narrower than half of the <b>Bit Width</b>.
* Of course, it\'s critical that your printer not distort the template when
  printing the template on paper.  I have a cheap inkjet printer that
  consistently distorts the template about 1/32" over 4".  This is well
  outside the accuracy of an Incra fence.  Fortunately for me, a friend\'s laser printer
  is very accurate.  After printing, make sure you check the dimensions of the template.

[Return to index](#page-index)

<a name="options-file"></a>

Options File
============

The options file
[options.py](https://github.com/lowrie/pyRouterJig/blob/master/options.py)
specifies advanced options and is located in the source directory.  The file
itself describes the various options, in detail.  {{ site.codename }} is still under
very active development.  Consequently, the options described in
[options.py](https://github.com/lowrie/pyRouterJig/blob/master/options.py) and
in a future release may change, be deleted, or be made available in a more
user-friendly manner.  Setting these options requires a basic knowledge of
Python.  Also, if you change
[options.py](https://github.com/lowrie/pyRouterJig/blob/master/options.py)
while {{ site.codename }} is running, the options will not take effect until you quit
and restart {{ site.codename }}.

[Return to index](#page-index)

<a name="needed-improvements"></a>

Needed Improvements
===================

I am looking for help to make the improvements outlined in this section.  I
will certainly give credit to those who help make these or any other
improvements!  If you\'re thinking of contributing, let me know, because I may
have already started on some of these.

* <b>Windows and Linux Support.</b>  If you can help test and improve {{ site.codename }} on
any platform, particularly Windows and Linux, please contact me.  Ideally, you
know Python and can send me proposed patches (or pull requests on Github).
* <b>Known Bugs.</b>
  1. The redraw after changing a parameter does not resize the graphics in the
  same manner as resizing the window with your mouse.  In particular, if you
  can\'t see all of the graphics, try resizing your window.
* <b>Features.</b> I\'m working on the following features, but would appreciate help:
  * Cleaning up these web pages.
  * Define the option for \"fold-over templates\" that are appropriate for
    laying out hand-cut joints.  This would be an alternative option to the Incra template.
  * More friendly error messages and handling.
  * Get rid of the dependence on matplotlib and use PyQt drawing
    directly.
  * Allow one to print the joint directly, without having to save to a file
    first and open the file in another application that is able to print it.
    This is apparently a limitation of matplotlib.
  * More spacing options, such as an interactive GUI to allow manual
    adjustment of individual finger positions and widths.
  * Consider relaxing the requirement that board and bit dimensions be exact multiples
    of intervals.
  * Double-joint support.
  * Easier installation, for those who don\'t know anything about Python.
  * Move to Python version 3+.

[Return to index](#page-index)
