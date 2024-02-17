---
title: PyBaMM GSoC 2024 Project Ideas
summary: This page contains project ideas for PyBaMM's participation in the Google Summer of Code program in 2024. These projects are intended to be suitable for students who are new to PyBaMM or to open-source software development in general, and wish to work on a project that will be beneficial to PyBaMM and its community.
---

## Migrate from `unittest` to `pytest`

PyBaMM's inception predates the rise in popularity of `pytest`, and so we have used the `unittest` testing framework for our tests. However, `pytest` is now the de facto standard for testing in Python, and it is time to migrate our test cases over to it. The reason for this is that `pytest` is much more flexible and powerful than `unittest`, and will allow us to write better tests with less code. This may also involve migrating our test cases to use `hypothesis` for property-based testing, which will allow us to write even more powerful tests via the use of strategies, which are like generators for test cases.

PyBaMM already uses `pytest` with the `nbmake` package to run our example notebooks as tests, but still uses `unittest` for the rest of the tests. `pytest-xdist` is also used to run the tests in parallel, which should end up being faster than the current serial implementation and should be adapted to be used with the new test framework.

The student will be expected to look at other popular Python packages to see how they use `pytest` and `hypothesis` to write tests, and then migrate our tests over to use these frameworks. This will involve writing new tests, and also migrating existing tests over to the new framework, making use of and exploring the `pytest` documentation for scouting potential features to be incorporated. The student will also be expected to improve the test coverage of the codebase, and to write tests for any new code that they end up writing.

As a stretch goal, the packaging infrastructure for PyBaMM should be updated to include a `pytest` test suite that can be run by users to check that their installation is working correctly for users who do not have access to a source installation of PyBaMM, i.e., through `pybamm.test()` or similar.

### Expected outcomes

* All test files and modules migrated to use `pytest` in the code base, in a way that is consistent with modern Python software engineering and testing practices – either manually or via automated migration tools
* Improvisation of test coverage
* Utilisation of advanced testing techniques based on advanced `pytest` features and `hypothesis` as a framework
* Deprecate some legacy test invocation methods such as `run-tests.py` in favour of the `pytest` path finding and test case discovery mechanisms

### Desired skills

* Experience with Python and unit testing (`unittest`, `pytest`, and `hypothesis`) in Python.
* Some experience with test-driven development, continuous integration, and coverage tools is desirable, but not required.
* Git version control and GitHub workflow for open-source projects.

### Difficulty and suitable project length

* Medium. This project is suitable for a 175-hour duration.

### Potential mentors

