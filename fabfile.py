#!/usr/bin/env python

from __future__ import print_function

##### Configuration ##############################

import codecs
import os
import json

os.environ["PYTHONIOENCODING"] = "utf-8"

CONFIG_FILE = "config.json"
CONFIG = json.load(codecs.open(CONFIG_FILE, "r", "utf-8"))

OAUTH_CONFIG_FILE = "oauth.json"
OAUTH_CONFIG = None
if os.path.exists(OAUTH_CONFIG_FILE):
    OAUTH_CONFIG = json.load(codecs.open(OAUTH_CONFIG_FILE, "r", "utf-8"))

## NOTES
## 1. This assumes that you have already created the S3 bucket whose name
##    is stored in AWS_S3_BUCKET_NAME environment variable.
## 2. Under that S3 bucket, you have created a folder whose name is stored
##    above as SHORT_PROJECT_NAME.
## 3. Under that S3 bucket, you have created a folder whose name is stored as
##    SHORT_PROJECT_NAME/assets.


##### Imports ####################################

import datetime
import subprocess
import copy
import webbrowser
import urllib
import time
from functools import wraps

import boto
import boto.s3.bucket
import boto.s3.key
from bs4 import BeautifulSoup
import requests

from fabric.api import task, local
from fabric.utils import abort

import logging


##### Start with checks ##########################

logging.basicConfig(level=logging.DEBUG)
log = logging.getLogger(__name__)

for chapter in CONFIG["MARKDOWN_FILES"]:
    assert (chapter["slug"].lower() == chapter["slug"]), \
        "Slug must be lower case : {}".format(chapter["slug"])

if str(os.environ.get("AWS_ENABLED")).lower() == "false":
    AWS_ENABLED = False
elif os.environ.get("AWS_ACCESS_KEY_ID") is not None \
        and len(os.environ["AWS_ACCESS_KEY_ID"]) > 0 \
        and os.environ.get("AWS_SECRET_ACCESS_KEY") is not None \
        and len(os.environ["AWS_SECRET_ACCESS_KEY"]) > 0 \
        and os.environ.get("AWS_S3_BUCKET_NAME") is not None \
        and len(os.environ["AWS_S3_BUCKET_NAME"]) > 0:
    AWS_ENABLED = True
else:
    AWS_ENABLED = False
    print("NOTE: S3 uploading is disabled because of missing " +
          "AWS key environment variables.")

# In my case, they are the same - "files.swaroopch.com"
# http://docs.amazonwebservices.com/AmazonS3/latest/dev/VirtualHosting.html#VirtualHostingCustomURLs
if AWS_ENABLED:
    S3_PUBLIC_URL = os.environ["AWS_S3_BUCKET_NAME"]
    #else
    #S3_PUBLIC_URL = "s3.amazonaws.com/{}".format(
        #os.environ["AWS_S3_BUCKET_NAME"])


if OAUTH_CONFIG is not None:
    WORDPRESS_ENABLED = True
    WORDPRESS_CLIENT_ID = os.environ["WORDPRESS_CLIENT_ID"]
    WORDPRESS_CLIENT_SECRET = os.environ["WORDPRESS_CLIENT_SECRET"]
    WORDPRESS_PARENT_PAGE_ID = int(os.environ["WORDPRESS_PARENT_PAGE_ID"])
    WORDPRESS_PARENT_PAGE_SLUG = os.environ["WORDPRESS_PARENT_PAGE_SLUG"]
    WORDPRESS_BASE_URL = os.environ["WORDPRESS_BASE_URL"]
else:
    WORDPRESS_ENABLED = False
    print("NOTE: Wordpress uploading is disabled because of " +
          "missing environment variables.")


##### Helper methods #############################

def retry(f):
    @wraps(f)
    def wrapped_f(*args, **kwargs):
        MAX_ATTEMPTS = 5
        for attempt in range(1, MAX_ATTEMPTS + 1):
            try:
                return f(*args, **kwargs)
            except:
                log.exception("Attempt %s/%s failed : %s",
                              attempt,
                              MAX_ATTEMPTS,
                              (args, kwargs))
                time.sleep(10 * attempt)
        log.critical("All %s attempts failed : %s",
                     MAX_ATTEMPTS,
                     (args, kwargs))
    return wrapped_f


