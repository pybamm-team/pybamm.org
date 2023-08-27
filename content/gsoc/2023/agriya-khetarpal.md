---
title: "Agriya Khetarpal — Google Summer of Code 2023 Final Report"
subtitle: "PyBaMM - Documentation"
summary: "This is the final report for Agriya Khetarpal's Google Summer of Code 2023 project with PyBaMM, NumFOCUS. I worked on improving the documentation infrastructure for PyBaMM."
date: 2023-08-22
shortcutDepth: 2
# WARNING: THE LINK TO THIS PAGE SHOULD NEVER BE CHANGED WITHOUT THE EXISTENCE OF A HUGO PERMALINK, AN ALIAS IN THE FRONTMATTER, OR WITHOUT THE EXISTENCE OF A PERMANENT (STATUS CODE 301) REDIRECTION RULE IN THE _redirects FILE AND A CORRESPONDING ENTRY IN THE netlify.toml FILE. THIS IS TO ENSURE THAT THE LINK TO THIS PAGE IS NEVER BROKEN SINCE IT ACCOUNTS FOR AGRIYA KHETARPAL'S GSoC 2023 FINAL REPORT AND IS LINKED TO FROM THE GOOGLE SUMMER OF CODE WEBSITE AS THE WORK PRODUCT SUBMISSION.
---

