# Sphinx configuration for RMTDataPro documentation

import os
import shutil
import sys

sys.path.insert(0, os.path.abspath("."))

# -- Project information -----------------------------------------------------
project = "RMTDataPro"
copyright = "2026, Wang Peijie"
author = "Wang Peijie"
version = "0.1"
release = "0.1.0"

# -- General configuration ---------------------------------------------------
extensions = [
    "myst_parser",
    "sphinx.ext.intersphinx",
    "sphinx.ext.viewcode",
    "sphinx_sitemap",
    "sphinxcontrib.mermaid",
]

templates_path = ["_templates"]
exclude_patterns = ["_build", "Thumbs.db", ".DS_Store"]

# -- Options for HTML output -------------------------------------------------
html_theme = "sphinx_rtd_theme"
html_theme_options = {
    "logo_only": False,
    "prev_next_buttons_location": "bottom",
    "style_external_links": False,
    "collapse_navigation": True,
    "sticky_navigation": True,
    "navigation_depth": 4,
    "includehidden": True,
    "titles_only": False,
}

# -- Language configuration ----------------------------------------------------
language = "zh-CN"

html_copy_source = False

html_baseurl = "https://emwpj.github.io/RMTDataPro-docs/"
sitemap_url_scheme = "https"

# -- Highlight configuration -------------------------------------------------
highlight_language = "none"
highlight_options = {"hl_lines": []}

# -- MyST configuration ------------------------------------------------------
myst_enable_extensions = [
    "amsmath",
    "dollarmath",
    "colon_fence",
    "deflist",
    "tasklist",
    "linkify",
]

myst_heading_anchors = 3
myst_fence_as_directive = ["mermaid"]

# -- Intersphinx configuration -----------------------------------------------
intersphinx_mapping = {
    "python": ("https://docs.python.org/3", None),
    "numpy": ("https://numpy.org/doc/stable/", None),
}

# -- Mermaid configuration ---------------------------------------------------
mermaid_output_format = "svg"
mermaid_versions = "latest"
# On Windows, use just "mmdc" (no path) because:
# 1) shell=True is required to run .CMD files
# 2) shlex.split() mangles backslash paths when shell=True
# 3) With shell=True, mmdc is found via PATH
mermaid_cmd = "mmdc"
mermaid_cmd_shell = "true"  # string "true" to match expected type

# -- Sphinx sitemap configuration --------------------------------------------
sphinx_sitemap_conf = {
    "sitemap_url_scheme": sitemap_url_scheme,
}

# -- Source file suffix ------------------------------------------------------
source_suffix = ".md"

# -- The master toctree document -------------------------------------------
master_doc = "index"