def _upload_to_s3(filename, key):
    """http://docs.pythonboto.org/en/latest/s3_tut.html#storing-data"""
    conn = boto.connect_s3()
    b = boto.s3.bucket.Bucket(conn, os.environ["AWS_S3_BUCKET_NAME"])
    k = boto.s3.key.Key(b)
    k.key = key
    k.set_contents_from_filename(filename)
    k.set_acl("public-read")

    url = "http://{}/{}".format(S3_PUBLIC_URL, key)
    print("Uploaded to S3 : {}".format(url))
    return url


def upload_output_to_s3(filename):
    key = "{}/{}".format(CONFIG["SHORT_PROJECT_NAME"],
                         filename.split("/")[-1])
    return _upload_to_s3(filename, key)


def upload_asset_to_s3(filename):
    key = "{}/assets/{}".format(CONFIG["SHORT_PROJECT_NAME"],
                                filename.split("/")[-1])
    return _upload_to_s3(filename, key)


def replace_images_with_s3_urls(text):
    """http://www.crummy.com/software/BeautifulSoup/bs4/doc/"""
    soup = BeautifulSoup(text)
    for image in soup.find_all("img"):
        image["src"] = upload_asset_to_s3(image["src"])
    return str(soup)


def markdown_to_html(source_text, upload_assets_to_s3=False):
    """Convert from Markdown to HTML; optional: upload images, etc. to S3."""
    args = ["pandoc",
            "-f", "markdown",
            "-t", "html5"]
    p = subprocess.Popen(args, stdin=subprocess.PIPE, stdout=subprocess.PIPE)
    output = p.communicate(source_text.encode("utf-8", "ignore"))[0]

    # http://wordpress.org/extend/plugins/raw-html/
    output = u"<!--raw-->\n" + \
             output.decode("utf-8", "ignore") + \
             u"\n<!--/raw-->"

    # NOTE: Also assumes that you have added the CSS from
    # `pandoc -S -t html5` to the `style.css` of your active Wordpress theme.

    if upload_assets_to_s3:
        output = replace_images_with_s3_urls(output)

    return output.decode("utf-8", "ignore")


def collect_header_anchors(chapter, i, all_headers):
    soup = BeautifulSoup(chapter["html"])
    for header in soup.find_all(["h1", "h2", "h3", "h4", "h5", "h6"]):
        if "id" in header.attrs:
            all_headers[header["id"]] = i


def fix_links_to_other_chapters(chapter, chapters, all_headers):
    """Fix links to other sections with Wordpress page URL."""
    soup = BeautifulSoup(chapter["html"])
    for link in soup.find_all("a"):
        if "href" in link.attrs:
            if link["href"].startswith("#"):
                header_id = link["href"][1:]
                assert header_id in all_headers, \
                    "#{} does not exist, referred in {}".format(
                    header_id, chapter["file"])
                other_chapter = chapters[all_headers[header_id]]
                link["href"] = "{}#{}".format(
                    other_chapter["link"],
                    header_id)
    chapter["html"] = unicode(soup)


def add_previous_next_links(chapter, i, chapters):
    previous_link = None
    if i > 0:
        previous_link = chapters[i - 1]["link"]

    next_link = None
    if i < len(chapters) - 1:
        next_link = chapters[i + 1]["link"]

    if previous_link is not None or next_link is not None:
        chapter["html"] += u"\n"

    if previous_link is not None:
        chapter["html"] += u"""\
<a href="{}">&lArr; Previous chapter</a>\
""".format(previous_link)

    if previous_link is not None and next_link is not None:
        chapter["html"] += u"&nbsp;" * 5

    if next_link is not None:
        chapter["html"] += u"""\
<a href="{}">Next chapter &rArr;</a>\
""".format(next_link)


##### Tasks ######################################


@task
def prepare():
    frontpage = CONFIG["MARKDOWN_FILES"][0]
    content = codecs.open(frontpage["file"], "r", "utf-8").read()
    # TODO Can I make this always go change the third line instead?
    # TODO And then go back and change it to "$$date$$" so that it
    # is not inadvertently committed to the git repo.
    today = unicode(datetime.datetime.now().strftime("%d %b %Y"))
    content = content.replace(u"$$date$$", today)
    with codecs.open(frontpage["file"], "w", "utf-8") as output:
        output.write(content)


