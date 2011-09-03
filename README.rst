Hubify rst to github html in a tick
===================================

Quickly put together little tool to see what your reStructuredText_ would look
like once rendered on github_.

Install docutils::

    $ pip install docutils

Add hubify/bin to your PATH e.g. in your .bashrc::

    export PATH=~/Code/hubify/bin:$PATH

Then give ``hubify`` any reStructuredText_ file to process, it will return a html
document you can save and open in a browser::

    $ hubify README.rst > README.html; open README.html

.. _github: https://github.com
.. _reStructuredText: http://docutils.sourceforge.net/rst.html
