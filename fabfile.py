#!/usr/bin/env python

from __future__ import print_function


##### Configuration ##############################


SHORT_PROJECT_NAME = 'python'
FULL_PROJECT_NAME = 'byte_of_{}'.format(SHORT_PROJECT_NAME)


# NOTE Slugs MUST be lower-case
MARKDOWN_FILES = [
    {
        'file': '01-frontpage.pd',
        'slug': "python",
        'title': "Python",
    },
    {
        'file': '02-preface.pd',
        'slug': "python_en-preface",
        'title': "Python : Preface",
    },
    {
        'file': '03-intro.pd',
        'slug': "python_en-introduction",
        'title': "Python : Introduction",
    },
    {
        'file': '04-installation.pd',
        'slug': "python_en-installation",
        'title': "Python : Installation",
    },
    {
        'file': '05-first-steps.pd',
        'slug': "python_en-first_steps",
        'title': "Python : First Steps",
    },
    {
        'file': '06-basics.pd',
        'slug': "python_en-basics",
        'title': "Python : Basics",
    },
    {
        'file': '07-operators-expressions.pd',
        'slug': "python_en-operators_and_expressions",
        'title': "Python : Operators and Expressions",
    },
    {
        'file': '08-control-flow.pd',
        'slug': "python_en-control_flow",
        'title': "Python : Control Flow",
    },
    {
        'file': '09-functions.pd',
        'slug': "python_en-functions",
        'title': "Python : Functions",
    },
    {
        'file': '10-modules.pd',
        'slug': "python_en-modules",
        'title': "Python : Modules",
    },
    {
        'file': '11-data-structures.pd',
        'slug': "python_en-data_structures",
        'title': "Python : Data Structures",
    },
]


## NOTES
## 1. This assumes that you have already created the S3 bucket whose name
##    is stored in AWS_S3_BUCKET_NAME environment variable.
## 2. Under that S3 bucket, you have created a folder whose name is stored
##    above as SHORT_PROJECT_NAME.
## 3. Under that S3 bucket, you have created a folder whose name is stored as
##    SHORT_PROJECT_NAME/assets.


##### Imports ####################################


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
from bs4 import BeautifulSoup

from fabric.api import task, local


##### Start with checks ##########################


for chapter in MARKDOWN_FILES:
    assert (chapter['slug'].lower() == chapter['slug']), \
        "Slug must be lower case : {}".format(chapter['slug'])

if str(os.environ.get('AWS_ENABLED')).lower() == 'false':
    AWS_ENABLED = False
elif os.environ.get('AWS_ACCESS_KEY_ID') is not None \
        and len(os.environ['AWS_ACCESS_KEY_ID']) > 0 \
        and os.environ.get('AWS_SECRET_ACCESS_KEY') is not None \
        and len(os.environ['AWS_SECRET_ACCESS_KEY']) > 0 \
        and os.environ.get('AWS_S3_BUCKET_NAME') is not None \
        and len(os.environ['AWS_S3_BUCKET_NAME']) > 0:
    AWS_ENABLED = True
else:
    AWS_ENABLED = False
    print("NOTE: S3 uploading is disabled because of missing " +
          "AWS key environment variables.")

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
    print("NOTE: Wordpress uploading is disabled because of " +
          "missing environment variables.")


##### Helper methods #############################


def _upload_to_s3(filename, key):
    """http://docs.pythonboto.org/en/latest/s3_tut.html#storing-data"""
    conn = boto.connect_s3()
    b = boto.s3.bucket.Bucket(conn, os.environ['AWS_S3_BUCKET_NAME'])
    k = boto.s3.key.Key(b)
    k.key = key
    k.set_contents_from_filename(filename)
    k.set_acl('public-read')

    url = 'http://{}/{}'.format(S3_PUBLIC_URL, key)
    print("Uploaded to S3 : {}".format(url))
    return url


def upload_output_to_s3(filename):
    key = "{}/{}".format(SHORT_PROJECT_NAME, filename.split('/')[-1])
    return _upload_to_s3(filename, key)


def upload_asset_to_s3(filename):
    key = "{}/assets/{}".format(SHORT_PROJECT_NAME, filename.split('/')[-1])
    return _upload_to_s3(filename, key)


def replace_images_with_s3_urls(text):
    """http://www.crummy.com/software/BeautifulSoup/bs4/doc/"""
    soup = BeautifulSoup(text)
    for image in soup.find_all('img'):
        image['src'] = upload_asset_to_s3(image['src'])
    return soup.prettify()


def markdown_to_html(source_text, upload_assets_to_s3=False):
    """Convert from Markdown to HTML; optional: upload images, etc. to S3."""
    args = ['pandoc',
            '-f', 'markdown',
            '-t', 'html5']
    p = subprocess.Popen(args, stdin=subprocess.PIPE, stdout=subprocess.PIPE)
    output = p.communicate(source_text)[0]

    # http://wordpress.org/extend/plugins/raw-html/
    output = '<!--raw-->\n' + output + '\n<!--/raw-->'

    if upload_assets_to_s3:
        output = replace_images_with_s3_urls(output)

    return output