@task
def html():
    """HTML5 output."""
    prepare()

    args = ["pandoc",
            "-f", "markdown",
            "-t", "html5",
            "-o", "{}.html".format(CONFIG["FULL_PROJECT_NAME"]),
            "-s",
            "--toc"] + [i["file"] for i in CONFIG["MARKDOWN_FILES"]]
    local(" ".join(args))
    local("open {}.html".format(CONFIG["FULL_PROJECT_NAME"]))


@task
def epub():
    """http://johnmacfarlane.net/pandoc/epub.html"""
    prepare()

    args = ["pandoc",
            "-f", "markdown",
            "-t", "epub",
            "-o", "{}.epub".format(CONFIG["FULL_PROJECT_NAME"])] + \
        [i["file"] for i in CONFIG["MARKDOWN_FILES"]]
    # TODO --epub-cover-image
    # TODO --epub-metadata
    # TODO --epub-stylesheet
    local(" ".join(args))
    if AWS_ENABLED:
        upload_output_to_s3("{}.epub".format(CONFIG["FULL_PROJECT_NAME"]))


@task
def pdf():
    """http://johnmacfarlane.net/pandoc/README.html#creating-a-pdf"""
    prepare()

    args = ["pandoc",
            "-f", "markdown",
            # https://github.com/jgm/pandoc/issues/571
            #"-t", "pdf",
            "-o", "{}.pdf".format(CONFIG["FULL_PROJECT_NAME"]),
            "-N",
            # https://github.com/jgm/pandoc/issues/600
            "-V", "papersize:\"a4paper\"",
            "--toc"] + [i["file"] for i in CONFIG["MARKDOWN_FILES"]]
    local(" ".join(args))
    if AWS_ENABLED:
        upload_output_to_s3("{}.pdf".format(CONFIG["FULL_PROJECT_NAME"]))


@task
def clean():
    """Remove generated output files"""
    possible_outputs = (
        "{}.html".format(CONFIG["FULL_PROJECT_NAME"]),
        "{}.epub".format(CONFIG["FULL_PROJECT_NAME"]),
        "{}.pdf".format(CONFIG["FULL_PROJECT_NAME"]),
    )

    for filename in possible_outputs:
        if os.path.exists(filename):
            os.remove(filename)
            print("Removed {}".format(filename))


@task
def push():
    """Upload Wordpress, EPUB, PDF."""
    clean()
    wp()
    epub()
    pdf()


########## WordPress ##########
## http://developer.wordpress.com/docs/api/ ##

@task
def oauth_step1():
    """Fetch OAuth2 token.

    http://developer.wordpress.com/docs/oauth2/"""
    if os.path.exists(OAUTH_CONFIG_FILE):
        os.remove(OAUTH_CONFIG_FILE)

    request_url = "https://public-api.wordpress.com/oauth2/authorize"
    params = {
        "client_id": WORDPRESS_CLIENT_ID,
        "redirect_uri": "http://swaroopch.com",
        "response_type": "code",
    }
    url = "{}?{}".format(request_url, urllib.urlencode(params))
    print("""\
1. After authorization, it will redirect, for e.g.
   http://swaroopch.com/?code=8D1Gq1tLQy&state
2. Extract the code from the URL and run:
   fab oauth_step2:8D1Gq1tLQy
3. See generated OAUTH_CONFIG_FILE file
""")
    try:
        proceed = raw_input("Proceed? (y/n) ")
        if proceed.lower().startswith("y"):
            webbrowser.open(url)
        else:
            abort("Okay, bye.")
    except SyntaxError:
        abort("Okay, bye.")


@task
def oauth_step2(code):
    """Use fetched token to generate OAuth access token."""
    request_url = "https://public-api.wordpress.com/oauth2/token"
    params = {
        "client_id": WORDPRESS_CLIENT_ID,
        "client_secret": WORDPRESS_CLIENT_SECRET,
        "code": code,
        "redirect_uri": "http://swaroopch.com",
        "grant_type": "authorization_code",
    }

    response = requests.post(request_url, data=params)
    response.raise_for_status()
    response = response.json()

    print(response)

    with codecs.open(OAUTH_CONFIG_FILE, "w", "utf-8") as output_file:
        json.dump(response, output_file, sort_keys=True, indent=2)


