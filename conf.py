# -*- coding: utf-8 -*-
#
import os
import sys

import sphinx_rtd_theme
from recommonmark.parser import CommonMarkParser

sys.path.insert(0, os.path.abspath('..'))
sys.path.append(os.path.dirname(__file__))
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "readthedocs.settings.dev")

from django.conf import settings

import django
django.setup()

sys.path.append(os.path.abspath('_ext'))
extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.intersphinx',
    'sphinxcontrib.httpdomain',
    'djangodocs',
    'doc_extensions',
]
templates_path = ['_templates']

source_suffix = ['.rst']
source_parsers = {
    '.md': CommonMarkParser,
}

master_doc = 'index'
project = u'Read the Docs'
copyright = u'2010-2017, Read the Docs, Inc & contributors'
version = '1.0'
release = '1.0'
exclude_patterns = ['_build']
default_role = 'obj'
pygments_style = 'sphinx'
intersphinx_mapping = {
    'python': ('http://python.readthedocs.io/en/latest/', None),
    'django': ('http://django.readthedocs.io/en/1.8.x/', None),
    'sphinx': ('http://sphinx.readthedocs.io/en/latest/', None),
}

exclude_patterns = [
    # 'api' # needed for ``make gettext`` to not die.
]

language = 'en'

locale_dirs = [
    'locale/',
]
gettext_compact = False

html_theme = 'sphinx_rtd_theme'
html_static_path = ['_static']
html_theme_path = [sphinx_rtd_theme.get_html_theme_path()]


def setup(app):
    app.add_stylesheet('stylesheet.css')
