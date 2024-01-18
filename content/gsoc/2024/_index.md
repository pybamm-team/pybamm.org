---
title: PyBaMM GSoC 2024 Project Ideas
summary: This page contains project ideas for PyBaMM's participation in the Google Summer of Code program in 2024. These projects are intended to be suitable for students who are new to PyBaMM or to open-source software development in general, and wish to work on a project that will be beneficial to PyBaMM and its community.
---

Improving battery technology is critical as we transition to a green economy. Battery modeling helps to achieve this by reducing costs and increasing reliability and safety. The PyBaMM package provides an open-source framework for physics-based battery models and simulations, with a growing focus on real-world experiments and battery degradation.
While most of our development team works day-to-day on creating new models and better ways to solve them, the proposed projects (which do not require domain-specific knowledge) will be fantastic contributions to the general framework.

To find out more about PyBaMM, you can visit our website [pybamm.org](/) or read our [paper](https://openresearchsoftware.metajnl.com/articles/10.5334/jors.309/).

## Getting started

We mostly communicate via Slack, so you should start off by [joining our Slack workspace](https://pybamm.org/contact/) and heading to the `#gsoc-main` channel.

A comprehensive set of [example notebooks](https://docs.pybamm.org/en/latest/source/examples/index.html) is available for becoming familiar with PyBaMM.
Knowledge of battery physics or mathematical modeling is *not* required for any of the projects, but may be beneficial for some.

Students are encouraged to propose their own ideas, but these should be discussed with the mentors before submitting a proposal.

All coding will be done in Python, so contributors should have some proficiency in Python, or another object-oriented programming language.

Each project will follow test-driven development, and also involve writing clear documentation (via Sphinx) and examples (mainly in the form of jupyter notebooks) alongside the code. New contributors should make themselves familiar with this workflow.

Finally, new contributors should read the [contributing guidelines](https://docs.pybamm.org/en/latest/source/user_guide/contributing.html) and be familiar with the basics of Git and GitHub.

## Applications

Students must submit proposals based on the ideas suggested here. GSoC will decide how many projects are funded, it’s unlikely that every project will be funded. Selection for the projects will take into consideration, in strongly decreasing order of importance:

- our interactions with you leading up to the project selection date
- your project application
- your background and experience

Applicants must have at least 1 non-trivial contribution in PyBaMM for their application to be considered.

We provide a [template for proposals](https://docs.google.com/document/d/1gER-yFt5_exHEu9Lx-jfrTH8I7QQXci8oDKH-5wgMys/edit?usp=sharing) for applicants to use, but it is not required to follow it exactly and modifications are encouraged as needed.

## Projects

### Migrate from `unittest` to `pytest`

PyBaMM's inception predates the rise in popularity of `pytest`, and so we have used the `unittest` testing framework for our tests. However, `pytest` is now the de facto standard for testing in Python, and it is time to migrate our test cases over to it. The reason for this is that `pytest` is much more flexible and powerful than `unittest`, and will allow us to write better tests with less code. This may also involve migrating our test cases to use `hypothesis` for property-based testing, which will allow us to write even more powerful tests via the use of strategies, which are like generators for test cases.

PyBaMM already uses `pytest` with the `nbmake` package to run our example notebooks as tests, but still uses `unittest` for the rest of the tests. `pytest-xdist` is also used to run the tests in parallel, which should end up being faster than the current serial implementation and should be adapted to be used with the new test framework.

The student will be expected to look at other popular Python packages to see how they use `pytest` and `hypothesis` to write tests, and then migrate our tests over to use these frameworks. This will involve writing new tests, and also migrating existing tests over to the new framework, making use of and exploring the `pytest` documentation for scouting potential features to be incorporated. The student will also be expected to improve the test coverage of the codebase, and to write tests for any new code that they end up writing.

As a stretch goal, the packaging infrastructure for PyBaMM should be updated to include a `pytest` test suite that can be run by users to check that their installation is working correctly for users who do not have access to a source installation of PyBaMM, i.e., through `pybamm.test()` or similar.

#### Expected outcomes

* All test files and modules migrated to use `pytest` in the code base, in a way that is consistent with modern Python software engineering and testing practices – either manually or via automated migration tools
* Improvisation of test coverage
* Utilisation of advanced testing techniques based on advanced `pytest` features and `hypothesis` as a framework
* Deprecate some legacy test invocation methods such as `run-tests.py` in favour of the `pytest` path finding and test case discovery mechanisms

#### Desired skills

* Experience with Python API design and testing, test-driven development, and continuous integration
* Test coverage and code quality analysis tools
* Some experience with `unittest`, `pytest`, and `hypothesis` is desirable, but not required
* Git version control, managing pull requests, and code reviews, as well as the GitHub workflow for open-source projects

### Difficulty and suitable project length

* Medium. This project is suitable for a 175-hour duration.

### Potential mentors

* [Agriya Khetarpal](https://agriyakhetarpal.github.io/)

### Migrate to a modern build-backend such as `scikit-build-core` or `meson-python` as a new build system for PyBaMM

There are two new build systems that are gaining popularity in the Python ecosystem: `scikit-build-core` and `meson-python`. Both of these build systems are designed to be more flexible and powerful in order to support the needs of compiled Python packages, which are becoming more common in line with Python's use in the field of scientific computing. PyBaMM relies on a C++-based solver based on SUNDIALS and SuiteSparse, and thereby requires significant compilation prerequisites and build-time configuration.

The goal of this project is to migrate PyBaMM's build system over to one of these new build systems, and to deprecate the current build system that is based on `setuptools` and `wheel`. This may involve writing new build scripts, adhering to the new build system's conventions, and setting up compilers and toolchains accordingly to ensure that PyBaMM works correctly on all platforms and architectures that are currently supported.

As a stretch goal, the student can explore the possibility of cross-compiling PyBaMM wheels for different platforms and architectures that are not currently supported, such as ARM-based systems for Linux and macOS.

#### Expected outcomes

* A new build backend for PyBaMM, either `scikit-build-core` or `meson-python`
* Revamped build scripts, configuration, and possibly a complete rewrite of the `setup.py` code
* Retained support for all platforms and architectures that are currently supported by PyBaMM
* Ensuring that there is a reliable mechanism for editable installations in CI and local development, with or without the use of the `-–no-build-isolation` command-line flag

#### Desired skills

* Experience with Python packaging for compiled extensions will be highly beneficial
* Build systems such as CMake, Meson, and/or Ninja
* Knowledge of compilers and toolchains, and how to set them up on different platforms
* Setting up efficient CI/CD pipelines and DevOps workflows across platforms and architectures

### Difficulty and suitable project length

* Hard. This project is suitable for a 350-hour duration.

### Potential mentors

* [Agriya Khetarpal](https://agriyakhetarpal.github.io/)