@task
def wp():
    """http://developer.wordpress.com/docs/api/"""
    if WORDPRESS_ENABLED:
        prepare()

        chapters = copy.deepcopy(CONFIG["MARKDOWN_FILES"])

        # header anchor id -> index in MARKDOWN_FILES
        all_headers = {}

        # Render html
        print("Rendering html")
        for (i, chapter) in enumerate(chapters):
            chapter_content = codecs.open(chapter["file"], "r", "utf-8").read()
            chapter["html"] = markdown_to_html(
                chapter_content,
                upload_assets_to_s3=AWS_ENABLED)

            collect_header_anchors(chapter, i, all_headers)

            chapter["link"] = "{}/{}/{}".format(
                WORDPRESS_BASE_URL,
                WORDPRESS_PARENT_PAGE_SLUG,
                chapter["slug"])

        # Fix cross-links
        for chapter in chapters:
            fix_links_to_other_chapters(chapter, chapters, all_headers)

        # Add previous and next links at end of html
        for (i, chapter) in enumerate(chapters):
            add_previous_next_links(chapter, i, chapters)

        # Fetch list of pages on the server and determine which already exist
        existing_pages = _wordpress_get_pages()
        page_slug_to_id = dict([(i.get("slug"), i.get("ID"))
                                for i in existing_pages])

        for chapter in chapters:
            if chapter["slug"] in page_slug_to_id:
                chapter["page_id"] = page_slug_to_id[chapter["slug"]]

        # Send to WP
        print("Uploading to WordPress")
        for chapter in chapters:
            if chapter["slug"] in page_slug_to_id:
                print("Existing page: {}".format(chapter["link"]))
                assert wordpress_edit_page(chapter["page_id"],
                                           chapter["title"],
                                           chapter["html"])
            else:
                print("New page: {}".format(chapter["link"]))
                assert wordpress_new_page(chapter["slug"],
                                          chapter["title"],
                                          chapter["html"])


def _wordpress_headers():
    assert WORDPRESS_ENABLED

    return {
        "Authorization": "Bearer {}".format(OAUTH_CONFIG["access_token"]),
    }


@retry
def _wordpress_get_pages():
    url = "https://public-api.wordpress.com/rest/v1/sites/{}/posts/"
    url = url.format(OAUTH_CONFIG["blog_id"])

    offset = 0
    number = 100
    posts = []

    while True:
        print("offset = {}".format(offset))
        response = requests.get(url,
                                params={"context": "edit",
                                        "type": "page",
                                        "status": "publish",
                                        "number": number,
                                        # TODO Use a proper category instead
                                        "search": "python_en",
                                        "offset": offset},
                                headers=_wordpress_headers())
        response.raise_for_status()
        new_posts = response.json()["posts"]
        posts.extend(new_posts)
        if len(new_posts) < number:
            break
        offset += 100

    return posts


@retry
def wordpress_new_page(slug, title, content):
    """Create a new Wordpress page."""
    url = "https://public-api.wordpress.com/rest/v1/sites/{}/posts/new"
    url = url.format(OAUTH_CONFIG["blog_id"])

    response = requests.post(url,
                             data={"slug": slug,
                                   "title": title,
                                   "content": content,
                                   "parent": WORDPRESS_PARENT_PAGE_ID,
                                   "type": "page",
                                   # TODO Use a proper category instead
                                   "tags": [CONFIG["FULL_PROJECT_NAME"]],
                                   "comments_open": False,
                                   "pings_open": False,
                                   "publicize": False},
                             headers=_wordpress_headers())
    response.raise_for_status()
    return response.json()


@retry
def wordpress_edit_page(post_id, title, content):
    """Edit a Wordpress page."""
    url = "https://public-api.wordpress.com/rest/v1/sites/{}/posts/{}"
    url = url.format(OAUTH_CONFIG["blog_id"], post_id)

    response = requests.post(url,
                             data={"title": title,
                                   "content": content,
                                   # TODO Use a proper category instead
                                   "tags": [CONFIG["FULL_PROJECT_NAME"]]},
                             headers=_wordpress_headers())
    response.raise_for_status()
    return response.json()
