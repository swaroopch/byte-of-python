#!/usr/bin/env python

import os
import glob
import subprocess
try:
    from xmlrpc.client import ServerProxy
except ImportError:
    from xmlrpclib import ServerProxy

import boto
import boto.s3.bucket
import boto.s3.key

from fabric.api import task, local


##################################################


SHORT_PROJECT_NAME = 'python'
FULL_PROJECT_NAME = 'byte_of_{}'.format(SHORT_PROJECT_NAME)


# The keys are the file names of the Pandoc source files.
# e.g. '01-frontpage.md'
# The values are the slugs of the WordPress pages
# e.g. http://www.swaroopch.com/notes/Python_en-Table_of_Contents
MARKDOWN_FILES = {
    '01-frontpage.md' : 'Python',
    '02-table-of-contents.md' : 'Python_en-Table_of_Contents',
}


## NOTES
## 1. This assumes that you have already created the S3 bucket whose name is stored in
##    AWS_S3_BUCKET_NAME environment variable.
## 2. Under that S3 bucket, you have created a folder whose name is stored above as
##    SHORT_PROJECT_NAME.
## 3. Under that S3 bucket, you have created a folder whose name is stored as
##    SHORT_PROJECT_NAME/assets.


##################################################


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

# In my case, they are the same - 'files.swaroopch.com'
# http://docs.amazonwebservices.com/AmazonS3/latest/dev/VirtualHosting.html#VirtualHostingCustomURLs
S3_PUBLIC_URL = os.environ['AWS_S3_BUCKET_NAME']
# else
#S3_PUBLIC_URL = 's3.amazonaws.com/{}'.format(os.environ['AWS_S3_BUCKET_NAME'])


def markdown_to_html(source_text):
    args = ['pandoc',
            '-f', 'markdown',
            '-t', 'html',
            '-S']
    p = subprocess.Popen(args, stdin=subprocess.PIPE, stdout=subprocess.PIPE)
    output = p.communicate(source_text)[0]

    # TODO Replace image URLs with uploaded AWS S3 assets public URLs

    return output


def __upload_to_s3(filename, key):
    conn = boto.connect_s3()
    b = boto.s3.bucket.Bucket(conn, os.environ['AWS_S3_BUCKET_NAME'])
    k = boto.s3.key.Key(b)
    k.key = key
    k.set_contents_from_filename(filename)
    k.set_acl('public-read')
    print("Uploaded to S3 : http://{}/{}".format(S3_PUBLIC_URL, key))


def upload_output_to_s3(filename):
    key = "{}/{}".format(SHORT_PROJECT_NAME, filename)
    __upload_to_s3(filename, key)


def upload_asset_to_s3(filename):
    key = "{}/assets/{}".format(SHORT_PROJECT_NAME, filename)
    __upload_to_s3(filename, key)


@task
def wp():
    for m in MARKDOWN_FILES.keys():
        converted_text = markdown_to_html(open(m).read())
        print converted_text[:50]
        # TODO Upload to WordPress
        # https://github.com/rgrp/pywordpress/blob/master/pywordpress.py
        # file:///Users/swaroop/code/docs/python/library/xmlrpclib.html


@task
def epub():
    args = ['pandoc',
            '-f', 'markdown',
            '-t', 'epub',
            '-o', '{}.epub'.format(FULL_PROJECT_NAME),
            '-S'] + MARKDOWN_FILES.keys()
    local(' '.join(args))
    if AWS_ENABLED:
        upload_output_to_s3('{}.epub'.format(FULL_PROJECT_NAME))


@task
def pdf():
    args = ['pandoc',
            '-f', 'markdown',
            ##'-t', 'pdf', # Intentionally commented out due to https://github.com/jgm/pandoc/issues/571
            '-o', '{}.pdf'.format(FULL_PROJECT_NAME),
            '-S'] + MARKDOWN_FILES.keys()
    local(' '.join(args))
    if AWS_ENABLED:
        upload_output_to_s3('{}.pdf'.format(FULL_PROJECT_NAME))


POSSIBLE_OUTPUTS = (
    '{}.epub'.format(FULL_PROJECT_NAME),
    '{}.pdf'.format(FULL_PROJECT_NAME),
)


@task
def clean():
    for filename in POSSIBLE_OUTPUTS:
        if os.path.exists(filename):
            os.remove(filename)
            print("Removed {}".format(filename))
