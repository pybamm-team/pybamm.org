# pybamm.org

[![Netlify](https://api.netlify.com/api/v1/badges/c4c60d47-1de1-4d0a-8a25-726d3cf100c8/deploy-status)](https://app.netlify.com/sites/pybamm-developer-preview/deploys)
[![Links](https://github.com/pybamm-team/pybamm.org/actions/workflows/links.yml/badge.svg)](https://github.com/pybamm-team/pybamm.org/actions/workflows/links.yml)
[![pre-commit.ci](https://results.pre-commit.ci/badge/github/pybamm-team/pybamm.org/main.svg)](https://results.pre-commit.ci/latest/github/pybamm-team/pybamm.org/main)

Source code for [pybamm.org](https://www.pybamm.org), released under the
BSD-3-Clause License. Currently under active development.

## Steps to contribute

1. Fork this repository
2. Install the extended version of Hugo from <https://gohugo.io/installation/>
and add it to your `PATH`
3. Clone your forked repository and add the theme repository as a submodule,
from <https://github.com/scientific-python/scientific-python-hugo-theme>.

```bash
git submodule update --init --recursive
```

4. Create pages and run the server locally with

```bash
make html
make serve
```

5. Before committing your changes, install [`pre-commit`](https://pre-commit.com/),
update the hooks, and run with

```bash
pip install pre-commit
pre-commit install
```

to ensure that there are no style errors before committing your changes. The
current hooks provide support for checking spelling errors and typos, Markdown
style, and common file-based issues.

Rather than just the files changed due to a commit, you may run the hooks on
all files using the `pre-commit run --all-files` command.

## Deployment

TODO: Netlify

## Analytics

TODO: Plausible.io / Google Analytics
