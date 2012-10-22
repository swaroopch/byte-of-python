#!/usr/bin/env python

from __future__ import print_function


##### Configuration ##############################

import json

CONFIG = json.load(open('config.json'))

## NOTES
## 1. This assumes that you have already created the S3 bucket whose name
##    is stored in AWS_S3_BUCKET_NAME environment variable.
## 2. Under that S3 bucket, you have created a folder whose name is stored
##    above as SHORT_PROJECT_NAME.
## 3. Under that S3 bucket, you have created a folder whose name is stored as
##    SHORT_PROJECT_NAME/assets.


##### Imports ####################################


import os
import subprocess
import copy
from xmlrpclib import ServerProxy

import boto
import boto.s3.bucket
import boto.s3.key
from bs4 import BeautifulSoup

from fabric.api import task, local


##### Start with checks ##########################


for chapter in CONFIG['MARKDOWN_FILES']:
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
    key = "{}/{}".format(CONFIG['SHORT_PROJECT_NAME'],
                         filename.split('/')[-1])
    return _upload_to_s3(filename, key)


def upload_asset_to_s3(filename):
    key = "{}/assets/{}".format(CONFIG['SHORT_PROJECT_NAME'],
                                filename.split('/')[-1])
    return _upload_to_s3(filename, key)


def replace_images_with_s3_urls(text):
    """http://www.crummy.com/software/BeautifulSoup/bs4/doc/"""
    soup = BeautifulSoup(text)
    for image in soup.find_all('img'):
        image['src'] = upload_asset_to_s3(image['src'])
    return unicode(soup)


def markdown_to_html(source_text, upload_assets_to_s3=False):
    """Convert from Markdown to HTML; optional: upload images, etc. to S3."""
    args = ['pandoc',
            '-f', 'markdown',
            '-t', 'html5']
    p = subprocess.Popen(args, stdin=subprocess.PIPE, stdout=subprocess.PIPE)
    output = p.communicate(source_text)[0]

    # http://wordpress.org/extend/plugins/raw-html/
    output = '<!--raw-->\n' + output + '\n<!--/raw-->'

    # NOTE: Also assumes that you have added the CSS from
    # `pandoc -S -t html5` to the `style.css` of your active Wordpress theme.

    if upload_assets_to_s3:
        output = replace_images_with_s3_urls(output)

    return output


def _wordpress_get_pages():
    server = ServerProxy(os.environ['WORDPRESS_RPC_URL'])
    print("Fetching list of pages from WP")
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


def collect_header_anchors(chapter, i, all_headers):
    soup = BeautifulSoup(chapter['html'])
    for header in soup.find_all(['h1', 'h2', 'h3', 'h4', 'h5', 'h6']):
        if 'id' in header.attrs:
            all_headers[header['id']] = i


def fix_links_to_other_chapters(chapter, chapters, all_headers):
    """Fix links to other sections with Wordpress page URL."""
    soup = BeautifulSoup(chapter['html'])
    for link in soup.find_all('a'):
        if 'href' in link.attrs:
            if link['href'].startswith('#'):
                header_id = link['href'][1:]
                assert header_id in all_headers, \
                    "#{} does not exist, referred in {}".format(
                    header_id, chapter['file'])
                other_chapter = chapters[all_headers[header_id]]
                link['href'] = '{}#{}'.format(
                    other_chapter['link'],
                    header_id)
    chapter['html'] = unicode(soup)


##### Tasks ######################################


