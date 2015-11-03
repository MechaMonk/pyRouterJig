---
layout: default
title: pyRouterJig Installation
---


Installation for Windows and Mac
================================

Pre-compiled binaries (thanks to [PyInstaller](http://www.pyinstaller.org/))
are available from the homepage for Windows and Mac.  For Windows, simply
download `pyRouterJig.exe` file, double-click on it, and the program should run.

For Mac, download the `pyRouterJig.app.zip` file.  Unzip this file by
double-clicking on it, which should create the folder `pyRouterJig.app`.
Double-clicking on this folder should start the application.

Installation from source
========================

This approach will likely be a challenge
unless you are familiar wit [Python](http://www.python.org), the language that
{{ site.codename }} uses.

{{ site.codename }} depends upon the following [Python](http://www.python.org)
packages, which must be installed in order to run {{ site.codename }}:

* [Python](http://www.python.org).  Python is installed by default on
  the Mac, but I use a different installation, discussed below.
* [PyQt4](http://pyqt.sourceforge.net).  This package is used as the
  graphical user interface (GUI).

I install all of these packages using [Anaconda](https://www.continuum.io/),
Which is also available for Windows, Mac, and Linux.  I highly recommend Anaconda,
as the packages above may have other dependencies that Anaconda also takes
care of installing.  Note that Anaconda may not install PyQt4 by default.  On
the Mac, you must enter the command

`conda install pyqt`

in a `Terminal.app` window.  If you don\'t have `conda` in your path, you must
do

`/anaconda/bin/conda install pyqt`

assuming that `/anaconda/bin` is where Anaconda was installed.  Another
required package is `future`, which is used so that {{ site.codename }} works
for both python 2.7 and 3.5 (these are the versions that I have tested;
versions inbetween should work also).  For Anaconda, simply do

`conda install future`

Another advantage of Anaconda is that you may install more than one version of Python.


Assuming that you satisfy the perquisites above and have
those files in your path, on any platform you should be able to type in a terminal

`./pyRouterJig.py`

and the application should start.
