# A Byte of Python

## Installation

Ensure Python (&gt;= 2.7) is installed for compiling the sources. You
will need Python 3 to run the Python programs itself.

Install Pandoc >= 1.11.1 from <http://johnmacfarlane.net/pandoc/installing.html>

Install `pdflatex` from <http://www.tug.org/texlive/>.
Note that Mac users can install `MacTex.pkg` from <http://www.tug.org/mactex/2012/>.

Install `pip` if not present already:

    sudo sh -c "curl -k -O https://raw.github.com/pypa/pip/master/contrib/get-pip.py && python get-pip.py && rm get-pip.py"

Install Python libraries needed:

    sudo pip install -r requirements.txt

Convert the source files into HTML files:

    fab html

Convert the source files into PDF:

    fab pdf

Convert the source files into EPUB (ebook):

    fab epub

## Editing

If you're using Emacs, you must use
[Jason Blevins' Markdown Mode](http://jblevins.org/projects/markdown-mode/).

If you're using Vim, then you may like the
[vim-pandoc](https://github.com/vim-pandoc/vim-pandoc) plugin. There
is one downside though - for long chapters, it becomes really slow, so
I edit only in plain text mode (`:set ft=`), but when reviewing, I use
the `pandoc` (`:set ft=pandoc`) mode.
