#!/usr/bin/env python

"""
take a HTML document as a string (e.g. output of rst2html) and modify it so
it renders like github would.

rst2hml.py README.rst | ./hubify.py > README.html; open README.html
"""

import sys
import os
import re
from xml.etree.cElementTree import ElementTree, fromstring, tostring


def get_namespace(element):
    """ extract the URI (namespace) of element """
    return str.split(element.tag, '}', 1)[0] + '}'

def process(source):
    """ modify the DOM tree so the github css can be applied as is """

    root = fromstring(source)
    uri = get_namespace(root)

    # github css
    style = root.find(".//%sstyle" % uri)
    css = os.path.normpath(os.path.join(os.path.dirname(sys.argv[0]),'github.css'))
    with open(css) as f:
        style.text = f.read().decode('utf-8')

    # add wikstyle to body and set width and padding for readabilty
    body = root.find("%sbody" % uri)
    body.set('class', 'wikistyle')
    body.set('style', 'width:920px; padding:20px')

    # replace the h1 tags with h2 (not the first)
    for element in body.findall(".//%sh1" % uri)[1:]:
        element.tag = 'h2'

    # substitute html: prefix in tags with nothing (brittle)
    print re.sub('html:', '', tostring(root, encoding='utf-8', method='html'))

if __name__ == '__main__':
    # sys.stdin is a file like object containing what is "piped"
    source = sys.stdin.read()
    process(source)
