# Configuration file for the Sphinx documentation builder.
#
# This file only contains a selection of the most common options. For a full
# list see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Path setup --------------------------------------------------------------

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#
# import os
# import sys
# sys.path.insert(0, os.path.abspath('.'))


# -- Project information -----------------------------------------------------
import sphinx_rtd_theme
import time  ###

project = '7-inch Touch Screen'
copyright = f'{time.localtime().tm_year}, SunFounder'  ###
author = 'www.sunfounder.com'


# -- General configuration ---------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.

extensions = [
    'sphinx.ext.autosectionlabel',
    'sphinx_copybutton',
    'sphinx_rtd_theme',
]

# -- sphinx_rtd_theme Theme options -----------------------------------------------------
html_theme_options = {
    'flyout_display': 'attached'
}

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = []


# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
html_theme = 'sphinx_rtd_theme'
html_theme_path = [sphinx_rtd_theme.get_html_theme_path()]


html_js_files = [
    'https://ezblock.cc/readDocFile/custom.js',
]
html_css_files = [
    'https://ezblock.cc/readDocFile/custom.css',
]

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['_static']

language = 'en'
locale_dirs = ['locale/'] 

# open link in a new window

rst_epilog = """

.. |link_sf_facebook| raw:: html

    <a href="https://bit.ly/raphaelkit" target="_blank">here</a>

.. |link_pc_monitor| raw:: html

    <a href="https://www.sunfounder.com/blogs/news/raspberry-pi-system-monitor-for-pc-enhancing-performance-and-remote-monitoring" target="_blank">PC monitoring device</a>

.. |link_7inch_Touch_Screen| raw:: html

    <a href="https://www.sunfounder.com/products/7inch-capacitive-touchscreen?_pos=9&_sid=fdce84a78&_ss=r" target="_blank">Purchase Link for TS-7C 7-inch Touch Screen</a>

.. |link_TS7C_7inch_Touch_Screen| raw:: html

    <a href="https://www.sunfounder.com/products/7inch-capacitive-touchscreen?_pos=9&_sid=fdce84a78&_ss=r" target="_blank">TS-7C 7-inch Touch Screen</a>

"""


