#!/usr/bin/env python
#
# Download images from imgur.com galleries Will download using xml
# (more flexible) or HTML scraping (a bit kludgy, but I had a few
# albums cut off early and suspect the API only delivers ~50 results
# from XML)
import sys
import xml.sax
import urllib
import re

class PostHandler(xml.sax.handler.ContentHandler):
    """
    SAX handler class to parse the imgur xml gallery document

    Simplified example input:
    <item><hash>eieio</hash><ext>.jpg</ext></item>
    """
    def __init__(self):
        self.inhash=0
        self.inext=0
        self.posts = []

    def startElement(self, name, attributes):
        if name == "item":
            self.filehash = ""
            self.fileext = ""
        if name == "hash":
            self.inhash=1
        if name == "ext":
            self.inext=1

    def characters(self, data):
        if self.inhash:
            self.filehash += data
        if self.inext:
            self.fileext += data

    def endElement(self, name):
        if name == "hash":
            self.inhash = 0
        if name == "ext":
            self.inext = 0
        if name == "item":
            self.posts.append([self.filehash, self.fileext])

def get_posts(album):
    """
    Grab a list of image hash names using the XML API
    """
    parser = xml.sax.make_parser()
    handler = PostHandler()
    parser.setContentHandler(handler)
    parser.parse("http://imgur.com/a/%s/all.xml" % album)
    return handler.posts

def get_images(album):
    """
    Scrape the 'noscript' HTML.  Supports larger galleries.
    """
    doc = urllib.urlopen("http://imgur.com/a/%s/noscript" % (album)).read()
    patt = re.compile('class="image" id="([^"]+)"')
    return [[hash, '.jpg'] for hash in patt.findall(doc)]

def make_url(filename):
    return "http://i.imgur.com/%s" % (filename)

def save_file(url, dest):
    try:
        content = urllib.urlopen(url)
        print "Saving %s to %s" % (url, dest)

        destination = open(dest, "w")
        destination.write(content.read())
        destination.close()

    except HTTPError as e:
            print("HTTP Error:",e.code , url)
    except URLError as e:
            print("URL Error:",e.reason , url)

if len(sys.argv) != 2:
    sys.stderr.write("Usage: imgurdl albumid\n")
    sys.exit(1)

album = sys.argv[1]

scraped_items = []
items = get_posts(album)

# I have seen albums with >50 items download successfully using the
# xml API, but have seen larger albums truncated to about 55 entries,
# even with "?count=100" set.  If >50 seen, try again with the HTML scraper
if items > 50:
    scraped_items = get_images(album)
    if len(scraped_items) < len(items):
        sys.stderr.write("Warning: HTML scraping failed\n")
    if len(scraped_items)>len(items):
        items = scraped_items
        sys.stderr.write("Warning: " +
                         "xml feed truncated.  Using HTML scraping.\n")
    
for i in range(len(items)):
    filename = "".join(items[i])
    save_file(make_url(filename), "%04d-%s" % (i,filename))
