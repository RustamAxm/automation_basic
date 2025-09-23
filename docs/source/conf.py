# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information
import os
import re
import sys
from datetime import datetime

from distutils.version import LooseVersion

from automation_basics import __version__

sys.path.insert(0, os.path.abspath("../.."))

project = "automation_basics"
copyright = f"{datetime.now().year}, Rustam Akhmadullin"
author = "Rustam Akhmadullin"
version = __version__

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration
extensions = [
    "sphinx.ext.napoleon",
    "sphinx.ext.intersphinx",
    "sphinx.ext.autodoc",
    "sphinx_automodapi.automodapi",
    "sphinx.ext.mathjax",
    "sphinx.ext.viewcode",
    "sphinx_simplepdf",
]
autoclass_content = "both"
simplepdf_vars = {
    "primary": "#1e94ff",
    "secondary": "#379683",
    "cover": "#ffffff",
    "white": "#ffffff",
    "links": "#1e94ff",
    "cover-bg": "url(cover-bg.jpg) no-repeat center",
    "cover-overlay": "#1e94ff",
    "top-left-content": "counter(page)",
    "bottom-center-content": '"Custom footer content"',
}

templates_path = ["_templates"]
exclude_patterns = []

language = "Python"

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = "sphinx_rtd_theme"
html_static_path = ["_static"]


def create_versions():
    import git

    repo = git.Repo("../..")
    tmp_tags = []
    for tag in repo.tags:
        m = re.search(r"\d+(\.\d+){1,3}", f"{tag}")
        if m:
            ver = m[0]
            tmp_tags.append(ver)
    tags = sorted(set(tmp_tags), key=LooseVersion)
    tmp = []
    root_docs_url = "."
    for tag in tags:
        tmp.append([f"{tag}", f"{root_docs_url}/{tag}/docs/"])
    return tmp


versions = create_versions()
html_context = {
    "current_version": version,
    "versions": create_versions(),
    "current_language": "en",
    "languages": [["en", "link to en"], ["de", "link to de"]],
}

autodoc_mock_imports = ["smbus3", "smbus2", "serial", "RPi", "ftd2xx"]
