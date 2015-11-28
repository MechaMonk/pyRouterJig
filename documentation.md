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
* [Editor](#editor)
* [Drop-Down Menus](#drop-down-menus)
* [Printing](#printing)
* [Intervals Explained](#intervals-explained)
* [Incra Template Details](#incra-template-details)
* [Options File](#options-file)
* [Needed Improvements](#needed-improvements)
* [Acknowledgments](#acknowledgments)

<a name="overview-of-features"></a>

Overview of Features
====================

When you start {{ site.codename }}, you should see something like the image
below (this image is from a Mac; on other platforms, the image may differ):

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
with the labels \"A\" and \"B\" on the boards of the joint.  Each finger is
labeled with its width, in intervals.  By default

* 1 interval = 1/32\" (English units)
* 1 interval = 1 mm (metric units)

See [Intervals Explained](#intervals-explained) section for more discussion on intervals.

Below the boards is the corresponding Incra template.  This template may be
cut out and used in an Incra LS Positioner.  Below the template is a concise
title that summarizes the properties of the joint.  A vertical dashed line
denotes the center of the boards.  The graphics containing the boards,
template, and title may be printed by selecting <b>Print</b> in the
<b>File</b> pull-down menu, or by pressing the key combination `Ctrl-P`
(`Command-P` on Mac).

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
pin or tail of a dovetail joint.  There are currently two automatic finger-spacing
algorithms, along with an editor to allow specification of arbitrary joints.
The automatic spacing options are <b>Equal</b> and <b>Variable</b>, located at
tabs in the lower-right portion of the window.  Each option has its own
controls, described below:

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

<a name="editor"></a>

Editor
======

The <b>Editor</b> tab allows you to edit each individual finger of the joint.
The starting joint for editing is whatever was last specified under either the
<b>Equal</b> or <b>Variable</b> spacing options.  Under the <b>Editor</b>, the board
and bit dimensions cannot be changed; make sure these are set to their final
values under under either the <b>Equal</b> or <b>Variable</b> before switching
to the <b>Editor</b>.

[Figure 7](#figure7) shows an example of entering the <b>Editor</b>, after setting up the
joint as in [Fig. 6](#figure6).  The active finger is highlighted in red and is the finger
which is to be edited, using either the buttons under the <b>Editor</b> tab,
or using keyboard shortcuts.  The active finger is always on Board-B. Because
any changes on Board-B are reflected on Board-A, there is no need to allow
editing of Board-A fingers.  The green vertical lines indicate the extents
that the active finger can be moved or widened, limited by the bit width.

<figure>
<a name="figure7"></a>
<img src="{{ site.baseurl }}/editor_screen_shot.png" alt="Editor example.">
<figcaption>
<b>Figure 7.</b>  Editor mode, following Variable spacing set up as in Fig. 6.
</figcaption>
</figure>

The buttons and shortcuts are as follows: 

* <b>Move:</b> (keyboard: left and right arrow keys) The arrows move the active finger 1 interval to the left or right, if possible.
* <b>Widen:</b> (keyboard: Hold `Shift` key, along with left and right arrow keys) Widens the active finger on its left or right side by 1 interval, if possible.
* <b>Trim:</b> (keyboard: Hold `Control` key, along with left or right arrows) Trim the active finger on its left or right side by 1 interval, if possible.
* <b>Select:</b>  (keyboard: Hold `Alt` key, along with left or right arrows) Selects the next
finger to the right or left to be the active finger.
* <b>Add:</b>  (keyboard: `+`) Adds a finger, if possible.  There needs to be
space enough to add a finger, given the board width and bit constraints.  The
finger is added in the first possible location found, searching from the
left side of the board.
* <b>Delete:</b>  (keyboard: `-`) Deletes the active finger.
* <b>Undo:</b>  (keyboard: `u`) Undo the last editing operation.  This key may
be pressed multiple times.

Note that if you make changes in the <b>Editor</b>, and then go back to either
<b>Equal</b> or <b>Variable</b> options, the changes will be lost.

[Return to index](#page-index)

<a name="drop-down-menus"></a>

Drop-Down Menus
===============

Drop-down menus are located at the top of the window.  There are three menus
available:

1. <b>File:</b>
* <b>Save (Ctrl-P)</b> Allows you to print the joint diagram (or save it to a file).
* <b>Screenshot (Ctrl-S)</b> Saves a screenshot of the window.
* <b>Quit (Ctrl-Q)</b> Quits {{ site.codename}}.  If you\'ve made any changes
to the joint and haven\'t saved it, then you\'ll be warned.
1. <b>Units:</b>
English and metric units are supported.  Note that
changing units may cause accuracy issues, as a result of rounding.  For example, changing from english
to metric units, and then changing back to english units, changes the
dimension `7 1/2"` to `7 9/16"`.
1. <b>Wood:</b>  This menu allows you to select the wood appearance of the boards.  Changes are
cosmetic only.
1. <b>Help:</b> Very limited, for now:
* <b>About (Ctrl-A)</b> Pops up a window showing the version and license.

On the Mac, for the keyboard shortcuts use the `Command` key rather than `Ctrl`.

[Return to index](#page-index)

<a name="printing"></a>

Printing
========

{{ site.codename }} prints through a preview screen.  Press the printer icon
at the upper-right of the preview screen to either select the printer, or to
print to a file.

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

* The Incra templates that come with the LS Positioner distinguish between
  Board-A and Board-B cuts using color.  To avoid requiring a color printer, 
  the Board-A router passes are placed on the
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
improvements.  In fact, thanks to 

If you\'re thinking of contributing, let me know, because I may
have already started on some of these.

* <b>Windows and Linux Support.</b>  If you can help test and improve {{ site.codename }} on
any platform, particularly Windows and Linux, please contact me.  Ideally, you
know Python and can send me proposed patches (or pull requests on Github).
* <b>Features.</b> I\'m working on the following features, but would appreciate help:
  * Cleaning up these web pages.
  * Define the option for \"fold-over templates\" that are appropriate for
    laying out hand-cut joints.  This would be an alternative option to the Incra template.
  * More friendly error messages and handling.
  * More spacing options.
  * Consider relaxing the requirement that board and bit dimensions be exact multiples
    of intervals.
  * Double-joint and double-double joint support.
  * Save joint to a file support.
  * Export to Sketchup, or a file that it can import.

[Return to index](#page-index)

<a name="acknowledgments"></a>

Acknowledgments
===============

Thanks to "PhilBa" at [routerforums.com](http://www.routerforums.com) for his
suggestions for improvement and testing help!

{{ site.codename }} depends upon and is extremely grateful for the following
open-source software efforts:

* [Python](http://www.python.org)
* [PyQt](http://sourceforge.net/projects/pyqt/)
* [PyInstaller](http://www.pyinstaller.org/)
* [Anaconda](https://www.continuum.io/)

[Return to index](#page-index)
