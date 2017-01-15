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
	'http://cdnjs.cloudflare.com/ajax/libs/jquery-easing/1.3/jquery.easing.min.js',
	'classie.js',
	'cbpAnimatedHeader.js',
	'jqBootstrapValidation.js',
	'contact_me.js',
	'freeagent.js'
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
	('#contact', 'Kontakt')
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

ADDRESS1 = 'Leirfenvegen 10'
ADDRESS2 = '4355 Kvernaland'
# Left column
ABOUT_LEFT = 'Take me to your leader! Switzerland is small and neutral! We are more like Germany, ambitious and misunderstood! I\'m Santa Claus! And so we say goodbye to our beloved pet, Nibbler, who\'s gone to a place where I, too, hope one day to go. The toilet.</p><p>Wow, you got that off the Internet? In my day, the Internet was only used to download pornography. <strong> I meant \'physically\'.</strong> <em> Look, perhaps you could let me work for a little food?</em> I could clean the floors or paint a fence, or service you sexually?</p><h3>Guess again.</h3>'
# Right column
ABOUT_RIGHT = '<p>It\'s a fez. I wear a fez now. Fezes are cool. You know how I sometimes have really brilliant ideas? You know when grown-ups tell you \'everything\'s going to be fine\' and you think they\'re probably lying to make you feel better?</p><p>You hate me; you want to kill me! Well, go on! Kill me! KILL ME! It\'s art! A statement on modern society, \'Oh Ain\'t Modern Society Awful? \'! <strong> All I\'ve got to do is pass as an ordinary human being.</strong> <em> Simple.</em> What could possibly go wrong?</p><p>Father Christmas. Santa Claus. Or as I\'ve always known him: Jeff.</p>'
# Center
ABOUT_CENTER = '<a href="https://www.facebook.com/vifortellerdinhistorie/?fref=ts" target="_blank" class="btn btn-lg btn-outline"><i class="fa fa-download">Møt oss på facebook</i> </a>'

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True