[![Google Summer of Code](https://img.shields.io/badge/Google_Summer_of_Code-2023-fbbd05?colorA=565656&logo=data:image/svg+xml;base64,PD94bWwgdmVyc2lvbj0iMS4wIiBlbmNvZGluZz0idXRmLTgiPz4KPCEtLSBHZW5lcmF0b3I6IEFkb2JlIElsbHVzdHJhdG9yIDE5LjIuMSwgU1ZHIEV4cG9ydCBQbHVnLUluIC4gU1ZHIFZlcnNpb246IDYuMDAgQnVpbGQgMCkgIC0tPgo8c3ZnIHZlcnNpb249IjEuMSIgaWQ9IkxheWVyXzExIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHhtbG5zOnhsaW5rPSJodHRwOi8vd3d3LnczLm9yZy8xOTk5L3hsaW5rIiB4PSIwcHgiIHk9IjBweCIKCSB2aWV3Qm94PSIwIDAgMTkyIDE5MiIgc3R5bGU9ImVuYWJsZS1iYWNrZ3JvdW5kOm5ldyAwIDAgMTkyIDE5MjsiIHhtbDpzcGFjZT0icHJlc2VydmUiPgo8c3R5bGUgdHlwZT0idGV4dC9jc3MiPgoJLnN0MHtmaWxsOiNGQkJDMDU7fQo8L3N0eWxlPgo8Zz4KCTxwYXRoIGNsYXNzPSJzdDAiIGQ9Ik0xNTguMSwzMy43aC0zNi40TDk2LDhMNzAuMywzMy43SDMzLjl2MzYuNEw4LjIsOTUuOWwyNS43LDI1LjdWMTU4aDM2LjRMOTYsMTgzLjdsMjUuNy0yNS43aDM2LjR2LTM2LjQKCQlsMjUuNy0yNS43bC0yNS43LTI1LjdWMzMuN3ogTTE1OC43LDk1LjljMCwzNC42LTI4LjEsNjIuNy02Mi43LDYyLjdzLTYyLjctMjguMS02Mi43LTYyLjdTNjEuNCwzMy4yLDk2LDMzLjIKCQlTMTU4LjcsNjEuMywxNTguNyw5NS45eiIvPgoJPHBhdGggY2xhc3M9InN0MCIgZD0iTTk2LDQxLjJjLTMwLjIsMC01NC43LDI0LjUtNTQuNyw1NC43YzAsMzAuMiwyNC41LDU0LjcsNTQuNyw1NC43YzMwLjIsMCw1NC43LTI0LjUsNTQuNy01NC43CgkJQzE1MC43LDY1LjcsMTI2LjIsNDEuMiw5Niw0MS4yeiBNNzkuOSw3NS42djlMNjUuNCw5NS45bDE0LjUsMTEuM3Y5bC0xLTAuN0w1Ny40LDk4LjdMNTYsOTcuNnYtMy40bDEuNC0xLjFsMjEuNS0xNi43TDc5LjksNzUuNgoJCUw3OS45LDc1LjZ6IE0xMDUuNyw3MC40TDkzLjgsMTIzbC0wLjEsMC40aC03LjRsMC40LTJsMTEuOS01Mi41bDAuMS0wLjRoNy40TDEwNS43LDcwLjR6IE0xMzYsOTcuNmwtMS40LDEuMUwxMTMsMTE1LjRsLTEsMC43di05CgkJbDE0LjUtMTEuM2wtMTQuNS0xMS4zdi05djBsMSwwLjdMMTM0LjUsOTNsMS40LDEuMVY5Ny42eiIvPgo8L2c+Cjwvc3ZnPgo=)](https://g.co/gsoc)
[![NumFOCUS](https://img.shields.io/badge/organisation-NumFOCUS-orange.svg?style=flat&colorA=007D8A&colorB=E1523D&logo=data:image/png;base64,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)](https://numfocus.org)
[![PyBaMM](https://img.shields.io/badge/sub%E2%80%93organisation-PyBaMM-blue?logo=data:image/svg+xml;base64,PHN2ZyBpZD0iTGF5ZXJfMSIgZGF0YS1uYW1lPSJMYXllciAxIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHhtbG5zOnhsaW5rPSJodHRwOi8vd3d3LnczLm9yZy8xOTk5L3hsaW5rIiB2aWV3Qm94PSIwIDAgMTc0IDIwMCI+PGRlZnM+PHN0eWxlPi5jbHMtMXtmaWxsOnVybCgjbGluZWFyLWdyYWRpZW50KTt9LmNscy0ye2ZpbGw6dXJsKCNsaW5lYXItZ3JhZGllbnQtMik7fS5jbHMtM3tmaWxsOiMyNDRmNzI7fS5jbHMtNHtmaWxsOnVybCgjbGluZWFyLWdyYWRpZW50LTMpO30uY2xzLTV7ZmlsbDp1cmwoI2xpbmVhci1ncmFkaWVudC00KTt9LmNscy02e2ZpbGw6dXJsKCNsaW5lYXItZ3JhZGllbnQtNSk7fS5jbHMtN3tmaWxsOnVybCgjbGluZWFyLWdyYWRpZW50LTYpO308L3N0eWxlPjxsaW5lYXJHcmFkaWVudCBpZD0ibGluZWFyLWdyYWRpZW50IiB4MT0iNDguMDMiIHkxPSI0Ny41IiB4Mj0iMTc3LjkzIiB5Mj0iMTIyLjUiIGdyYWRpZW50VW5pdHM9InVzZXJTcGFjZU9uVXNlIj48c3RvcCBvZmZzZXQ9IjAiIHN0b3AtY29sb3I9IiNmZmQ0M2IiLz48c3RvcCBvZmZzZXQ9IjEiIHN0b3AtY29sb3I9IiNmZmU4NzMiLz48L2xpbmVhckdyYWRpZW50PjxsaW5lYXJHcmFkaWVudCBpZD0ibGluZWFyLWdyYWRpZW50LTIiIHgxPSIxMy4zOSIgeTE9IjY3LjUiIHgyPSIxNDMuMjkiIHkyPSIxNDIuNSIgeGxpbms6aHJlZj0iI2xpbmVhci1ncmFkaWVudCIvPjxsaW5lYXJHcmFkaWVudCBpZD0ibGluZWFyLWdyYWRpZW50LTMiIHgxPSIwLjQiIHkxPSIxMjUiIHgyPSI4NyIgeTI9IjEyNSIgZ3JhZGllbnRVbml0cz0idXNlclNwYWNlT25Vc2UiPjxzdG9wIG9mZnNldD0iMCIgc3RvcC1jb2xvcj0iIzMwNjk5OCIvPjxzdG9wIG9mZnNldD0iMSIgc3RvcC1jb2xvcj0iIzRiOGJiZSIvPjwvbGluZWFyR3JhZGllbnQ+PGxpbmVhckdyYWRpZW50IGlkPSJsaW5lYXItZ3JhZGllbnQtNCIgeDE9IjE2OS4yNyIgeTE9IjU3LjUiIHgyPSI3NC4wMSIgeTI9IjIuNSIgZ3JhZGllbnRVbml0cz0idXNlclNwYWNlT25Vc2UiPjxzdG9wIG9mZnNldD0iMCIgc3RvcC1jb2xvcj0iIzZmYTJjYiIvPjxzdG9wIG9mZnNldD0iMSIgc3RvcC1jb2xvcj0iIzRiOGJiZSIvPjwvbGluZWFyR3JhZGllbnQ+PGxpbmVhckdyYWRpZW50IGlkPSJsaW5lYXItZ3JhZGllbnQtNSIgeDE9IjEzNC42MyIgeTE9Ijc3LjUiIHgyPSIzOS4zNyIgeTI9IjIyLjUiIHhsaW5rOmhyZWY9IiNsaW5lYXItZ3JhZGllbnQtNCIvPjxsaW5lYXJHcmFkaWVudCBpZD0ibGluZWFyLWdyYWRpZW50LTYiIHgxPSI5OS45OSIgeTE9Ijk3LjUiIHgyPSI0LjczIiB5Mj0iNDIuNSIgeGxpbms6aHJlZj0iI2xpbmVhci1ncmFkaWVudC00Ii8+PC9kZWZzPjxwb2x5Z29uIGNsYXNzPSJjbHMtMSIgcG9pbnRzPSIxNTYuMjggMTYwIDY5LjY4IDExMCA2OS42OCAxMCAxNTYuMjggNjAgMTU2LjI4IDE2MCIvPjxwb2x5Z29uIGNsYXNzPSJjbHMtMiIgcG9pbnRzPSIxMjEuNjQgMTgwIDM1LjA0IDEzMCAzNS4wNCAzMCAxMjEuNjQgODAgMTIxLjY0IDE4MCIvPjxwb2x5Z29uIGNsYXNzPSJjbHMtMyIgcG9pbnRzPSIxNTYuMjggMTYwIDE1Ni4yOCA2MCAxNzMuNiA1MCAxNzMuNiAxNTAgMTU2LjI4IDE2MCIvPjxwb2x5Z29uIGNsYXNzPSJjbHMtMyIgcG9pbnRzPSIxMjEuNjQgMTgwIDEyMS42NCA4MCAxMzguOTYgNzAgMTM4Ljk2IDE3MCAxMjEuNjQgMTgwIi8+PHBvbHlnb24gY2xhc3M9ImNscy0zIiBwb2ludHM9Ijg3IDIwMCA4NyAxMDAgMTA0LjMyIDkwIDEwNC4zMiAxOTAgODcgMjAwIi8+PHBvbHlnb24gY2xhc3M9ImNscy00IiBwb2ludHM9Ijg3IDIwMCAwLjQgMTUwIDAuNCA1MCA4NyAxMDAgODcgMjAwIi8+PHBvbHlnb24gY2xhc3M9ImNscy01IiBwb2ludHM9IjY5LjY4IDEwIDE1Ni4yOCA2MCAxNzMuNiA1MCA4NyAwIDY5LjY4IDEwIi8+PHBvbHlnb24gY2xhc3M9ImNscy02IiBwb2ludHM9IjM1LjA0IDMwIDEyMS42NCA4MCAxMzguOTYgNzAgNTIuMzYgMjAgMzUuMDQgMzAiLz48cG9seWdvbiBjbGFzcz0iY2xzLTciIHBvaW50cz0iMC40IDUwIDg3IDEwMCAxMDQuMzIgOTAgMTcuNzIgNDAgMC40IDUwIi8+PC9zdmc+Cg==)](https://pybamm.org)

[![Blogs](https://img.shields.io/badge/blogs-dev.to-0A0A0A?style=flat&logo=devdotto&logoColor=white&colorA=blue)](https://dev.to/agriyakhetarpal)
[![Project page on the Google Summer of Code website](https://img.shields.io/badge/%20view%20project%20-darkmagenta)](https://summerofcode.withgoogle.com/archive/2023/projects/DdcerdTx)
[![Proposal on Google Docs](https://img.shields.io/badge/%20view%20proposal%20-palevioletred)](https://docs.google.com/document/d/1JDLxmU8Qou9i38vJrJ-HmG-89xTMcF9CoRbu9tHz-3Q/)

<br>

[![View my Twitter profile](https://img.shields.io/badge/Twitter-1DA1F2?style=flat&logo=twitter&logoColor=white)](https://twitter.com/agriyakhetarpal)
[![View my GitHub profile](https://img.shields.io/badge/GitHub-100000?style=flat&logo=github&logoColor=white)](https://github.com/agriyakhetarpal)
[![View my LinkedIn profile](https://img.shields.io/badge/LinkedIn-0077B5?style=linkedin&logo=linkedin&logoColor=white)](https://linkedin.com/in/agriyakhetarpal)

---

This page serves as a permalink to the final report that provides details of Agriya Khetarpal’s project in the Google Summer of Code 2023 programme.

## 📖 TL;DR

A summary of some of the tasks I achieved throughout the community bonding and the coding periods is given below.

- A revamped static PyBaMM website, at https://pybamm.org
- Documentation infrastructure improvements with Sphinx extensions and new functionality to make it more robust, readable, and maintainable
- Various improvements to the general infrastructure, DevOps-related issues, and repository maintenance-related tasks: tweaks to the CI/CD pipelines, issues related to the migration of the test suite from `tox` to `nox`, caching dependencies for speed-ups in the jobs matrices, removing unused dependencies, addressing deprecations, and more
- Some features integrated into the core PyBaMM functionality

## 🔋 About PyBaMM

PyBaMM is an open-source Python package for the mathematical modelling of batteries and running fast, flexible, and accurate simulations for myriads of battery models. Its mission is to accelerate battery modelling research by providing open-source tools for multi-institutional, interdisciplinary collaboration; it is fiscally sponsored by NumFOCUS and The Faraday Institution in the U.K. The use of the software in academia and industry has been prolific since its inception—it has been used at a multitude of universities, research institutions, and commercial research labs in collaborative settings.

## 📄 Project abstract

This project aims to enhance the documentation infrastructure for PyBaMM and consolidate all of it in one place, which includes but will not be limited to: the API documentation, user guides, the example Jupyter notebooks, and the PyBaMM Wiki. This project will also introduce a new pybamm.org website with the Hugo static site generator, and improvements to the existing documentation built with Sphinx – based on other popular Python packages and libraries in order to make it more robust and maintainable.

### 🚀 Motivation

A robust and up-to-date documentation infrastructure is essential to PyBaMM’s development and usage as the package transitions into a modern, open-source software suite to model battery simulations and provide unparalleled flexibility to its end users. It will help not only future contributors and maintainers but also users across various domains involved in the battery science ecosystem.

### 🍀 Benefits to the community

My work shall make it convenient to maintain an ever-expanding documentation resource by implementing a series of both short and major quality-of-life improvements to prettify it, and by adding new features that have been requested in the past. The aim is to make it easier not only for users and learners of PyBaMM but also for new contributors towards its development in the future.

## 🧑‍💻 Work done

### ⚡️ A new website for PyBaMM

PyBaMM has received a revamp on the realms of the internet—the new static website can be accessed on the same domain as the previous one: at https://pybamm.org. It uses the Scientific Python theme for Hugo and Netlify for the deployment infrastructure and is inspired by the NumPy and the SciPy websites. The content is written in `Markdown` syntax. The pages of the website comprise but are not limited to: a homepage, an about page, a teams page to list maintainers and contributors, the governance and roadmap pages, a GSoC page, a newsroom, and more. The site has an impeccable SEO score and is WCAG-compliant on most pages and elements as much as it is possible without significant alterations to the theme itself.

The website incorporates a Makefile to be used with `make` as a task runner. The CI includes workflows for linting and autoformatting, and for updating the teams page at https://pybamm.org/teams/ weekly via the GitHub API.

The pinned summary issue lists all the tasks that were pursued in the form of issues and the pull requests that tracked them, as a part of getting the website ready for deployment: https://github.com/pybamm-team/pybamm.org/issues/6/

### 🚇 Documentation infrastructure improvements

1. A custom domain was added on Read the Docs, so the documentation hosted on https://pybamm.readthedocs.io now redirects to and can be accessed at https://docs.pybamm.org.

2. PyBaMM uses a citation file to keep track of relevant papers for battery models and parameter sets. With the `sphinxcontrib-bibtex` extension; the CITATIONS.bib file can be parsed to extract references from it, and the directives provided such as `:footcite:t:` and `.. footbibliography::` are used to display all references on a page programmatically. This eliminates the possibilities of errors in spelling and BibTeX validation errors.

3. Pages now display when they were last updated in the docs via the `sphinx-last-updated-by-git` Sphinx extension.

4. Added configuration for multithreaded documentation builds to speed up the documentation builds locally.

5. Added `nbsphinx` to display and render Jupyter notebooks and their galleries with `sphinx-gallery`: it was used as a Sphinx extension to convert `.ipynb` files to `.rst` format that can be parsed by Sphinx’s HTML builder. The notebooks can be viewed in a gallery format on the [Examples page](https://docs.pybamm.org/en/latest/source/examples) of the website. Functionality was added such that each notebook can be separately downloaded from the website itself or opened in Google Colab from the `main` or the `develop` branches. Similarly, the example scripts will soon be incorporated in the form of a thumbnail gallery on the same page.

6. Added floating window tooltips for cross-references in the docs using the `sphinx-hoverxref` extension, which enables external tooltips for classes, methods, and self-contained links inside the documentation and references `intersphinx` inventories for external links. Users can hover over a link to display the contents of the link.

7. Inheritance diagrams to display class hierarchies for models and submodels: PyBaMM ships with an extensive library of models and submodels for various battery chemistries—such as lithium-ion models, lead-acid models, and more. The `sphinx.ext.inheritance_diagram` extension was added and customised through a custom extension in the `docs/sphinxext/` folder that automatically creates inheritance diagrams via `graphviz` for a particular model or submodel to show the qualified name(s) of the base model class(es) it inherits from.

8. Algolia DocSearch: the default Sphinx search was relatively slower than other third-party vector search solutions. Algolia offered a search-as-you-type service for open-source technical websites, which was configured and added to the Sphinx configuration via the `sphinx-docsearch` extension. It can be accessed on the [latest version](https://docs.pybamm.org/en/latest) of the documentation using the <kbd>`⌘`</kbd> + <kbd>`K`</kbd> or <kbd>`Ctrl`</kbd> + <kbd>`K`</kbd> keyboard shortcuts.

There were many more experiments with the documentation infrastructure which were tried, such as the use of `sphinx.ext.autosummary` for automatically picking up relevant bits of documentation and reST-formatted docstrings from Python modules and classes instead of referencing them, and that of `sphinx.ext.coverage` for automatically checking the if all public API elements were included in the documentation and generating formatted documentation coverage reports. Both of them did not make it to the source code due to issues with public-private API behaviour (see [pybamm-team/PyBaMM #2427](https://github.com/pybamm-team/PyBaMM/issues/2427)) and the conflicting use of the `sphinx.ext.autodoc` extension respectively.

### 🍪 `pybamm-cookiecutter`: a template for battery modelling projects using PyBaMM

After the completion of the requirements and the stretch goals of my project, there is a new project named `pybamm-cookiecutter` that has been started to provide a template for battery modelling projects using PyBaMM. It is a cookiecutter template that can be used to generate a new project with a pre-defined file structure and a set of files that are required to get started with a new project. It is a work in progress and will be updated with more features and functionality in the future. The project can be accessed at https://github.com/pybamm-team/pybamm-cookiecutter.

The idea is to integrate it with features such as `nox`, `pre-commit`, and the necessary `Sphinx` boilerplate such that new projects, research showcases, battery models, and other examples can be integrated with PyBaMM’s documentation and CI/CD infrastructure with ease. At the time of writing, the project can support third-party parameter sets through entry points, which can be loaded from PyBaMM, which comes installed as a dependency. The project is statically typed with `mypy` and has a `pyproject.toml` file with support for `hatch` and `hatch-vcs` to manage releases using `git` tags and uploading wheels to PyPI. Support for the `flit` and `setuptools621` backends is coming soon!

## 📑 A list of issues opened and pull requests submitted

This list contains issues and pull requests that are both specific to and not directly related to my project: they contain documentation infrastructure improvements, improvements to the infrastructure in general, bug fixes, miscellaneous enhancements, and relevant queries and/or discussions.

### 🛠️ Issues

- ([pybamm-team/pybamm.org #1](https://github.com/pybamm-team/pybamm.org/issues/1))                     Support for link checker on GitHub Actions
- ([pybamm-team/pybamm.org #2](https://github.com/pybamm-team/pybamm.org/issues/2))                     Setup pre-commit hooks
- ([pybamm-team/pybamm.org #6](https://github.com/pybamm-team/pybamm.org/issues/6))                     Summary issue: pages and embeds for `pybamm.org`
- ([pybamm-team/pybamm.org #7](https://github.com/pybamm-team/pybamm.org/issues/7))                     Hosting with Netlify and showcasing builds on PRs with `netlify-bot`
- ([pybamm-team/pybamm.org #9](https://github.com/pybamm-team/pybamm.org/issues/9))                     PyBaMM News pages
- ([pybamm-team/pybamm.org #11](https://github.com/pybamm-team/pybamm.org/issues/11))                   Add a 404 page
- ([pybamm-team/pybamm.org #13](https://github.com/pybamm-team/pybamm.org/issues/13))                   A favicon based on the PyBaMM logo
- ([pybamm-team/pybamm.org #15](https://github.com/pybamm-team/pybamm.org/issues/15))                   Donations and sponsorships to list fiscal sponsors and links
- ([pybamm-team/pybamm.org #17](https://github.com/pybamm-team/pybamm.org/issues/17))                   Current and future associations and collaborations (NumFOCUS, the Faraday Institution)
- ([pybamm-team/pybamm.org #18](https://github.com/pybamm-team/pybamm.org/issues/18))                   Embedding @pybamm_ Twitter timeline on the homepage or on an About page

- ([pybamm-team/PyBaMM #2968](https://github.com/pybamm-team/PyBaMM/issues/2968))                       [Bug]: Installing SuiteSparse and SUNDIALS with `tox -e pybamm-requires` will fail silently in some cases
- ([pybamm-team/PyBaMM #3052](https://github.com/pybamm-team/PyBaMM/issues/3052))                       [Bug]: Conversion to scalars for arrays with ndim>0: NumPy 1.25 deprecation (Python 3.9–3.11)
- ([pybamm-team/PyBaMM #3184](https://github.com/pybamm-team/PyBaMM/issues/3184))                       CI cache improvements (nox, pip and more)
- ([pybamm-team/PyBaMM #3197](https://github.com/pybamm-team/PyBaMM/issues/3197))                       Add documentation for example scripts in accordance with `sphinx-gallery`
- ([pybamm-team/PyBaMM #3251](https://github.com/pybamm-team/PyBaMM/issues/3251))                       Infrastructure for nightly releases

- ([pybamm-team/pybamm-cookiecutter #1](https://github.com/pybamm-team/pybamm-cookiecutter/issues/1))   Repository structure (file layouts, cookiecutter templating engines, distribution options)
- ([pybamm-team/pybamm-cookiecutter #5](https://github.com/pybamm-team/pybamm-cookiecutter/issues/5))   Documentation about `pybamm-cookiecutter`

- ([scipy/scipy #18733](https://github.com/scipy/scipy/issues/18733))                                   DOC: documenting the `SciPy` API with  `__init__.py` files (discussion)

### 👷 Pull requests

- ([pybamm-team/pybamm.org #3](https://github.com/pybamm-team/pybamm.org/pull/3))                       Use `Lychee` to check for broken links
- ([pybamm-team/pybamm.org #4](https://github.com/pybamm-team/pybamm.org/pull/4))                       Add `pre-commit` support
- ([pybamm-team/pybamm.org #5](https://github.com/pybamm-team/pybamm.org/pull/5))                       Improvements to `pre-commit`
- ([pybamm-team/pybamm.org #8](https://github.com/pybamm-team/pybamm.org/pull/8))                       Netlify deployment infrastructure
- ([pybamm-team/pybamm.org #10](https://github.com/pybamm-team/pybamm.org/pull/10))                     Add news pages from PyBaMM blogspot
- ([pybamm-team/pybamm.org #12](https://github.com/pybamm-team/pybamm.org/pull/12))                     Custom 404 PyBaMM page
- ([pybamm-team/pybamm.org #14](https://github.com/pybamm-team/pybamm.org/pull/14))                     Favicon for PyBaMM
- ([pybamm-team/pybamm.org #16](https://github.com/pybamm-team/pybamm.org/pull/16))                     Add Donations copy, test sponsor button
- ([pybamm-team/pybamm.org #19](https://github.com/pybamm-team/pybamm.org/pull/19))                     Twitter feed, institutional partners, about PyBaMM
- ([pybamm-team/pybamm.org #22](https://github.com/pybamm-team/pybamm.org/pull/22))                     Restructure pages on the navigation bar and reformat contents
- ([pybamm-team/pybamm.org #24](https://github.com/pybamm-team/pybamm.org/pull/24))                     Reformat news to be single-page only
- ([pybamm-team/pybamm.org #30](https://github.com/pybamm-team/pybamm.org/pull/30))                     Redirect links for benchmarks
- ([pybamm-team/pybamm.org #31](https://github.com/pybamm-team/pybamm.org/pull/31))                     Generate teams
- ([pybamm-team/pybamm.org #32](https://github.com/pybamm-team/pybamm.org/pull/32))                     Accessibility improvements
- ([pybamm-team/pybamm.org #34](https://github.com/pybamm-team/pybamm.org/pull/34))                     Generate teams in the CI

- ([pybamm-team/PyBaMM #2867](https://github.com/pybamm-team/PyBaMM/pull/2867))                         Issue 2725 reduce `Windows` and `macOS` tests and run all tests nightly
- ([pybamm-team/PyBaMM #2916](https://github.com/pybamm-team/PyBaMM/pull/2916))                         Do not run `needs_reply.yml` and `needs_reply_remove.yml` on forks
- ([pybamm-team/PyBaMM #2923](https://github.com/pybamm-team/PyBaMM/pull/2923))                         2447 cache Linux (`apt`) dependencies in CI
- ([pybamm-team/PyBaMM #2961](https://github.com/pybamm-team/PyBaMM/pull/2961))                         Issue 1182 faster tagging for PyBaMM citations
- ([pybamm-team/PyBaMM #2969](https://github.com/pybamm-team/PyBaMM/pull/2969))                         New status badge to reflect scheduled tests
- ([pybamm-team/PyBaMM #3016](https://github.com/pybamm-team/PyBaMM/pull/3016))                         Use Python 3.11 for generating coverage in CI
- ([pybamm-team/PyBaMM #3022](https://github.com/pybamm-team/PyBaMM/pull/3022))                         Add inline-tabs for Sphinx docs
- ([pybamm-team/PyBaMM #3034](https://github.com/pybamm-team/PyBaMM/pull/3034))                         Use `sphinxcontrib-bibtex` for citing references in docs
- ([pybamm-team/PyBaMM #3043](https://github.com/pybamm-team/PyBaMM/pull/3043))                         Use `nbsphinx` to embed Jupyter notebooks
- ([pybamm-team/PyBaMM #3050](https://github.com/pybamm-team/PyBaMM/pull/3050))                         Remove backport `importlib_metadata` from required dependencies
- ([pybamm-team/PyBaMM #3055](https://github.com/pybamm-team/PyBaMM/pull/3055))                         Extract single element from `np.ndarray` when converting to scalar
- ([pybamm-team/PyBaMM #3062](https://github.com/pybamm-team/PyBaMM/pull/3062))                         Temporarily pin `autograd` < 1.6, fix builds
- ([pybamm-team/PyBaMM #3066](https://github.com/pybamm-team/PyBaMM/pull/3066))                         Make docs more maintainable
- ([pybamm-team/PyBaMM #3074](https://github.com/pybamm-team/PyBaMM/pull/3074))                         Generate inheritance diagrams for models and submodels in the documentation
- ([pybamm-team/PyBaMM #3076](https://github.com/pybamm-team/PyBaMM/pull/3076))                         Add an option to download Jupyter notebooks from readthedocs
- ([pybamm-team/PyBaMM #3078](https://github.com/pybamm-team/PyBaMM/pull/3078))                         Restructure example notebooks and their thumbnail galleries in docs
- ([pybamm-team/PyBaMM #3079](https://github.com/pybamm-team/PyBaMM/pull/3079))                         Cache `nox` environments and refactor unit tests in CI
- ([pybamm-team/PyBaMM #3083](https://github.com/pybamm-team/PyBaMM/pull/3083))                         Add floating window tooltips for cross-references in the docs
- ([pybamm-team/PyBaMM #3089](https://github.com/pybamm-team/PyBaMM/pull/3089))                         Display when pages were last updated in the docs
- ([pybamm-team/PyBaMM #3091](https://github.com/pybamm-team/PyBaMM/pull/3091))                         Fix scheduled tests
- ([pybamm-team/PyBaMM #3097](https://github.com/pybamm-team/PyBaMM/pull/3097))                         Enable multithreaded documentation builds
- ([pybamm-team/PyBaMM #3108](https://github.com/pybamm-team/PyBaMM/pull/3108))                         Configure `versions.json` and remove the version switcher dropdown
- ([pybamm-team/PyBaMM #3123](https://github.com/pybamm-team/PyBaMM/pull/3123))                         Fix failing doctests
- ([pybamm-team/PyBaMM #3125](https://github.com/pybamm-team/PyBaMM/pull/3125))                         Updates for `versions.json` and related configuration
- ([pybamm-team/PyBaMM #3157](https://github.com/pybamm-team/PyBaMM/pull/3157))                         Ensure `setup-python` outputs are always included in `nox` cache keys
- ([pybamm-team/PyBaMM #3159](https://github.com/pybamm-team/PyBaMM/pull/3159))                         Algolia docsearch
- ([pybamm-team/PyBaMM #3167](https://github.com/pybamm-team/PyBaMM/pull/3167))                         Restructure notebook galleries
- ([pybamm-team/PyBaMM #3173](https://github.com/pybamm-team/PyBaMM/pull/3173))                         Fix broken notebooks links, port `pybamm.readthedocs.io` ➡️ `docs.pybamm.org`
- ([pybamm-team/PyBaMM #3182](https://github.com/pybamm-team/PyBaMM/pull/3182))                         Enable downloadable PDF, EPUB, and zipped HTML formats on Read the Docs
- ([pybamm-team/PyBaMM #3183](https://github.com/pybamm-team/PyBaMM/pull/3183))                         Add docstrings for `nox` sessions
- ([pybamm-team/PyBaMM #3228](https://github.com/pybamm-team/PyBaMM/pull/3228))                         Updates for `.readthedocs.yaml` and `docs/requirements.txt` deprecation
- ([pybamm-team/PyBaMM #3231](https://github.com/pybamm-team/PyBaMM/pull/3231))                         Add `pip` caches, remove `nox` caches, and remove `requirements.txt`
- ([pybamm-team/PyBaMM #3245](https://github.com/pybamm-team/PyBaMM/pull/3245))                         Temporarily disable PDF documentation builds
- ([pybamm-team/PyBaMM #3260](https://github.com/pybamm-team/PyBaMM/pull/3260))                         Re-enable PDF builds for Read the Docs
- ([pybamm-team/PyBaMM #3264](https://github.com/pybamm-team/PyBaMM/pull/3264))                         Split CI test groups into concurrent jobs
- ([pybamm-team/PyBaMM #3267](https://github.com/pybamm-team/PyBaMM/pull/3267))                         Disallow modifications to `pybamm.Simulation` object attributes after initialisation
- ([pybamm-team/PyBaMM #3279](https://github.com/pybamm-team/PyBaMM/pull/3279))                         Split Jupyter notebooks tests and example scripts tests into separate `nox` sessions
- ([pybamm-team/PyBaMM #3292](https://github.com/pybamm-team/PyBaMM/pull/3292))                         Do not generate notebooks in PDF builds on Read the Docs

- ([pybamm-team/BPX #36](https://github.com/pybamm-team/BPX/pull/36))                                   Add Python 3.11 to CI matrix

- ([pybamm-team/pybamm-cookiecutter #2](https://github.com/pybamm-team/pybamm-cookiecutter/pull/2))     Initial draft for a `cookiecutter` template (licenses and folder structure)
- ([pybamm-team/pybamm-cookiecutter #3](https://github.com/pybamm-team/pybamm-cookiecutter/pull/3))     Add `pre-commit` hooks
- ([pybamm-team/pybamm-cookiecutter #4](https://github.com/pybamm-team/pybamm-cookiecutter/pull/4))     Add templates and configuration for documentation
- ([pybamm-team/pybamm-cookiecutter #6](https://github.com/pybamm-team/pybamm-cookiecutter/pull/6))     Add functionality for third-party parameter sets

## ✍️ Blogs

I wrote a series of blogs entailing my journey throughout the coding period. They can be accessed at the following link: https://dev.to/agriyakhetarpal

## 🔮 Future work

- **A new project named `pybamm-cookiecutter`** is under development. It started as a supernumerary project after the completion of the main requirements of the documentation infrastructure project. This will be a BSD-licensed Python package and a cookiecutter template for battery modelling projects and will rely on PyBaMM as a dependency, the embodiments of which will simplify the creation and usage of third-party parameter sets, add utility functions to use with PyBaMM for ease-of-use, and provide configuration options for the surrounding infrastructure for creating releases and hosting documentation. The development of `pybamm-cookiecutter` can be tracked on its GitHub repository at https://github.com/pybamm-team/pybamm-cookiecutter and the package will soon be `pip`-installable after the first release on PyPI.
- **Nightly release infrastructure:** alongside creating Docker images for simplifying the developer installation of PyBaMM, a new goal is to create nightly builds and subsequent releases on a custom, public PyPI index. The envisioned releases will help install PyBaMM through `pip`, the package manager that ships with Python and provide convenience to users and developers in the case of bug fixes and improvements that are yet to make it to the next official release on PyPI. This process will require suitable versioning with timestamps of release tags and modifications to the existing infrastructure for building wheels on GNU/Linux, macOS, and Windows, and uploading them to the third-party PyPI index.
- **Migration to `pyproject.toml`:** PyBaMM is not a pure-Python package and depends on `pybind11` for interoperability between C++ and Python code. There are new build-backends available, such as `meson-py` and `scikit-build`, which can be used with or alongside the `setuptools621` specification to migrate from setup.py to the new standard for modern Python packaging.
- **Adding example scripts to the hosted documentation:** this will entail adding reST documentation for the Python scripts and configuring them to work with Sphinx and `sphinx-gallery` to display them on the website.
- With all the new changes, we enabled PDF builds for the documentation on Read the Docs, however, the outcome has been error-prone. I will look to resolve the issues with Sphinx’s LaTeXBuilder and ensure that the PDF output works properly, and consider either **self-hosting the documentation** or migrating from Read the Docs to GitHub Pages.

## Acknowledgements

I would like to thank the Google Summer of Code programme, NumFOCUS, and the PyBaMM Team for a rewarding experience and a productive summer. It has been the first time that I have contributed to the development and maintenance of a set of open-source, scientific software of this scale – I have learned a lot throughout the process.

I am honoured to have been mentored by the PyBaMM Steering Council members [Valentin Sulzer](https://sites.google.com/view/valentinsulzer) and [Saransh Chopra](https://saransh-cpp.github.io). They were always helpful in recharging my batteries (no pun intended) and amicably provided valuable feedback on both technical and non-technical issues; going forward, I shall truly cherish the camaraderie we shared.

I am also grateful to [Ferran Brosa Planella](https://www.brosaplanella.xyz/) and [Robert Timms](https://www.robertwtimms.com/) for their assistance in many stages of my contributions to PyBaMM. None of the work done would have been possible without the guidance of the members of the PyBaMM team. I also enjoyed working with [Arjun](https://github.com/arjxn-py), my co-student at GSoC and we took part in discussions on issues and PRs as a part of the collaborative process that the philosophy of working on open-source software advocates for. A part of me wants to inoculate the meticulous zeal of software development and design choices followed by the ethos of PyBaMM across my own life’s spheres.

## 🎬 Footnotes

I am enthralled to have completed the Google Summer of Code 2023 programme! I hope to lay down my contributions to PyBaMM and its infrastructure further in the future and help ameliorate the development and success of the PyBaMM ecosystem.

I also look forward to incorporating the technical skills I have learned into my repertoire through academic, personal, and professional projects in the future.

## 🔭 References

- The GitHub repository for the PyBaMM website: https://github.com/pybamm-team/pybamm.org
- The official PyBaMM website: https://pybamm.org
- The GitHub repository for PyBaMM: https://github.com/pybamm-team/PyBaMM
- The PyBaMM documentation: https://docs.pybamm.org
- The GitHub repository for `pybamm-cookiecutter`: https://github.com/pybamm-team/pybamm-cookiecutter
