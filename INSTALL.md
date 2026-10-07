```
# Bootstrap the pinned HonKit fork used by this book.
# The first run clones and builds it in .honkit/.
make setup

# show website running locally
make serve

# generate website files
make build

# generate PDF (with physical page numbers in the table of contents)
make pdf

# generate EPUB
make epub
```

The wrapper in `scripts/honkit` pins the HonKit fork commit that implements
physical PDF table-of-contents page numbers. Once that change is released by
HonKit, the wrapper can be replaced with the corresponding published package.

See https://github.com/honkit/honkit and https://honkit.netlify.app/
