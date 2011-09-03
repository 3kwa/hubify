Hubify
======

Quickly put together little tool to see what your reStructuredText_ would look
like once rendered on github_.

Installation
------------

Get the source::

    $ git clone https://github.com/3kwa/hubify.git

Install docutils::

    $ pip install docutils

Add ``hubify/bin`` to your PATH e.g. in your .bashrc::

    export PATH=~/Code/hubify/bin:$PATH

Usage
-----

Give ``hubify`` any reStructuredText_ file to process, it will return a html
document you can save and open in a browser::

    $ hubify README.rst > /tmp/README.html; open /tmp/README.html

.. _github: https://github.com
.. _reStructuredText: http://docutils.sourceforge.net/rst.html