@task
def wp():
    """https://codex.wordpress.org/XML-RPC_WordPress_API/Posts"""
    if WORDPRESS_ENABLED:
        chapters = copy.deepcopy(CONFIG['MARKDOWN_FILES'])

        # header anchor id -> index in MARKDOWN_FILES
        all_headers = {}

        # Render html
        print("Rendering html")
        for (i, chapter) in enumerate(chapters):
            chapter['html'] = markdown_to_html(open(chapter['file']).read(),
                                               upload_assets_to_s3=AWS_ENABLED)

            collect_header_anchors(chapter, i, all_headers)

            chapter['link'] = "{}/{}/{}".format(
                os.environ['WORDPRESS_BASE_URL'],
                os.environ['WORDPRESS_PARENT_PAGE_SLUG'],
                chapter['slug'])

        # Fix cross-links
        for chapter in chapters:
            fix_links_to_other_chapters(chapter, chapters, all_headers)

        # Add previous and next links at end of html
        for (i, chapter) in enumerate(chapters):
            previous_link = None
            if i > 0:
                previous_link = chapters[i - 1]['link']

            next_link = None
            if i < len(chapters) - 1:
                next_link = chapters[i + 1]['link']

            if previous_link is not None or next_link is not None:
                chapter['html'] += "\n"

            if previous_link is not None:
                chapter['html'] += """\
<a href="{}">&lArr; Previous chapter</a>\
""".format(previous_link)

            if previous_link is not None and next_link is not None:
                chapter['html'] += '&nbsp;' * 5

            if next_link is not None:
                chapter['html'] += """\
<a href="{}">Next chapter &rArr;</a>\
""".format(next_link)

        # Fetch list of pages on the server and determine which already exist
        existing_pages = _wordpress_get_pages()
        existing_page_slugs = [i.get('post_name') for i in existing_pages]

        def page_slug_to_id(slug):
            pages = [i for i in existing_pages if i.get('post_name') == slug]
            page = pages[0]
            return page['post_id']

        for chapter in chapters:
            if chapter['slug'] in existing_page_slugs:
                chapter['page_id'] = page_slug_to_id(chapter['slug'])

        # Send to WP
        print("Uploading to WordPress")
        for chapter in chapters:
            if chapter['slug'] in existing_page_slugs:
                print("Existing page: {}".format(chapter['link']))
                assert wordpress_edit_page(chapter['page_id'],
                                           chapter['title'],
                                           chapter['html'])
            else:
                print("New page: {}".format(chapter['link']))
                assert wordpress_new_page(chapter['slug'],
                                          chapter['title'],
                                          chapter['html'])


@task
def html():
    """HTML5 output."""
    args = ['pandoc',
            '-f', 'markdown',
            '-t', 'html5',
            '-o', '{}.html'.format(CONFIG['FULL_PROJECT_NAME']),
            '-s',
            '--toc'] + [i['file'] for i in CONFIG['MARKDOWN_FILES']]
    local(' '.join(args))
    local('open {}.html'.format(CONFIG['FULL_PROJECT_NAME']))


@task
def epub():
    """http://johnmacfarlane.net/pandoc/epub.html"""
    args = ['pandoc',
            '-f', 'markdown',
            '-t', 'epub',
            '-o', '{}.epub'.format(CONFIG['FULL_PROJECT_NAME'])] + \
        [i['file'] for i in CONFIG['MARKDOWN_FILES']]
    # TODO --epub-cover-image
    # TODO --epub-metadata
    # TODO --epub-stylesheet
    local(' '.join(args))
    if AWS_ENABLED:
        upload_output_to_s3('{}.epub'.format(CONFIG['FULL_PROJECT_NAME']))


@task
def pdf():
    """http://johnmacfarlane.net/pandoc/README.html#creating-a-pdf"""
    args = ['pandoc',
            '-f', 'markdown',
            # https://github.com/jgm/pandoc/issues/571
            #'-t', 'pdf',
            '-o', '{}.pdf'.format(CONFIG['FULL_PROJECT_NAME']),
            '--toc'] + [i['file'] for i in CONFIG['MARKDOWN_FILES']]
    local(' '.join(args))
    if AWS_ENABLED:
        upload_output_to_s3('{}.pdf'.format(CONFIG['FULL_PROJECT_NAME']))


@task
def docx():
    """OOXML document format."""
    args = ['pandoc',
            '-f', 'markdown',
            '-t', 'docx',
            '-o', '{}.docx'.format(CONFIG['FULL_PROJECT_NAME'])] + \
        [i['file'] for i in CONFIG['MARKDOWN_FILES']]
    local(' '.join(args))
    if AWS_ENABLED:
        upload_output_to_s3('{}.docx'.format(CONFIG['FULL_PROJECT_NAME']))


@task
def odt():
    """OpenDocument document format."""
    args = ['pandoc',
            '-f', 'markdown',
            '-t', 'odt',
            '-o', '{}.odt'.format(CONFIG['FULL_PROJECT_NAME'])] + \
        [i['file'] for i in CONFIG['MARKDOWN_FILES']]
    local(' '.join(args))
    if AWS_ENABLED:
        upload_output_to_s3('{}.odt'.format(CONFIG['FULL_PROJECT_NAME']))


@task
def clean():
    """Remove generated output files"""
    possible_outputs = (
        '{}.html'.format(CONFIG['FULL_PROJECT_NAME']),
        '{}.epub'.format(CONFIG['FULL_PROJECT_NAME']),
        '{}.pdf'.format(CONFIG['FULL_PROJECT_NAME']),
        '{}.docx'.format(CONFIG['FULL_PROJECT_NAME']),
        '{}.odt'.format(CONFIG['FULL_PROJECT_NAME']),
    )

    for filename in possible_outputs:
        if os.path.exists(filename):
            os.remove(filename)
            print("Removed {}".format(filename))
