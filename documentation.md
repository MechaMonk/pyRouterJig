---
layout: default
title: pyRouterJig Documentation
---

Note that {{ site.codename }} is in its early development stage.  Many bugs likely
still exist.  If you contact me, I\'ll try to help, but please keep in mind that I
also have a day job.

<a name="page-index"></a>

This page is split into the following sections ("Return to index" link at the
bottom of each section returns to this location):

* [Overview of Features](#overview-of-features)
* [Wood Pattern Selection](#wood-pattern)
* [Finger Spacing Options](#finger-spacing-options)
* [Editor](#editor)
* [Double and Double-Double Joints](#double)
* [Drop-Down Menus](#drop-down-menus)
* [Increments Explained](#increments-explained)
* [Incra Template Details](#incra-template-details)
* [Configuration File](#configuration-file)
* [Needed Improvements](#needed-improvements)
* [Acknowledgments](#acknowledgments)

<a name="overview-of-features"></a>

Overview of Features
====================

When you start {{ site.codename }}, you should see something like the image
below (this image is from a Mac; on other platforms, the image may differ):

<figure>
<a name="figure1"></a>
<img src="{{ site.baseurl }}/opening_screen_shot.png" alt="Opening screenshot">
<figcaption>
<b>Figure 1.</b>  Opening screenshot. The screenshot doesn't show the
mouse pointer, which is located over the <b>Bit Width</b> input box so that its tooltip appears.
</figcaption>
</figure>

The default joint is a box joint, with the fingers equally spaced, over a
width of 7 1/2\".  The upper portion of the window draws the current joint.
Each finger is labeled with its width, in increments.  By default

* 1 increment = 1/32\" (English units)
* 1 increment = 1 mm (metric units)

See [Increments Explained](#increments-explained) section for more discussion on increments.

Below the boards is the corresponding Incra template.  This template may be
cut out and used in an Incra LS Positioner.  Below the template is a concise
title that summarizes the properties of the joint.  A vertical dashed line
denotes the center of the boards.  The graphics containing the boards,
template, and title may be printed by selecting <b>Print</b> in the
<b>File</b> pull-down menu, or by pressing the key combination `Ctrl-P`
(`Command-P` on Mac).

The lower part of the window allows you to interactively change the parameters
for the joint.  The joint is re-drawn after each change.  At the lower left,
you can see two rows of input parameters, which are available for any
finger-spacing algorithm.  On the top row, we have

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

Also shown in [Figure 1](#figure1) is a \"tooltip\", which is a small window that appears when
you hover the mouse over an available parameter.  In this case, the mouse
is hovering above the <b>Bit Width</b> parameter.  All of the inputs have
tooltips which give a short explaination of the parameter or option.

To create a dovetail joint, change <b>Bit Angle</b> to 7 degrees, and we obtain the
dovetail joint shown in [Figure 2](#figure2) below:

<figure>
<a name="figure2"></a>
<img src="{{ site.baseurl }}/images/dovetail_screen_shot.png" alt="Dovetail
example.">
<figcaption>
<b>Figure 2.</b>  Dovetail example.  Compared to Fig. 1, the <b>Bit Angle</b>
has been changed to 7 degrees.
</figcaption>
</figure>

[Return to index](#page-index)

<a name="wood-pattern"></a>

Wood Pattern Selection
======================

On the bottom row of the lower-left input parameters are <b>Top Board</b>,
<b>Bottom Board</b>, <b>Double Board</b>, and <b>Double-Double Board</b>,
which allow you to select the pattern or wood images used to draw these
boards, along with parameters for Double and Double-Double joints.  The Double
and Double-Double joints are explained in the section [Double and
Double-Double Joints](#double).  In this section, we cover how to specify
patterns for any board and how to add image files to simulate
the appearance of wood grain.

The patterns for Boards may be selected under each respective board header
(Top, Bottom, Double, and Double-Double).  By default, {{ site.codename }}
uses simple patterns to draw the board, such as the default `DiagCrossPattern`
shown in the figures above.  You may also specify any image file (such as a
Portable Network Graphics - PNG) to draw the board.  At startup, 
{{ site.codename }} looks in the `wood_images` folder in your home directory
and assumes any file in this folder is an image file.  It then makes these
images available to draw any of the boards.

A starting `wood_images` can be downloaded [from this link]({{ site.baseurl }}/wood_images.zip).
Unzip this file in your home directory and you should be
ready to go.  As an example, the file `hard-maple.png` is in this `wood_images` folder.
Using this image for the Top and Bottom Boards in [Figure 1](#figure1)
displays [Figure 3](#figure3).
Other good wood image files can be obtained from [the wood database
website](http://www.wood-database.com/).

<figure>
<a name="figure3"></a>
<img src="{{ site.baseurl }}/images/woods_screen_shot.png" alt="Wood image example.">
<figcaption>
<b>Figure 3.</b>  Same as Figure 1, but using a "hard-maple" image file for
the Top and Bottom Boards.
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

  1. <b>Spacing:</b> This slider allows you to specify additional spacing between
    the A-cuts.  [Figure 4](#figure4) shows an example of increasing this parameter.
  2. <b>Width:</b> This slider allows you to specify additional width added
    to the A-cuts.
    [Figure 5](#figure5) shows an example of increasing this parameter.
  3. <b>Centered:</b> This input is only available for straight bits (bit
    angle = 0).  If this box is checked, a finger is always centered on
    the board.  Otherwise, a full finger is started on the left edge, which
    will result in a centered finger only if the finger width divides into the
    board width an odd number of times.
    [Figure 6](#figure6) shows an example of a non-centered pattern.

  The sliders can be moved by using either dragging the mouse, or my clicking on the
  slider and using the left and right arrow keys for small changes and Page Up
  and Page Down for large changes.

* <b>Variable:</b> In this case a large finger is centered on the board,
  and the fingers decrease in size proportional to the distance to the center.
  There is one input that affects this algorithm:

  1. <b>Fingers:</b> Specifies the approximate number of
    fingers.  At its minimum value, the width of the center finger is maximized. At
    its maximum value, the width of the center finger is minimized, and the result is
    the same as equally-spaced with zero \"Spacing\", zero \"Width\", and
    the \"Centered\" option checked.

[Figure 7](#figure7) shows an example of a Variable-spaced box joint.

<figure>
<a name="figure4"></a>
<img src="{{ site.baseurl }}/images/bspacing_screen_shot.png" alt="Spacing example">
<figcaption>
<b>Figure 4.</b>  Effect of Spacing option.  Compared to Fig. 1, the <b>Spacing</b>
slider been moved to a value of 1 17/32".
</figcaption>
</figure>

<figure>
<a name="figure5"></a>
<img src="{{ site.baseurl }}/images/width_screen_shot.png" alt="Width example.">
<figcaption>
<b>Figure 5.</b>  Effect of Width option.  Compared to Fig. 1, the <b>Width</b>
slider been moved to a value of 27/32".
</figcaption>
</figure>

<figure>
<a name="figure6"></a>
<img src="{{ site.baseurl }}/images/centered_screen_shot.png" alt="Centered example.">
<figcaption>
<b>Figure 6.</b>  Effect of Centered option.  Compared to Fig. 1, the <b>Board
Width</b> has been changed to 7" and the <b>Centered</b> option unclicked.
</figcaption>
</figure>

<figure>
<a name="figure7"></a>
<img src="{{ site.baseurl }}/images/variable_screen_shot.png" alt="Variable spacing example.">
<figcaption>
<b>Figure 7.</b>  Variable spacing option.  Compared to Fig. 1, the
<b>Variable</b> tab has been clicked and the <b>Fingers</b> input has a
value of 5.
</figcaption>
</figure>

[Return to index](#page-index)

<a name="editor"></a>

Editor
======

The <b>Editor</b> tab allows you to edit each individual cut of the joint.
The editor operates on the A-cuts of the Top Board; all of the other cuts
(B, C, D, etc.) follow from the A-cuts.  The starting joint for editing is
whatever was last specified under either the <b>Equal</b> or <b>Variable</b>
spacing options.  Under the <b>Editor</b>, the board and bit dimensions, the
Double and Double-Double parameters, cannot be changed; make sure these are
set to their final values under under either the <b>Equal</b> or
<b>Variable</b> before switching to the <b>Editor</b>.

[Figure 8](#figure8) shows an example of entering the <b>Editor</b>, after
setting up the joint as in [Fig. 7](#figure7).  An active cut is highlighted
in red and is the cut which is to be edited, using either the buttons under
the <b>Editor</b> tab, or using keyboard shortcuts.  Again, active cuts are
always on the A-cuts of the Top Board.  The blue outline on a cut indicates
the cut cursor.  The cursor is used to select active cuts.  More than one cut
may be active.  The green vertical lines indicate the extents that the active
cuts can be moved or widened, limited by the bit width.

<figure>
<a name="figure8"></a>
<img src="{{ site.baseurl }}/images/editor_screen_shot.png" alt="Editor example.">
<figcaption>
<b>Figure 8.</b>  Editor mode, following Variable spacing set up as in Fig. 7.
The first three cuts on the Top Board are active, with the cut cursor on the
center cut.
</figcaption>
</figure>

The Editor functionality is grouped into two main categories, with buttons (or
corresponding keyboard shortcuts) controlling the actions taken.  
The buttons and shortcuts are as follows: 

* <b>Active Cut Select</b>:  This category allows you to select which
  cuts are active.  Active cuts are those for which the <b>Active Cut
  Operators</b> will be applied, described below.
   The buttons for this category are as follows:
  * The arrow buttons (keyboard:  left or right arrows) control the position
  of the cut cursor, shown with a blue outline.  
  * <b>Toggle:</b> (keyboard: `Return`) Toggle the cut at the cursor as active and deactive.
    When active, the cut is highlighted in red.
  * <b>All:</b> (keyboard: `a`) All cuts are set as active.
  * <b>None:</b> (keyboard: `n`) All cuts are set as inactive.
* <b>Active Cut Operators</b>: This category applies editing operators to
  the active cuts, and its buttons are as follows:
  * <b>Move:</b> (keyboard: Hold `Alt` key, along with left and right arrow keys) The arrows move the active cuts 1 increment to the left or right, if possible.
  * <b>Widen:</b> (keyboard: Hold `Shift` key, along with left and right arrow keys) Widens the active cuts on their left or right side by 1 increment, if possible.
  * <b>Trim:</b> (keyboard: Hold `Control` key, along with left or right arrows) Trims the active cuts on their left or right side by 1 increment, if possible.
  * Moves the cut cursor to the right or left
  cut to the right or left to be the active cut.
  * <b>Add:</b>  (keyboard: `+`) Adds one cut, if possible.  There needs to be
    space enough to add a cut, given the board width and bit constraints.  The
    cut is added in the first possible location found, searching from the
    left side of the board.
  * <b>Delete:</b>  (keyboard: `-`) Deletes the active cut.

Finally, the <b>Undo</b> button  (keyboard: `u`) reverses the last editing
operation.  Undo may be applied repeatedly, until the joint is back to the
starting point of invoking the <b>Editor</b>.

Note that if you make changes in the <b>Editor</b>, and then go back to either
<b>Equal</b> or <b>Variable</b> options, the changes will be lost.

[Return to index](#page-index)

<a name="double"></a>

Double and Double-Double Joints
===============================

A Double joint is created simply by selecting a wood pattern other than `NONE`
under <b>Double Board</b>.  Its <b>Thickness</b> may also be changed from
its default of 1/8", similar to parameters such as <b>Board Width</b>.
[Figure 9](#figure9) is an example of a Double joint.

<figure>
<a name="figure9"></a>
<img src="{{ site.baseurl }}images/double_screen_shot.png" alt="Double joint example.">
<figcaption>
<b>Figure 9.</b>  Example of a Double joint, following the Equal spacing set up as in Fig. 1.
</figcaption>
</figure>

Once a Double joint has been specified, you can make it a Double-Double joint
by selecting a wood pattern other than `NONE` under <b>Double-Double Board</b>.
[Figure 10](#figure10) is an example of a Double-Double joint.  In this case,
there are two templates which must be aligned in two slots in the Incra LS
Positioner at the dashed line labeled `ALIGN`.  The alignment line is not
always in the same position on the template; its position is placed to minimize
interference with cut lines on the templates.

<figure>
<a name="figure10"></a>
<img src="{{ site.baseurl }}/images/dd_screen_shot.png" alt="Double-double joint example.">
<figcaption>
<b>Figure 10.</b>  Example of a Double-Double joint, following the the set up as in Fig. 9.
</figcaption>
</figure>

[Return to index](#page-index)

<a name="drop-down-menus"></a>

Drop-Down Menus
===============

Drop-down menus are located at the top of the window.  There are three menus
available:

1. <b>File:</b>
* <b>Open (Ctrl-O)</b> Opens a previously saved or screenshot file (see
<b>Save</b> and <b>Screenshot</b>).
{{ site.codename }} embeds the joint data in the `PNG` image files that it
saves.  Opening the `PNG` file will allow you to start work again where you
left off.  Note that in the <b>Editor</b> mode, the Undo history is
not saved.   Any of the images in this documentation page may be opened with
{{ site.codename }}.  For the wood images described in [Wood Pattern
Selection](#wood-pattern), only the name of the wood image is saved.  So
if the image uses wood images, such as the `hard-maple` and `black-walnut` in
[Figure 9](#figure9),  if you don't have these images available
in your own `wood_images` folder, then a simple pattern is substituted.
* <b>Save (Ctrl-S)</b> Saves the joint figure as a `PNG` file.  By
default, the image files are placed in your home directory, numbered sequentially as
`pyrouterjig_0.png`, `pyrouterjig_1.png`, `pyrouterjig_2.png`, and so on.  The
image size is the same as your current window size, but no smaller than
`min_image_size`, which is set in the [configuration
file](#configuration-file).  By default, `min_image_size = 2048`.
[Figure 11](#figure11) shows the saved image corresponding to [Figure 10](#figure10).
* <b>Screenshot (Ctrl-W)</b> Similar to <b>Save</b>, but includes the entire
{{ site.codename }} application window.  The image size is the same as your
current window size.  Figures 1 through 10 were created with
<b>Screenshot</b>.  Screenshots always use the default filename for output and
are meant to be used to quickly generate image files (such as for this documentation!).
* <b>Print (Ctrl-P)</b> Allows you to print the joint diagram (including print
to a file). {{ site.codename }} prints through a preview screen.  Press the printer icon
at the upper-right of the preview screen to either select the printer, or to
print to a file.
* <b>Quit (Ctrl-Q)</b> Quits {{ site.codename}}.  If you\'ve made any changes
to the joint and haven\'t saved it, then you\'ll be warned.
1. <b>Units:</b>
English and metric units are supported.  Note that
changing units may cause accuracy issues, as a result of rounding.  For example, changing from English
to metric units, and then changing back to English units, changes the
dimension `7 1/2"` to `7 9/16"`.
1. <b>View:</b>
* <b>Fullscreen (Ctrl-F)</b> Toggles full-screen mode.
* <b>Caul Template</b> Toggles the caul template.  The caul template is an
additional Incra template that can be used to create clamping cauls for the
joint with the LS Positioner.  It's assumed that a straight router bit of the
same width is used to create the cauls.  The template follows the same pattern as that for the
Top and Bottom Boards, but with narrower fingers.  By default, 1
increment is removed from the side of each finger. [Figure 12](#figure12)
shows an example of the caul template.
1. <b>Help:</b>
* <b>About (Ctrl-A)</b> Pops up a window showing the version and license.
* <b>Documentation</b> Opens your default browser and goes to the
documentation page you are now reading.  You must have an Internet connection for
this operation to work.

On the Mac, for the keyboard shortcuts use the `Command` key rather than `Ctrl`.

<figure>
<a name="figure11"></a>
<img src="{{ site.baseurl }}/images/dd_fig.png" alt="Save option figure.">
<figcaption>
<b>Figure 11.</b> The same as Figure 10, but using <b>Save</b> rather than
<b>Screenshot</b> to create the image file.
</figcaption>
</figure>

<figure>
<a name="figure12"></a>
<img src="{{ site.baseurl }}/images/caul_screen_shot.png" alt="Example of Caul Template.">
<figcaption>
<b>Figure 12.</b> The same as Figure 1, but after toggling <b>Caul
Template</b> under the <b>View</b> menu.  The A-cuts on the Cauls template
will create a clamping caul for the Top Board, while the B-cuts create a
clamping caul for teh Bottom Board.
</figcaption>
</figure>

[Return to index](#page-index)

<a name="increments-explained"></a>

Increments Explained
====================

{{ site.codename }} does all of its computations in terms of what we refer
to as \"increments.\"  By default,

* 1 increment = 1/32\" (English units)
* 1 increment = 1 mm (metric units)

An increment is the resolution of {{ site.codename }}.  All dimensions used by
{{ site.codename }}, such as the router-bit width, are rounded to the nearest number
of increments.  The reason for the default choices above is that these are the
resolutions of the respective [Incra LS Positioner
fence](http://www.incra.com/router_table_fences-ls_positiners.html).  By using
increments, we ensure that it\'s possible to position the fence at the exact
location desired.  More generally, using increments (or \"integer arithmetic\")
means that {{ site.codename }} does not need to be worried about floating-point
errors.

[Return to index](#page-index)

<a name="incra-template-details"></a>

Incra Template Details
======================

As mentioned above, the Incra template may be cut out and used in a Incra LS
Positioner fence.  Referring to any of the figures above, the template needs
some explanation:

* The router passes are labeled with their ordering and the edge letter (A, B,
  C, etc.).
* The gray regions are margins for the template, outside the board\'s width.
  It\'s possible for a pass to be placed in the gray region, if the outer
  fingers are narrower than half of the <b>Bit Width</b>.
* On any one router pass, a good rule of thumb is not to cut deeper than the
  <b>Bit Width</b>.  So for example, for a <b>Bit Width</b> of 1/2" and a
  <b>Bit Depth</b> of 3/4", it's best to run the board through twice, the
  first pass with the depth set at 3/8", and the second pass at 3/4".  This
  rule of thumb may vary with the particular wood species, the sharpness of your
  bit, minimizing tear-out, and other variables.
* Of course, it\'s critical that your printer not distort the template when
  printing the template on paper.  I have a cheap inkjet printer that
  consistently distorts the template about 1/32" over 4".  This is well
  outside the accuracy of an Incra fence.  Fortunately, a friend\'s laser printer
  is very accurate.  After printing, make sure you check the dimensions of the template.

[Return to index](#page-index)

<a name="configuration-file"></a>

Configuration File
==================

The configuration file `.pyrouterjig` is created in the user's home directory
when {{ site.codename }} is first executed.  This file contains advanced
options, each described within the file itself.  {{ site.codename }} is still
under very active development.  Consequently, in a future release, the options
may change, be deleted, or be made available in a more user-friendly manner.
Setting these options requires a basic knowledge of Python.  If you change the
configuration file while {{ site.codename }} is running, the options will not
take effect until you quit and restart {{ site.codename }}.

[Return to index](#page-index)

<a name="needed-improvements"></a>

Needed Improvements
===================

I am looking for help to make the improvements outlined in this section.  I
will certainly give credit to those who help make these or any other
improvements.

If you\'re thinking of contributing, let me know, because I may
have already started on some of these.

* <b>Windows and Linux Support.</b>  If you can help test and improve {{ site.codename }} on
any platform, particularly Windows and Linux, please contact me.  Ideally, you
know Python and can send me proposed patches (or pull requests on Github).
* <b>Features.</b> I\'m working on the following features, but would appreciate help:
  * In Editor, allow for certain changes in parameters, such as board width
  and bit width.  The reason changes are disabled now is that parameter changes
  may create errors that are difficult to recover from.
  * Define the option for \"fold-over templates\" that are appropriate for
    laying out hand-cut joints.  This would be an alternative option to the Incra template.
  * More friendly error messages and handling.
  * More spacing options.
  * Cleaning up these web pages. Create a webpage with more example joints.
  * Consider relaxing the requirement that board and bit dimensions be exact multiples
    of increments.
  * Export to Sketchup, or a file that it can import.

[Return to index](#page-index)

<a name="acknowledgments"></a>

Acknowledgments
===============

Thanks to "PhilBa" at [routerforums.com](http://www.routerforums.com) for his
numerous suggestions for improvement and testing help! I'm always amazed at
the bugs he finds.  Among many great ideas, in particular he should be
credited with the ideas of storing the joint metadata in the `PNG` file and
the clamping caul template

{{ site.codename }} depends upon and is extremely grateful for the following
open-source software efforts:

* [Python](http://www.python.org)
* [PyQt](http://sourceforge.net/projects/pyqt/)
* [PyInstaller](http://www.pyinstaller.org/)
* [Anaconda](https://www.continuum.io/)

[Return to index](#page-index)
