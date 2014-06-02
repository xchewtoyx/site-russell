Quick-n-Dirty Scripts
=====================

depoch
------

A simple script that takes input from files or stdin, matches a
timestamp in unix epoch format and rewrites it into a human readable
format before sending it to stdout.  Handy for interpreting log files
which use epoch timestamps.

https://github.com/xchewtoyx/depoch

histogram
---------

matches values based on a pattern in an input stream and produces a
histgram of the values for quick distribution analysis.

http://github.com/xchewtoyx/histogram

imgurdl
-------

For reasons to boring to go into, I needed a script to grab the images from an
imgur.com gallery.  Imgur is a great resource for quick picture posting, used a
lot by Reddit users.  The images may not be around for long though.  This
script will grab the photos from a gallery, given the short hash used as the
gallery id, and save the files locally, prepending a sequence number onto the
files to preserve ordering.  File attached as :download:`imgurdl.py`.  Enjoy.

swtagger
--------

I have quite a large collection of photos I have taken over the past few years
and I have them organised on the hard disk in a way that there is actually
quite a bit of useful meta-data in the directory structure.  After importing
this library into the Gnome photo manager Shotwell I found that the UI doesn't
allow for much in the way of filtering by filesystem hierarchy.  In order to
save some time with re-tagging all my photos, I knocked together a quick Python
script that can be used to add tags and events to Shotwell images based on
regular expression matches against the full path to the file.   I have shoved
the code up at github under an MIT license.

https://github.com/xchewtoyx/swtagger

xmlback
-------

GNOME 3 supports xml background files to define a slideshow rather than a
single background image, but it provides neither the tools to create the file
or the means to select one via the GUI (actually I have found that Shotwell
does include this)  I knocked together a quick tool for generating the xml flie
to rotate through the images in a specific directory.  Github + MIT again

https://github.com/xchewtoyx/chewtoy-xmlback