def _wordpress_get_pages():
    server = ServerProxy(os.environ['WORDPRESS_RPC_URL'])
    print("(Fetching list of pages from WP)")
    return server.wp.getPosts(os.environ['WORDPRESS_BLOG_ID'],
                              os.environ['WORDPRESS_USERNAME'],
                              os.environ['WORDPRESS_PASSWORD'],
                              {
                                  'post_type': 'page',
                                  'number': pow(10, 5),
                              })


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
                                 'post_name': slug,
                                 'post_content': content,
                                 'post_title': title,
                                 'post_parent':
                                 os.environ['WORDPRESS_PARENT_PAGE_ID'],
                                 'post_type': 'page',
                                 'post_status': 'publish',
                                 'comment_status': 'closed',
                                 'ping_status': 'closed',
                             })


def wordpress_edit_page(post_id, title, content):
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
                                  'post_content': content,
                                  'post_title': title,
                              })


##### Tasks ######################################


@task
def wp():
    """https://codex.wordpress.org/XML-RPC_WordPress_API/Posts"""
    if WORDPRESS_ENABLED:
        existing_pages = _wordpress_get_pages()
        existing_page_slugs = [i.get('post_name') for i in existing_pages]

        def page_slug_to_id(slug):
            pages = [i for i in existing_pages if i.get('post_name') == slug]
            page = pages[0]
            return page['post_id']

        for chapter in MARKDOWN_FILES:
            html = markdown_to_html(open(chapter['file']).read(),
                                    upload_assets_to_s3=True)
            # TODO Add previous and next links at end of html

            if chapter['slug'] in existing_page_slugs:
                page_id = page_slug_to_id(chapter['slug'])
                print("Existing page to be updated: {} : {}".format(
                      chapter['slug'],
                      page_id))
                result = wordpress_edit_page(page_id,
                                             chapter['title'],
                                             html)
                print("Result: {}".format(result))
            else:
                print("New page to be created: {}".format(chapter['slug']))
                result = wordpress_new_page(chapter['slug'],
                                            chapter['title'],
                                            html)
                print("Result: {}".format(result))

            page_url = "{}/{}/{}".format(os.environ['WORDPRESS_BASE_URL'],
                       os.environ['WORDPRESS_PARENT_PAGE_SLUG'],
                       chapter['slug'])
            print(page_url)
            print()


@task
def html():
    """HTML5 output."""
    args = ['pandoc',
            '-f', 'markdown',
            '-t', 'html5',
            '-o', '{}.html'.format(FULL_PROJECT_NAME),
            '-s',
            '--toc'] + [i['file'] for i in MARKDOWN_FILES]
    local(' '.join(args))
    local('open {}.html'.format(FULL_PROJECT_NAME))


@task
def epub():
    """http://johnmacfarlane.net/pandoc/epub.html"""
    args = ['pandoc',
            '-f', 'markdown',
            '-t', 'epub',
            '-o', '{}.epub'.format(FULL_PROJECT_NAME)] + \
        [i['file'] for i in MARKDOWN_FILES]
    # TODO --epub-cover-image
    # TODO --epub-metadata
    # TODO --epub-stylesheet
    local(' '.join(args))
    if AWS_ENABLED:
        upload_output_to_s3('{}.epub'.format(FULL_PROJECT_NAME))


@task
def pdf():
    """http://johnmacfarlane.net/pandoc/README.html#creating-a-pdf"""
    args = ['pandoc',
            '-f', 'markdown',
            # https://github.com/jgm/pandoc/issues/571
            #'-t', 'pdf',
            '-o', '{}.pdf'.format(FULL_PROJECT_NAME)] + \
        [i['file'] for i in MARKDOWN_FILES]
    local(' '.join(args))
    if AWS_ENABLED:
        upload_output_to_s3('{}.pdf'.format(FULL_PROJECT_NAME))


@task
def docx():
    """OOXML document format."""
    args = ['pandoc',
            '-f', 'markdown',
            '-t', 'docx',
            '-o', '{}.docx'.format(FULL_PROJECT_NAME)] + \
        [i['file'] for i in MARKDOWN_FILES]
    local(' '.join(args))
    if AWS_ENABLED:
        upload_output_to_s3('{}.docx'.format(FULL_PROJECT_NAME))


@task
def odt():
    """OpenDocument document format."""
    args = ['pandoc',
            '-f', 'markdown',
            '-t', 'odt',
            '-o', '{}.odt'.format(FULL_PROJECT_NAME)] + \
        [i['file'] for i in MARKDOWN_FILES]
    local(' '.join(args))
    if AWS_ENABLED:
        upload_output_to_s3('{}.odt'.format(FULL_PROJECT_NAME))


@task
def clean():
    """Remove generated output files"""
    possible_outputs = (
        '{}.html'.format(FULL_PROJECT_NAME),
        '{}.epub'.format(FULL_PROJECT_NAME),
        '{}.pdf'.format(FULL_PROJECT_NAME),
        '{}.docx'.format(FULL_PROJECT_NAME),
        '{}.odt'.format(FULL_PROJECT_NAME),
    )

    for filename in possible_outputs:
        if os.path.exists(filename):
            os.remove(filename)
            print("Removed {}".format(filename))
