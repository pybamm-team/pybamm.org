---
title: PyBaMM GSoC 2023 Project Ideas
---

Improving battery technology is critical as we transition to a green economy. Battery modeling helps to achieve this by reducing costs and increasing reliability and safety. The PyBaMM package provides an open-source framework for physics-based battery models and simulations, with a growing focus on real-world experiments and battery degradation.
While most of our development team works day-to-day on creating new models and better ways to solve them, the proposed projects (which do not require domain-specific knowledge) will be fantastic contributions to the general framework.

To find out more about PyBaMM, you can visit our website [pybamm.org](pybamm.org) or read our [paper](https://openresearchsoftware.metajnl.com/articles/10.5334/jors.309/).

## Getting started
We mostly communicate via Slack, so you should start off by [joining our Slack workspace](https://www.pybamm.org/contact) and heading to the `#gsoc-main` channel.

A comprehensive set of [example notebooks](https://docs.pybamm.org/en/latest/source/examples/index.html) is available for becoming familiar with PyBaMM.
Knowledge of battery physics or mathematical modeling is *not* required for any of the projects, but may be beneficial for some.

All coding will be done in Python, so contributors should have some proficiency in Python, or another object-oriented programming language.
Each project will follow test-driven development, and also involve writing clear documentation (via Sphinx) and examples (mainly in the form of jupyter notebooks) alongside the code. New contributors should make themselves familiar with this workflow.
Finally, new contributors should read the [contributing guidelines](https://github.com/pybamm-team/PyBaMM/blob/develop/CONTRIBUTING.md) and be familiar with the basics of Git and Github.

## Applications

Students must submit proposals based on the ideas suggested here. GSoC will decide how many projects are funded, it’s unlikely that every project will be funded. Selection for the projects will take into consideration, in strongly decreasing order of importance:

- our interactions with you leading up to the project selection date
- your project application
- your background and experience

[Template for proposals](https://docs.google.com/document/d/1gER-yFt5_exHEu9Lx-jfrTH8I7QQXci8oDKH-5wgMys/edit?usp=sharing)

# Projects

* [Documentation](#documentation)
* [Techno-economic analysis](#techno-economic-analysis)
* [Dockerizing and simplifying PyBaMM's installation](#dockerizing-and-simplifying-pybamms-installation)

## Documentation

Our documentation is currently fragmented across several different locations:
* The readme on GitHub
* Our website, pybamm.org, contains generic information about the project
* API docs + a fledgling user guide on [readthedocs](https://pybamm.readthedocs.io/en/latest/)
* Example notebooks on [GitHub](https://docs.pybamm.org/en/latest/source/examples/index.html)
* Some information here on GitHub Wiki

The goal of this project is to consolidate all of the information together under a single location.
* Create a new website using Hugo's scientific python theme (see [#2639](https://github.com/pybamm-team/PyBaMM/issues/2639)). This should contain the same content as the current version of pybamm.org (the pybamm.org URL will be reassigned to this page)
* Link docs.pybamm.org to our readthedocs API docs and user guide (it might make sense to move the user guide out)
* Move information from this wiki page to the website
* Use nbconvert (or other) to run and display static versions of the jupyter notebooks on the website; also use [nbstripout](https://github.com/kynan/nbstripout) to clear the output of notebooks in version control

As a stretch goal, the student will be expected to survey other popular python packages for ideas on how to improve our documentation infrastructure. Some ideas are:
* Using sphinxcontrib-bibtex to print references from bibtex instead of hardcoding them in docstrings as we currently do
* Dependency trees
* In the API docs, link to examples where various functionality is used (scikit-learn)

Note that the focus of this project is not on writing documentation but on improving the infrastructure around it.

### Expected outcomes
* All documentation in one place
* As much automation as possible to make maintaining and updating documentation easy

### Desired skills

* Basic python and markdown knowledge
* Basic web development knowledge would be helpful but not required (html + css)
* Hosting documentation on Sphinx
* Git version control, CI, testing

### Difficulty
* Medium. This project is suitable for a 350h project.

### Potential mentors
* [Robert Timms](https://github.com/rtimms)
* [Valentin Sulzer](https://github.com/tinosulzer)
* [Saransh Chopra](https://github.com/Saransh-cpp)
* [Priyanshu Agarwal](https://github.com/priyanshuone6)

## Techno-economic analysis

While PyBaMM goes deep into advanced models of batteries, much can be done with simpler "back-of-the-envelope" calculations for the capacity, energy, mass, and cost of a battery. The goal of this project will be to create a library for techno-economic analysis that can be combined with existing PyBaMM functionality. This project will draw inspiration from existing libraries (https://github.com/mjlacey/cellmodels, https://github.com/ndrewwang/BotB). See those repositories for more detail on what the outcome might look like.

### Expected outcomes
* A library for techno-economic analysis that can be combined with existing PyBaMM functionality

### Desired skills

* Strong python skills, particularly ability to construct user-friendly APIs
* Knowledge of basic battery concepts (capacity, resistance, energy, electrodes, etc)
* Git version control, CI, testing

### Difficulty
* Medium. This project is suitable for a 175h project.

### Potential mentors
* [Robert Timms](https://github.com/rtimms)
* [Valentin Sulzer](https://github.com/tinosulzer)
* [Jacqueline Edge](https://www.linkedin.com/in/jacqueline-edge-1754111/?originalSubdomain=uk)

## Dockerizing and simplifying PyBaMM's installation

PyBaMM currently has multiple required and optional dependencies, but the installation process for some of them is not straightforward. PyBaMM depends on `tox` to unify the installation process at the moment, but Dockerizing the process (without removing the `tox` dependency) will make it uniform for every platform and developer. The goal of this project would be to make PyBaMM's developer installation, with optional as well as default dependencies, a breeze. Ideally, in the end, developers will be able to install PyBaMM (with specific dependencies chosen by them) using a single command.

### Expected outcomes
* A new installation process using Docker. Related issue - [#1926](https://github.com/pybamm-team/PyBaMM/issues/1926).
* A better installation guide (for all installation processes, platforms, and popular package managers).
* CI for testing different installation processes of PyBaMM.
* DockerHub support and CI (synced with PyBaMM's releases) for uploading container images to the same.

Other possible issues/PRs that can be tackled - [#2457](https://github.com/pybamm-team/PyBaMM/issues/2457), [#2346](https://github.com/pybamm-team/PyBaMM/issues/2346), [#2537](https://github.com/pybamm-team/PyBaMM/pull/2537).

Stretch goals:

* Providing Docker support for running the example notebooks.
* Docker images to install PyBaMM with specific optional dependencies chosen by a developer.
* Uploading separate Docker images (each mapping to different optional dependencies) to DockerHub with CI support (synced with PyBaMM's releases).

### Desired skills

* Basic knowledge of DevOps tools and platforms - Docker, DockerHub, CI (GitHub Actions), Shell Scripting, etc.
* Some knowledge/experience in packaging and building Python libraries.
* Git version control.

### Difficulty
* Medium. This project is suitable for a 350h project.

### Potential mentors
* [Saransh Chopra](https://github.com/Saransh-cpp)
