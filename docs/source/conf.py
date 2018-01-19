#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# Matrix Python SDK documentation build configuration file, created by
# sphinx-quickstart on Tue May  3 14:25:58 2016.
#
# This file is execfile()d with the current directory set to its
# containing dir.
#
# Note that not all possible configuration values are present in this
# autogenerated file.
#
# All configuration values have a default; values that are commented out
# serve to show the default.

import sys
import os
import sphinx_rtd_theme


srcdir = os.path.abspath('../../')
sys.path.insert(0, srcdir)


# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
# sys.path.insert(0, os.path.abspath('.'))

# -- General configuration ------------------------------------------------

# If your documentation needs a minimal Sphinx version, state it here.
needs_sphinx = '1.3'

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
    'sphinx.ext.viewcode',
    'sphinx.ext.autodoc',
    'sphinx.ext.napoleon'
]

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# The suffix(es) of source filenames.
# You can specify multiple suffix as a list of string:
# source_suffix = ['.rst', '.md']
source_suffix = '.rst'

# The encoding of source files.
# source_encoding = 'utf-8-sig'

# The master toctree document.
master_doc = 'index'

# General information about the project.
project = 'Matrix Python SDK'
copyright = '2016, matrix.org'
author = 'matrix.org'


version = '0.0.5'
release = '0.0.5'

language = None

exclude_patterns = []

pygments_style = 'sphinx'

todo_include_todos = False

html_theme = "sphinx_rtd_theme"
html_theme_path = [sphinx_rtd_theme.get_html_theme_path()]
html_title = 'Matrix Python SDK v' + version
# html_static_path = ['_static']

htmlhelp_basename = 'MatrixPythonSDKdoc'
highlight_language = 'python'

latex_documents = [
    (master_doc, 'MatrixPythonSDK.tex', 'Matrix Python SDK Documentation',
     'matrix.org', 'manual'),
]

man_pages = [
    (master_doc, 'matrixpythonsdk', 'Matrix Python SDK Documentation',
     [author], 1)
]

texinfo_documents = [
    (master_doc, 'MatrixPythonSDK', 'Matrix Python SDK Documentation',
     author, 'MatrixPythonSDK', 'SDK for writing Matrix Clients in Python',
     'Miscellaneous'),
]
