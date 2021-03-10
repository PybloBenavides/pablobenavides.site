#!/usr/bin/env python
# -*- coding: utf-8 -*- #

import os
from pelican_jupyter import markup as nb_markup

MARKUP = ("md", "ipynb")
AUTHOR = 'Pablo Benavides'
SITENAME = 'Pablo Benavides'
SITEURL = ''

PATH = 'content'

TIMEZONE = 'Europe/Paris'

DEFAULT_LANG = 'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (('Pelican', 'https://getpelican.com/'),
         ('Python.org', 'https://www.python.org/'),
         ('Jinja2', 'https://palletsprojects.com/p/jinja/'),
         ('You can modify those links in your config file', '#'),)

# Social widget
# SOCIAL = (('You can add links in your config file', '#'),
#           ('Another social link', '#'),)

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
RELATIVE_URLS = True

'''
jupyter - pelican
'''


PLUGINS = [nb_markup]

IGNORE_FILES = [".ipynb_checkpoints"]
# IPYNB_SKIP_CSS=True
IPYNB_FIX_CSS = True
IPYNB_SKIP_CSS = False

IPYNB_STOP_SUMMARY_TAGS = [('div', ('class', 'input')), ('div', ('class', 'output')), ('h2', ('id', 'Header-2'))]
IPYNB_GENERATE_SUMMARY = True
dir_path = os.path.dirname(os.path.realpath(__file__))
IPYNB_EXPORT_TEMPLATE = os.path.join( dir_path, r"jupyter-pelican\templates\basic_jupyter.html")
'''
jupyter - pelican
'''

'''
MinimalXY Theme--------------------------------------------------------------------------------------------------------
'''
THEME = 'minimal_xy_theme'
# AUTHOR_INTRO = u'Hello world! I’m Pablo Benavides'
# AUTHOR_DESCRIPTION = u'Hello world! I’m John Doe. I use Python to make a more fluid traffic world'
# AUTHOR_AVATAR = 'images/logo_transparente.png'
# AUTHOR_WEB = 'https://pyblobenavides.github.io/pablobenavides.site/pages/portfolio.html'

# SOCIAL = (('github', 'https://github.com/PybloBenavides'),
#           ('linkedin','https://www.linkedin.com/in/pablo-benavides-0a5352116/'))

'''
MinimalXY Theme--------------------------------------------------------------------------------------------------------
'''
