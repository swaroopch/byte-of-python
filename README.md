
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
