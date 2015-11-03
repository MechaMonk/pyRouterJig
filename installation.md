---
layout: default
title: pyRouterJig Installation
---


Installation for Windows and Mac
================================

Pre-compiled binaries for Windows and Mac (thanks to
[PyInstaller](http://www.pyinstaller.org/)) are available on the 
[home page](http://lowrie.github.io/pyRouterJig/).  For Windows, simply download the
`pyRouterJig.exe` file, double-click on it, and the program should run.

For Mac, download the `pyRouterJig.app.zip` file.  Unzip this file by
double-clicking on it, which should create the folder `pyRouterJig.app`.
Double-clicking on this folder should start the application.

Installation from source
========================

This approach will likely be a challenge unless you are familiar working with
[Python](http://www.python.org), the language that {{ site.codename }} uses.
To obtain the source code for a release, go to the [github release
site](https://github.com/lowrie/pyRouterJig/releases), download either the
`.zip` or `.tar.gz` file (your preference), and decompress the file.  This
should create a folder `pyRouterJig-vX.X.X`, where `X.X.X` is the release
number.  In this folder, the script `pyRouterJig.py` should start the
application, if you happen to satisfy the prerequisites below.

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

in a `Terminal.app` window and `conda` is in your path.  Another required
package is [Python-Future](http://python-future.org/overview.html), which is
used so that {{ site.codename }} works for both python 2.7 and 3.5 (these are
the versions that I have tested; intermediate versions should work also).  For
Anaconda, use the command

`conda install future`

Another advantage of Anaconda is that you may install more than one version of Python.

With the prerequisites above satisfies, and `python` or `python.exe` in your
path, in the source folder on any platform you should be able to type in a terminal

`./pyRouterJig.py`

or on Windows

`.\pyRouterJig.py`

and the application should start.
