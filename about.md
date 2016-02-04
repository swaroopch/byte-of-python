# Appendix: Colophon {#colophon}

Almost all of the software that I have used in the creation of this book are [FLOSS](./floss.md#floss).

## Birth of the Book

In the first draft of this book, I had used Red Hat 9.0 Linux as the foundation of my setup and in the sixth draft, I used Fedora Core 3 Linux as the basis of my setup.

Initially, I was using KWord to write the book (as explained in the [history lesson](./revision_history.md#history-lesson)).

## Teenage Years

Later, I switched to DocBook XML using Kate but I found it too tedious. So, I switched to OpenOffice which was just excellent with the level of control it provided for formatting as well as the PDF generation, but it produced very sloppy HTML from the document.

Finally, I discovered XEmacs and I rewrote the book from scratch in DocBook XML (again) after I decided that this format was the long term solution.

In the sixth draft, I decided to use Quanta+ to do all the editing. The standard XSL stylesheets that came with Fedora Core 3 Linux were being used. However, I had written a CSS document to give color and style to the HTML pages. I had also written a crude lexical analyzer, in Python of course, which automatically provides syntax highlighting to all the program listings.

For the seventh draft, I was using [MediaWiki](http://www.mediawiki.org) as the basis of my setup. I used to edit everything online and the readers can directly read/edit/discuss within the wiki website, but I ended up spending more time fighting spam than writing.

For the eight draft, I used [Vim]({{ book.vimBookUrl }}), [Pandoc](http://johnmacfarlane.net/pandoc/README.html), and Mac OS X.

For the ninth draft, I switched to [AsciiDoc format](http://asciidoctor.org/docs/what-is-asciidoc/) and used [Emacs 24.3](http://www.masteringemacs.org/articles/2013/03/11/whats-new-emacs-24-3/),
[tomorrow theme](https://github.com/chriskempson/tomorrow-theme),
[Fira Mono font](https://www.mozilla.org/en-US/styleguide/products/firefox-os/typeface/#download-primary) and [adoc-mode](https://github.com/sensorflo/adoc-mode/wiki) to write.

## Now

2016: I got tired of several minor rendering issues in AsciiDoctor, like the `++` in `C/C++` would disappear and it was hard to keep track of escaping such minor things. Plus, I had become reluctant to edit the text because of the complex Asciidoc format.

For the tenth draft, I switched to writing in Markdown + [GitBook](https://www.gitbook.com) format, using the [Spacemacs editor](http://spacemacs.org).

## About the Author

See {{ book.authorUrl }}
