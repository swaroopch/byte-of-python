#!/usr/bin/env python

import os
import glob
import subprocess
from fabric.api import local


# The keys are the file names of the Pandoc source files.
# e.g. '01-frontpage.md'
# The values are the slugs of the WordPress pages
# e.g. http://www.swaroopch.com/notes/Python_en-Table_of_Contents
MARKDOWN_FILES = {
    '01-frontpage.md' : 'Python',
    '02-table-of-contents.md' : 'Python_en-Table_of_Contents',
}


def _markdown_to_html(source_text):
    from_format = 'markdown'
    to_format = 'html'

    args = ['pandoc',
            '-f', from_format,
            '-t', to_format,
            '-S']
    p = subprocess.Popen(args, stdin=subprocess.PIPE, stdout=subprocess.PIPE)
    output = p.communicate(source_text)[0]

    # TODO Replace image URLs with uploaded AWS S3 public URLs

    return output


def html():
    for m in MARKDOWN_FILES.keys():
        converted_text = _markdown_to_html(open(m).read())
        output_file_name = MARKDOWN_FILES[m] + ".html"
        with open(output_file_name, 'w') as output:
            output.write(converted_text)
        local("open {}".format(output_file_name))


def cleanup():
    for m in MARKDOWN_FILES.keys():
        output_file_name = MARKDOWN_FILES[m] + ".html"
        if os.path.exists(output_file_name):
            os.remove(output_file_name)


def epub():
    from_format = 'markdown'
    to_format = 'epub'
    output_file_name = 'byte_of_python.epub'

    args = ['pandoc',
            '-f', from_format,
            '-t', to_format,
            '-o', output_file_name,
            '-S'] + MARKDOWN_FILES.keys()
    local(' '.join(args))
