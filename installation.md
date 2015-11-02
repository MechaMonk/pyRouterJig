---
layout: default
title: pyRouterJig Installation
---

Prerequisites
=============

At this stage of the project, {{ site.codename }} is likely not easily installed for someone
completely unfamiliar with getting [Python](http://www.python.org)
applications running on their particularly platform.  All I have access
to is a Mac running OSX 10.9.2, so I won\'t be much help debugging other
installations.

{{ site.codename }} depends upon the following [Python](http://www.python.org)
packages, which must be installed in order to run {{ site.codename }}:

* [Python](http://www.python.org).  Python is installed by default on
  the Mac, but I use a slightly different version, as I will discuss below.
* [PyQt4](http://pyqt.sourceforge.net).  This package is used as the
  graphical user interface (GUI).

I install all of these packages using [Anaconda](https://www.continuum.io/),
which is also available for Windows, Mac, and Linux.  I highly recommend Anaconda,
as the packages above may have other dependencies that Anaconda also takes
care of installing.  Note that Anaconda does not install PyQt4 by default.  On
the Mac, you must enter the command

`conda install pyqt`

in a `Terminal.app` window.  If you don\'t have `conda` in your path, you must
do

`/anaconda/bin/conda install pyqt`

assuming that `/anaconda/bin` is where Anaconda was installed.


Installation
============

After unzipping (or untarring) the download file, locate the file named
`pyRouterJig`.  Assuming that you satisfy the Perquisites above and have
those files in your path, on Mac and Linux you should be able to type in a terminal

`./pyRouterJig.py`

and the application should start.  On Windows, I don\'t know how to run python
scripts, and this documentation will be updated once I receive that feedback.



