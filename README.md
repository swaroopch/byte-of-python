
## Installation

Install Pandoc from <http://johnmacfarlane.net/pandoc/installing.html>


Install `pip` if not present already:
    
    sudo sh -c "curl -k -O https://raw.github.com/pypa/pip/master/contrib/get-pip.py && python get-pip.py && rm get-pip.py"


Install Python libraries needed:

    sudo pip install -r requirements.txt


Convert the source files into HTML files:

    fab html
