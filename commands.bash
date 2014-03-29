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

# TODO https://github.com/schacon/git-scribe/blob/master/lib/git-scribe/generate.rb#L107
# TODO Instead, create an official backend for asciidoctor to create a website?
#
function make_website () {
    echo "TODO"
}

function install_deps_osx () {
    # http://brew.sh
    brew update
    brew install docbook docbook-xsl fop epubcheck git
    brew tap homebrew/binary
    brew install kindlegen
    # brew install asciidoc

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

    # If emacs, install package: https://github.com/sensorflo/adoc-mode/wiki
}
