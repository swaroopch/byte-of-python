#!/usr/bin/env python

import os
import glob
import subprocess
try:
    from xmlrpc.client import ServerProxy
except ImportError:
    from xmlrpclib import ServerProxy

import boto

from fabric.api import task, local


if os.environ.get('AWS_ACCESS_KEY_ID') is not None \
        and len(os.environ['AWS_ACCESS_KEY_ID']) > 0 \
        and os.environ.get('AWS_SECRET_ACCESS_KEY') is not None \
        and len(os.environ['AWS_SECRET_ACCESS_KEY']) > 0 \
        and os.environ.get('AWS_S3_BUCKET_NAME') is not None \
        and len(os.environ['AWS_S3_BUCKET_NAME']) > 0:
    AWS_ENABLED = True
else:
    AWS_ENABLED = False
    print("NOTE: S3 uploading is disabled because of missing AWS key environment variables.")



# The keys are the file names of the Pandoc source files.
# e.g. '01-frontpage.md'
# The values are the slugs of the WordPress pages
# e.g. http://www.swaroopch.com/notes/Python_en-Table_of_Contents
MARKDOWN_FILES = {
    '01-frontpage.md' : 'Python',
    '02-table-of-contents.md' : 'Python_en-Table_of_Contents',
}


def _markdown_to_html(source_text):
    args = ['pandoc',
            '-f', 'markdown',
            '-t', 'html',
            '-S']
    p = subprocess.Popen(args, stdin=subprocess.PIPE, stdout=subprocess.PIPE)
    output = p.communicate(source_text)[0]

    # TODO Replace image URLs with uploaded AWS S3 public URLs

    return output


@task
def wp():
    for m in MARKDOWN_FILES.keys():
        converted_text = _markdown_to_html(open(m).read())
        with open(output_file_name, 'w') as output:
            # TODO Replace with uploading to WordPress
            # https://github.com/rgrp/pywordpress/blob/master/pywordpress.py
            # file:///Users/swaroop/code/docs/python/library/xmlrpclib.html
            output.write(converted_text)
        local("open {}".format(output_file_name))


@task
def epub():
    args = ['pandoc',
            '-f', 'markdown',
            '-t', 'epub',
            '-o', 'byte_of_python.epub',
            '-S'] + MARKDOWN_FILES.keys()
    local(' '.join(args))


@task
def pdf():
    args = ['pandoc',
            '-f', 'markdown',
            ##'-t', 'pdf', # Intentionally commented out due to https://github.com/jgm/pandoc/issues/571
            '-o', 'byte_of_python.pdf',
            '-S'] + MARKDOWN_FILES.keys()
    local(' '.join(args))


POSSIBLE_OUTPUTS = (
    'byte_of_python.epub',
    'byte_of_python.pdf',
)


@task
def clean():
    for filename in POSSIBLE_OUTPUTS:
        if os.path.exists(filename):
            os.remove(filename)
            print("Removed {}".format(filename))


# TODO Make epub and pdf upload to S3 directly if AWS_ENABLED
# TODO http://docs.pythonboto.org/en/latest/s3_tut.html
