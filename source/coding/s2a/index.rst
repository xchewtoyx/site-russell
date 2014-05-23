sphinx2appengine framework
==========================

sphinx2appengine is a base application I coded to scratch my own itch which
takes a collection of `ReST`_ files, builds a website from them using `Sphinx`_
and finally pushes it all up to appengine to be served.

I have put it up as a `GitHub project`_, both so I can keep the versions
deployed on my two instances straight, and so that it is there in case anyone
else wants to use it.

.. _rest: http://sphinx-doc.org/rest.html

.. _sphinx: http://sphinx-doc.org/

Configuration
-------------

The config isn't particularly modular of well documented.

The file layout is::

   Makefile     - Defines make shorcuts for deployment
   README.md    - Some simple instructions
   appengine    - Contains the stuff to be deployed to appengine
   build        - The sphinx output
   source       - This is where the documents go
   tools        - Helper scripts

Under ``appengine``::

   app.yaml     - The appengine application config
   json         - link to the json output from sphinx
   sitemap.pkl  - Used by the app to build an xml sitemap
                  generated with "make sitemap"
   sphinx.py    - The application that takes requests and delivers
                  the relevant web pages.
   static       - Static content for the site
   templates    - The templates used for rendering the pages

Under ``appengine/static``::

   favicon.ico  - replace this with your favicon
   logo.png     - likewise with your logo for the sidebar
   pygments.css - styles for syntax highlighting of code blocks
   robots.txt   - If you want to restrict access for crawlers
   site.css     - Update with local styling
   site.js      - Mostly used to add bootstrap components

Under ``appengine/templates``::

   sitemap.xml  - Used for rendering the xml sitemap
   sphinx.html  - A parent template which can be inherited from
                  for styling the site
   site.html    - Local overrides for content blocks.

To get it up and running you will need to edit::

   Makefile           - Make sure the base URL matches your site
   appengine/app.yaml - Add your application id
   site.html          - Any local style overrides

In addition to this you will need to populate the ``source`` directory
with your content (natch).

Once this is done you can use the following make shortcuts:

::

   make json

Rebuild modified site content.

::

   make json-all

Rebuild all site content

::

   make sitemap

Build the pickle file that the app uses to populate the xml sitemap.
This information is in the environment.pickle file produced by sphinx
but that file can only be unpickled if the sphinx module is available
so by splitting it out it removes any need to install sphinx on the
appengine side.

::

   make appserver

Fire up the development appserver for local testing (this will
automatically make the json and sitemap targets using dependencies)

::

   make deploy

Push your app into production. (this will automatically make the json and
sitemap targets using dependencies)

Contributing
------------

I am more than happy to accept pull requests over on the `GitHub project`_

Users
-----

* http://russell.heilling.net
* http://www.s8n.net

.. _github project: http://github.com/xchewtoyx/sphinx2appengine
