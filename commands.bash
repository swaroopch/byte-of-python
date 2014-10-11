#!/usr/bin/env bash

## References:
## http://asciidoctor.org/docs/asciidoc-writers-guide/

SLUG="byte_of_python"
FOPUB="$HOME/code/asciidoctor/asciidoctor-fopub/fopub"

function doctor() {
    backend=$1
    shift

    asciidoctor -n -a 'source-highlighter=pygments' -b $backend ${SLUG}.asciidoc
}

function make_html () {
    doctor html5
    ls -lh "$PWD/$SLUG.html"
}

function make_pdf () {
    doctor docbook
    $FOPUB ${SLUG}.xml
    # OR
    # a2x -f pdf --fop ${SLUG}.asciidoc
    ls -lh "$PWD/$SLUG.pdf"
}

# TODO Syntax highlighting in output
#   - http://docbook.sourceforge.net/release/xsl/current/doc/fo/highlight.source.html
#      - ~/code/asciidoctor/asciidoctor-fopub/src/dist/docbook-xsl/xslthl-config.xml
#   - http://www.vogella.com/tutorials/DocBook/article.html#advanced_syntaxhighlighting
function make_epub () {
    doctor docbook
    dbtoepub ${SLUG}.xml
    # OR
    # a2x -f epub ${SLUG}.xml
    epubcheck "$PWD/$SLUG.epub"
    ls -lh "$PWD/$SLUG.epub"
}

function make_mobi () {
    doctor html5
    kindlegen -verbose ${SLUG}.html -o ${SLUG}.mobi
    ls -lh "$PWD/$SLUG.mobi"
}

function install_deps_osx () {
    # http://brew.sh
    brew update
    brew install docbook docbook-xsl fop epubcheck git
    brew tap homebrew/binary
    brew install kindlegen
    # brew install asciidoc

    # http://s3tools.org/usage
    sudo pip install -U python-magic
    sudo pip install -U https://github.com/s3tools/s3cmd/archive/master.zip

    # http://asciidoctor.org/docs/install-asciidoctor-macosx/
    sudo gem update --system
    sudo gem install asciidoctor -N

    # https://groups.google.com/forum/#!topic/asciidoc/FC-eOwU8rYg
    echo >> ~/.bash_profile
    echo 'export XML_CATALOG_FILES="/usr/local/etc/xml/catalog"' >> ~/.bash_profile

    # https://github.com/asciidoctor/asciidoctor-fopub/blob/master/README.adoc
    mkdir -p $HOME/code/asciidoctor/
    cd $HOME/code/asciidoctor/
    git clone https://github.com/asciidoctor/asciidoctor-fopub
}


function s3_put () {
    filename=$1
    shift

    if [[ -f $filename ]]
    then
        s3cmd --verbose \
              --access_key=$AWS_ACCESS_KEY \
              --secret_key=$AWS_SECRET_KEY \
              --acl-public \
              put \
              "$filename" \
              "s3://files.swaroopch.com/python/$filename"
    fi
}


# https://en.wikipedia.org/wiki/Tput#Usage
function say () {
    echo "$(tput setaf 2)$(tput bold)$@$(tput sgr0)"
}


function make_upload () {
    CWD=$PWD

    say "Generating HTML"
    make_html

    say "Syncing to blog server"
    cp -v "$SLUG.html" ../blog/notes/python/index.html
    rm -v ../blog/notes/python/*.png
    cp -v *.png ../blog/notes/python/
    cd ../blog
    blog_sync  # Defined in ~/.bash_profile
    cd $CWD

    say "Generating EPUB"
    make_epub
    say "Uploading EPUB"
    s3_put "$SLUG.epub"

    say "Generating PDF"
    make_pdf
    say "Uploading PDF"
    s3_put "$SLUG.pdf"

    say "Generating MOBI"
    make_mobi
    say "Uploading MOBI"
    s3_put "$SLUG.mobi"
}
