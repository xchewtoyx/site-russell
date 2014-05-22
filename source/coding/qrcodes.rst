Generating QR Codes using the Google Chart API
==============================================

Simple info on using the google charts API to create QRCode images (as
described in `this blog post`_).

.. _this blog post: http://google-code-updates.blogspot.com/2008/07/qr-codes-now-available-on-google-chart.html

Example:

.. image:: http://chart.apis.google.com/chart?cht=qr&chs=100x100&chl=http://perlmonkey.blogspot.com/

http://chart.apis.google.com/chart?cht=qr&chs=100x100&chl=http://perlmonkey.blogspot.com/

You can also embed information in VCARD format by URL encoding the VCARD into the chl field:

.. code::

   BEGIN:VCARD
   VERSION:2.1
   N:Heilling;Russell
   FN:Russell Heilling
   TITLE:Packet Wrangler
   TEL;CELL:+447538287157
   EMAIL:russell@heilling.net
   URL:http://perlmonkey.blogspot.com/
   END:VCARD

This VCARD produces the QR code below:


.. image:: http://chart.apis.google.com/chart?cht=qr&chs=150x150&chl=BEGIN:VCARD%0d%0aVERSION:2.1%0d%0aN:Heilling;Russell%0d%0aFN:Russell%20Heilling%0d%0aTITLE:Packet%20Wrangler%0d%0aTEL;CELL:%2b447538287157%0d%0aEMAIL:russell@heilling.net%0d%0aURL:http://perlmonkey.blogspot.com/%0d%0aEND:VCARD

http://chart.apis.google.com/chart?cht=qr&chs=150x150&chl=BEGIN:VCARD%0d%0aVERSION:2.1%0d%0aN:Heilling;Russell%0d%0aFN:Russell%20Heilling%0d%0aTITLE:Packet%20Wrangler%0d%0aTEL;CELL:%2b447538287157%0d%0aEMAIL:russell@heilling.net%0d%0aURL:http://perlmonkey.blogspot.com/%0d%0aEND:VCARD
