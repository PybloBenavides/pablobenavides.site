#!/usr/bin/env python
# -*- coding: utf-8 -*- #

# This file is only used if you use `make publish` or
# explicitly specify it as your config file.

import os
import sys
sys.path.append(os.curdir)
from pelicanconf import *

# If your site is available via HTTPS, make sure SITEURL begins with https://
# SITEURL = 'https://pyblobenavides.github.io/pablobenavides.site' #Hay que dejar esto asi y solo tocar el cname
SITEURL = 'http://pablobenavides.site'
RELATIVE_URLS = True #ESto se queda asi tambien

FEED_ALL_ATOM = 'feeds/all.atom.xml'
CATEGORY_FEED_ATOM = 'feeds/{slug}.atom.xml'

DELETE_OUTPUT_DIRECTORY = True

# Following items are often useful when publishing

DISQUS_SITENAME = "pablobenavides-site"
GOOGLE_ANALYTICS = 'G-DLMRN2NQ83'