* [Agriya Khetarpal](https://agriyakhetarpal.github.io/)
* [Saransh Chopra](https://Saransh-cpp.github.io/)
* [Valentin Sulzer](https://sites.google.com/view/valentinsulzer)
* [Arjun Verma](https://github.com/arjxn-py)

## Migrate to a modern build-backend such as `scikit-build-core` or `meson-python` as a new build system for PyBaMM

There are two new build systems that are gaining popularity in the Python ecosystem: `scikit-build-core` and `meson-python`. Both of these build systems are designed to be more flexible and powerful in order to support the needs of compiled Python packages, which are becoming more common in line with Python's use in the field of scientific computing. PyBaMM relies on a C++-based solver based on SUNDIALS and SuiteSparse, and thereby requires significant compilation prerequisites and build-time configuration.

The goal of this project is to migrate PyBaMM's build system over to one of these new build systems, and to deprecate the current build system that is based on `setuptools` and `wheel`. This may involve writing new build scripts, adhering to the new build system's conventions, and setting up compilers and toolchains accordingly to ensure that PyBaMM works correctly on all platforms and architectures that are currently supported.

As a stretch goal, the student can explore the possibility of cross-compiling PyBaMM wheels for different platforms and architectures that are not currently supported, such as ARM-based systems for Linux and macOS.

### Expected outcomes

* A new build backend for PyBaMM, either `scikit-build-core` or `meson-python`
* Revamped build scripts, configuration, and possibly a complete rewrite of the `setup.py` code
* Retained support for all platforms and architectures that are currently supported by PyBaMM
* Ensuring that there is a reliable mechanism for editable installations in CI and local development, with or without the use of the `-–no-build-isolation` command-line flag

### Desired skills

* Experience with Python packaging for compiled extensions will be highly beneficial
* Build systems such as CMake, Meson, and/or Ninja
* Knowledge of compilers and toolchains, and how to set them up on different platforms is desirable, but not required.
* Experience with CI/CD pipelines and DevOps workflows across platforms and architectures is desirable, but not required.

### Difficulty and suitable project length

* Hard. This project is suitable for a 350-hour duration.

### Potential mentors

* [Agriya Khetarpal](https://agriyakhetarpal.github.io/)
* [Saransh Chopra](https://Saransh-cpp.github.io/)
* [Arjun Verma](https://github.com/arjxn-py)

## Build and publish `pybamm-cookiecutter` as a template for new PyBaMM-based projects

There is a cookiecutter template at https://github.com/pybamm-team/pybamm-cookiecutter/ that was started as a part of GSoC 2023. The goal of this project is to finish the template and release it on PyPI so that it can be used by the community to create new PyBaMM-based projects. The template has had a start as of November 2023, but it is not ready for use by researchers and scientists who are looking to add their own parameter sets and models to PyBaMM.

The student will receive an opportunity to perform each and every aspect of Python software development tasks, including adding features, writing tests, documentation, usage examples, CI/CD pipelines for testing automation and deployment, and so on. The template is supposed to be an opinionated one, combining all the best ideas from the original PyBaMM repository and new practices in other data science and scientific computing projects and their distribution, in order to provide both extensibility and ease of use for new users in the battery modeling fraternity.

### Expected outcomes

* Completion of a cookiecutter template that can be used to create new PyBaMM-based projects
* Documentation and usage examples for the template in the form of a Sphinx-based website and Jupyter notebooks
* CI/CD pipelines for testing automation and deployment for the correct functioning of the template
* Release infrastructure that allows the template to be published on PyPI and installed via `pip`, mirroring PyBaMM's own release system and versioning

### Desired skills

* Experience with Python packaging and distribution for pure-Python packages and modern Python projects will be beneficial but is not required
* Familiarity with cookiecutter templates and the `cookiecutter` Python package (or other templating packages, such as `cookieninja`, `copier`, `cruft`), including the use of `jinja2` as a templating engine
* Basics of CI/CD pipelines and DevOps for Python projects

### Difficulty and suitable project length

* Easy. This project is suitable for a 175-hour duration.

### Potential mentors

* [Agriya Khetarpal](https://agriyakhetarpal.github.io/)
* [Saransh Chopra](https://Saransh-cpp.github.io/)

## Training a Machine Learning Model for Chatbot Assistance on PyBaMM Documentation

PyBaMM's extensive documentation serves as a valuable resource for users, but accessing information efficiently can be challenging. This project aims to develop a chatbot using machine learning techniques trained on PyBaMM documentation. The chatbot will act as a virtual assistant, providing users with prompt and accurate responses to basic queries related to PyBaMM functionalities, installation instructions, usage guidelines, and troubleshooting tips.

The project will involve collecting and preprocessing a comprehensive dataset comprising PyBaMM documentation, including tutorials, API references, user guides, and FAQs. This data will then be used to train a machine learning model, selecting from various architectures such as sequence-to-sequence models or transformers. Natural language understanding techniques will be implemented to preprocess user queries and extract relevant features. The trained model will be integrated into an interactive chatbot interface, allowing users to interact in real-time. Finally, the chatbot's performance will be evaluated using metrics such as accuracy and user satisfaction, with feedback used to refine and improve its responses iteratively.

### Expected outcomes

* A trained machine learning model capable of understanding and responding to user queries based on PyBaMM documentation.
* Development of a functional chatbot interface enabling users to interact with the model for assistance and support.
* Improved user experience and efficiency in accessing information related to PyBaMM through the chatbot.

### Desired skills

* Experience with machine learning techniques for natural language processing, including text classification and sequence modeling.
* Experience with deep learning frameworks such as TensorFlow or PyTorch.
* Good programming skills in Python for implementing the chatbot interface and integration.
* Familiarity with chatbot development platforms or libraries is advantageous.
* Ability to analyze user feedback and iteratively improve the chatbot's performance and usability.

### Difficulty and suitable project length

* Medium. This project is suitable for a 175-hour duration.

### Potential mentors

* [Arjun Verma](https://github.com/arjxn-py)
