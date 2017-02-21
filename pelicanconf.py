#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

THEME='../theme'

AUTHOR = u'Svein F. Hestvaag'
SITENAME = u'Popkornet'
SITESUBTITLE = u'Alle har en historie å fortelle.<br/>Popkornet hjelper deg å fortelle din.'
SITEURL = ''
LOAD_CONTENT_CACHE=False
THEME_STATIC_DIR = 'static'
PATH = 'content'
STATIC_PATHS = [ 'images','mail','js', 'css', 'fonts']
EXTRA_PATH_METADATA = {
    'static/images/portfolio': {'path': 'images/portfolio'},
    }

TIMEZONE = 'Europe/Paris'

DEFAULT_DATE=u'fs'
DEFAULT_LANG = u'no'
BOOTSTRAP_FILE = 'bootstrap.css'
CSS_FILE = 'popkornet.css'
FONTS = 'fonts'
SCRIPTS = [
	'jquery-1.11.0.js',
	'bootstrap.min.js',
	'https://cdnjs.cloudflare.com/ajax/libs/jquery-easing/1.3/jquery.easing.min.js',
	'classie.js',
	'cbpAnimatedHeader.js',
	'jqBootstrapValidation.js',
	'contact_me.js',
	'popkornet.js'
]
# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

DIRECT_TEMPLATES = ['index']

# Top Menu Links
NAVLINKS = (
	('#page-top', ''),
	('#portfolio', 'Bøker'),
	('#about', 'Om'),
	('#contact', 'Bokidé?')
)

# Portfolio Name
PORTFOLIO = 'Bøker'

#Contact form fields sorted by: label, input_type, id, required_validation_,msg
CONTACT_FIELDS = (
	['Navn', 'text', 'name', 'Please enter your name.'],
	['E-mailadresse', 'email', 'email','Please enter your email address.' ],
	['Telefonnummer', 'tel', 'phone', 'Please enter your phone number.'],
	['Beskjed', 'textarea', 'message', 'Please enter a message.']
)
FORMSPREEURL = 'https://formspree.io/gullstrek+popkornet@gmail.com'
ADDRESS1 = 'Leirfenvegen 10'
ADDRESS2 = '4355 Kvernaland'
# Center
ABOUT_CENTER = '<a href="https://www.facebook.com/vifortellerdinhistorie/?fref=ts" target="_blank" class="btn btn-lg btn-outline"><i class="fa fa-download"> Ta kontakt på facebook</i> </a>'

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True
