#!/usr/bin/env python

# This file is only used if you use `make publish` or
# explicitly specify it as your config file.

import os
import sys
sys.path.append(os.curdir)
from pelicanconf import *

# Para producción
SITEURL = 'https://movimientolibre.com'
RELATIVE_URLS = False

# Feed generation
FEED_DOMAIN = SITEURL
FEED_ALL_ATOM = 'feeds/all.atom.xml'
FEED_ALL_RSS = 'feeds/all.rss.xml'
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None
CATEGORY_FEED_ATOM = None
CATEGORY_FEED_RSS = None
TAG_FEED_ATOM = None
TAG_FEED_RSS = None
TRANSLATION_FEED_ATOM = None
TRANSLATION_FEED_RSS = None

# Feed options
FEED_MAX_ITEMS = 24
RSS_FEED_SUMMARY_ONLY = True

# Paginacion
DEFAULT_PAGINATION = True
DEFAULT_PAGINATION = 16
DEFAULT_ORPHANS = 2

# Plugins, disabled: 'articles_lists_json'
PLUGINS = ['pelican_javascript', 'sitemap']

# Plugin sitemap
SITEMAP = {
    'format': 'xml',
    'priorities': {
        'articles': 1,
        'indexes': 0.5,
        'pages': 1,
    },
    'changefreqs': {
        'articles': 'weekly',
        'indexes': 'daily',
        'pages': 'monthly',
    },
    'exclude': [
        'archives.html',
        'tags.html',
        'categories.html',
        'author/',
    ],
}

# Habilitar los servicios de terceros, como Google Analytics y Search
USE_REMOTE_SERVICES = True
