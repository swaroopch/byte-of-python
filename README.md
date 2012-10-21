
## Installation

Ensure Python (&gt;= 2.7) is installed.

Install Pandoc from <http://johnmacfarlane.net/pandoc/installing.html>

Install `pdflatex` from <http://www.tug.org/texlive/>.
Note that Mac users can install `MacTex.pkg` from <http://www.tug.org/mactex/2012/>.

Install `pip` if not present already:

    sudo sh -c "curl -k -O https://raw.github.com/pypa/pip/master/contrib/get-pip.py && python get-pip.py && rm get-pip.py"


Install Python libraries needed:

    sudo pip install -r requirements.txt


Convert the source files into HTML files:

    fab html

## Editing

If you're using Vim editor, then you may like the [vim-pandoc](https://github.com/vim-pandoc/vim-pandoc) plugin. There is one downside though - for long chapters, it becomes really slow, so I edit only in plain text mode (`:set ft=`), but when reviewing, I use the `pandoc` (`:set ft=pandoc`) mode.

If you're using [Sublime Text](http://www.sublimetext.com/) editor, you may find the following plugins useful:

- [Sublime Package Control](http://wbond.net/sublime_packages/package_control/installation)
- [Pandoc Academic](https://github.com/larlequin/PandocAcademic)
- [Table Editor](https://github.com/vkocubinsky/SublimeTableEditor)
