#!/usr/bin/env python

import os
import glob
import subprocess
try:
    from xmlrpc.client import ServerProxy
except ImportError:
    from xmlrpclib import ServerProxy
from pprint import pprint

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
MARKDOWN_FILES = [
    {
        'file'   : '01-frontpage.md',
        'slug'   : "Python",
        'title'  : "Python",
    },
    {
        'file'   : '02-table-of-contents.md',
        'slug'   : "Python_en-Table_of_Contents",
        'title'  : "Table of Contents of A Byte of Python",
    },
]


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


if os.environ.get('WORDPRESS_RPC_URL') is not None \
        and len(os.environ['WORDPRESS_RPC_URL']) > 0 \
        and os.environ.get('WORDPRESS_BASE_URL') is not None \
        and len(os.environ['WORDPRESS_BASE_URL']) > 0 \
        and os.environ.get('WORDPRESS_BLOG_ID') is not None \
        and len(os.environ['WORDPRESS_BLOG_ID']) > 0 \
        and os.environ.get('WORDPRESS_USERNAME') is not None \
        and len(os.environ['WORDPRESS_USERNAME']) > 0 \
        and os.environ.get('WORDPRESS_PASSWORD') is not None \
        and len(os.environ['WORDPRESS_PASSWORD']) > 0 \
        and os.environ.get('WORDPRESS_PARENT_PAGE_ID') is not None \
        and len(os.environ['WORDPRESS_PARENT_PAGE_ID']) > 0 \
        and os.environ.get('WORDPRESS_PARENT_PAGE_SLUG') is not None \
        and len(os.environ['WORDPRESS_PARENT_PAGE_SLUG']) > 0:
    WORDPRESS_ENABLED = True
else:
    WORDPRESS_ENABLED = False
    print("NOTE: Wordpress uploading is disabled because of missing environment variables.")


##################################################


def markdown_to_html(source_text):
    args = ['pandoc',
            '-f', 'markdown',
            '-t', 'html',
            '-S']
    p = subprocess.Popen(args, stdin=subprocess.PIPE, stdout=subprocess.PIPE)
    output = p.communicate(source_text)[0]

    # TODO Replace image URLs with uploaded AWS S3 assets public URLs

    return output


def _upload_to_s3(filename, key):
    conn = boto.connect_s3()
    b = boto.s3.bucket.Bucket(conn, os.environ['AWS_S3_BUCKET_NAME'])
    k = boto.s3.key.Key(b)
    k.key = key
    k.set_contents_from_filename(filename)
    k.set_acl('public-read')
    print("Uploaded to S3 : http://{}/{}".format(S3_PUBLIC_URL, key))


def upload_output_to_s3(filename):
    key = "{}/{}".format(SHORT_PROJECT_NAME, filename)
    _upload_to_s3(filename, key)


def upload_asset_to_s3(filename):
    key = "{}/assets/{}".format(SHORT_PROJECT_NAME, filename)
    _upload_to_s3(filename, key)


def _wordpress_get_pages():
    server = ServerProxy(os.environ['WORDPRESS_RPC_URL'])
    print("(Fetching list of pages from WP)")
    return server.wp.getPosts(os.environ['WORDPRESS_BLOG_ID'],
                os.environ['WORDPRESS_USERNAME'],
                os.environ['WORDPRESS_PASSWORD'],
                {'post_type' : 'page', 'number' : pow(10, 5)})


def wordpress_new_page(slug, title, content):
    """Create a new Wordpress page.

https://codex.wordpress.org/XML-RPC_WordPress_API/Posts#wp.newPost
https://codex.wordpress.org/Function_Reference/wp_insert_post
http://docs.python.org/library/xmlrpclib.html
"""
    server = ServerProxy(os.environ['WORDPRESS_RPC_URL'])
    return server.wp.newPost(os.environ['WORDPRESS_BLOG_ID'],
                os.environ['WORDPRESS_USERNAME'],
                os.environ['WORDPRESS_PASSWORD'],
                {
                    'post_name'       : slug,
                    'post_content'    : content,
                    'post_title'      : title,
                    'post_parent'     : os.environ['WORDPRESS_PARENT_PAGE_ID'],
                    #'post_category'   : os.environ['WORDPRESS_CATEGORY'], # TODO Take env var for category
                    'post_type'       : 'page',
                    'post_status'     : 'publish',
                    'comment_status'  : 'closed',
                    'ping_status'     : 'closed',
                })


def wordpress_edit_page(post_id, content):
    """Edit a Wordpress page.

https://codex.wordpress.org/XML-RPC_WordPress_API/Posts#wp.editPost
https://codex.wordpress.org/Function_Reference/wp_insert_post
http://docs.python.org/library/xmlrpclib.html
"""
    server = ServerProxy(os.environ['WORDPRESS_RPC_URL'])
    return server.wp.editPost(os.environ['WORDPRESS_BLOG_ID'],
                os.environ['WORDPRESS_USERNAME'],
                os.environ['WORDPRESS_PASSWORD'],
                post_id,
                {
                    'post_content' : content,
                })


@task
def wp():
    """https://codex.wordpress.org/XML-RPC_WordPress_API/Posts"""
    if WORDPRESS_ENABLED:
        existing_pages = _wordpress_get_pages()
        existing_page_slugs = [i.get('post_name') for i in existing_pages]

        for chapter in MARKDOWN_FILES:
            html = markdown_to_html(open(chapter['file']).read())

            if chapter['slug'].lower() in existing_page_slugs:
                page_id = [i for i in existing_pages \
                            if i.get('post_name') == chapter['slug'].lower()] \
                        [0] \
                        ['post_id']
                print("Existing page to be updated: {} : {}".format(chapter['slug'], page_id))
                result = wordpress_edit_page(page_id, html)
                print("Result: {}".format(result))
            else:
                print("New page to be created: {}".format(chapter['slug']))
                result = wordpress_new_page(chapter['slug'], chapter['title'], html)
                print("Result: {}".format(result))

            page_url = "{}/{}/{}".format(os.environ['WORDPRESS_BASE_URL'],
                os.environ['WORDPRESS_PARENT_PAGE_SLUG'],
                chapter['slug'])
            print(page_url)
            print


@task
def epub():
    """http://johnmacfarlane.net/pandoc/epub.html"""
    args = ['pandoc',
            '-f', 'markdown',
            '-t', 'epub',
            '-o', '{}.epub'.format(FULL_PROJECT_NAME),
            '-S'] + [i['file'] for i in MARKDOWN_FILES]
    local(' '.join(args))
    if AWS_ENABLED:
        upload_output_to_s3('{}.epub'.format(FULL_PROJECT_NAME))


@task
def pdf():
    """http://johnmacfarlane.net/pandoc/README.html#creating-a-pdf"""
    args = ['pandoc',
            '-f', 'markdown',
            ##'-t', 'pdf', # Intentionally commented out due to https://github.com/jgm/pandoc/issues/571
            '-o', '{}.pdf'.format(FULL_PROJECT_NAME),
            '-S'] + [i['file'] for i in MARKDOWN_FILES]
    local(' '.join(args))
    if AWS_ENABLED:
        upload_output_to_s3('{}.pdf'.format(FULL_PROJECT_NAME))


POSSIBLE_OUTPUTS = (
    '{}.epub'.format(FULL_PROJECT_NAME),
    '{}.pdf'.format(FULL_PROJECT_NAME),
)


@task
def clean():
    """Remove generated output files"""
    for filename in POSSIBLE_OUTPUTS:
        if os.path.exists(filename):
            os.remove(filename)
            print("Removed {}".format(filename))
