#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'Swapan Rajdev'
SITENAME = u'Swapan Rajdev'
SITEURL = ''

TIMEZONE = 'US/Pacific'

DEFAULT_LANG = u'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None

# Content
PATH = 'content'
PAGE_DIR = 'pages'
ARTICLE_DIR = 'articles'
STATIC_PATHS = ['images']
ARTICLE_URL = ('articles/{slug}/')
ARTICLE_SAVE_AS = ('articles/{slug}/index.html')
PAGE_URL = 'pages/{slug}' 
PAGE_SAVE_AS = 'pages/{slug}.html'
AUTHOR_URL = 'author/{slug}'
AUTHOR_SAVE_AS = 'author/{slug}.html'
CATEGORY_URL = 'category/{slug}'
CATEGORY_SAVE_AS = 'category/{slug}.html'
TAG_URL = 'tag/{slug}'
TAG_SAVE_AS = 'tag/{slug}.html'

# Theme.
THEME = './theme/pure'
COVER_IMG_URL = '/images/coffee_mug.jpg'
TAGLINE = 'My blog'
TYPOGRIFY = True
DEFAULT_PAGINATION = 10

MENUITEMS = (
    ('About', 'pages/about'),
)

PLUGIN_PATH = './plugins'
PLUGINS = ['gravatar', 'disqus_static', 'optimize_images']

DISQUS_SITENAME = u'srajdev'
DISQUS_SECRET_KEY = u'v8elbrW1aNxbOQJ0yC9G6QXic9KM43fHYcQ5JUshxZsXmkzQV4ycRpsmQW4A20pk'
DISQUS_PUBLIC_KEY = u'J3JMMBYHyHfGpPjiRwp01IPb8WwRYNzzcbF64QChO1dsprKpfk4n31bV38gSUEU5'

# Blogroll
#LINKS =  (('Pelican', 'http://getpelican.com/'),
#          ('Python.org', 'http://python.org/'),
#          ('Jinja2', 'http://jinja.pocoo.org/'),
#          ('You can modify those links in your config file', '#'),)

# Social widget
SOCIAL = (('Twitter', 'https://twitter.com/srajdev'),
          ('LinkedIn', 'http://www.linkedin.com/pub/swapan-rajdev/1a/59/64a'),)

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True
