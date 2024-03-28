---
title: Google Season of Docs with PyBaMM
summary: This page describes the process, idea lists, and other logistics for participation in the Google Season of Docs program with PyBaMM.
shortcutDepth: 1
---

<!-- Note: the names of individual pages in folders should be marked with an
underscore, i.e., _index.md to treat them as branched pages. -->

# Document PyBaMM submodels

## About your organisation

PyBaMM (Python Battery Mathematical Modelling) is an open-source battery simulation package written in Python, whose mission is to accelerate battery modelling research by providing open-source tools for multi-institutional, interdisciplinary collaboration. Broadly, PyBaMM consists of (i) a framework for writing and solving systems of differential equations, (ii) a library of battery models and parameters, and (iii) specialised tools for simulating battery-specific experiments and visualising the results. Together, these enable flexible model definitions and fast battery simulations, allowing users to explore the effect of different battery designs and modelling assumptions under a variety of operating scenarios.

## About your project

### Your project's problem

The battery models included in PyBaMM’s library consist of an innovative submodel structure allowing users to modify the physics they wish to include into their model, including such processes like degradation or particle mechanics. Ideally if a PyBaMM user or developer has developed new, novel battery submodels we wish to encourage them to include these within PyBaMM as a PR. However, so far we have only had limited success in encouraging people outside the core development team to contribute new battery models, and the obvious reason for this is that the documentation on the existing submodel structure is limited and there is no documentation on the process of integrating a new submodel.

The goals of this project is to (a) document the existing submodule structure at a higher level than currently exists (the current documentation is limited to docstrings on individual classes), at a level suitable for new PyBaMM users who just wish to use the existing submodels, and (b) document the process for creating and publishing new PyBaMM models, either as a new submodel, or as a standalone model entry point.

### Your project's scope

This project has three goals, (a) document the existing submodel structure, (b) document the process for creating a new submodel, and (c) document how to publish a standalone model entry point.

**Document the existing submodel structure**: Create a unified user documentation for the PyBaMM models/submodels in our sphinx generated [user guide](https://docs.pybamm.org/en/stable/source/user_guide/index.html). There should be a separate page for each submodel type (e.g. “particle”, “current collector”), along with a list of the relevant options, variables, parameters, model equations (in latex equation format) and paper citations for that submodel. For each main model type (SPM, SPMe, DFN) there should be a list of submodels that are compatible with this model.
**Document the process for creating a new submodel**: This involves taking the current information on the submodel structure (in docstrings on, for example, [`pybamm.BaseSubModel`](https://docs.pybamm.org/en/stable/source/api/models/submodels/base_submodel.html)), and writing a higher level user-guide on the submodel class structure and how multiple submodels work together to form a full battery model. Another user-guide should be written on how to create and integrate a new submodel into PyBaMM, stepping through every step of the process from first creating an issue, writing the submodel class, where to get help from the community, the Pull Request process and going through a review of your code and finally merging it into PyBaMM
**Document PyBaMM model entry points**: The PyBaMM team is currently in the process of creating model entry points (see [issue 3908](https://github.com/pybamm-team/PyBaMM/issues/3908)) for users that wish to publish their own standalone PyBaMM models. We wish to add user-facing documentation that covers how to create a new model entry point using a template repository we provide, and how to publish this online.

The new documentation will be written in reStructuredText and incorporated into the existing PyBaMM user guide. Any equations will be written using sphinx’s [math directive](https://sphinx-rtd-trial.readthedocs.io/en/latest/ext/math.html), and the user guides will link to the relevant API docs where appropriate.

Core PyBaMM developers [Martin Robinson](https://github.com/martinjrobins) and [Ferran Brosa Planella](https://github.com/brosaplanella) will onboard and then mentor the technical writer.

### Measuring your project's success

Success measures for this project would be:
Reducing the number of submodel questions on our GitHub discussion boards and allowing developers to simply point to existing documentation to answer these questions
PRs adding or updating submodels from outside the current PyBaMM development team
New model entry points from users outside the current development team

### Timeline


| Dates              | Action Items                                                                |
|--------------------|-----------------------------------------------------------------------------|
| May                | Onboarding and reviewing existing submodel structure and documentation      |
| June               | Plan new user guides                                                        |
| August - September | Write users guides                                                          |
| October - November | Review based on feedback and merge the user guides as PRs into the codebase |



### Project budget


| Budget Item      | Amount (USD)    | Notes                                                                    |
|------------------|-----------|--------------------------------------------------------------------------|
| Technical writer | 10,000.00 | Design, write and publish new submodel and model entry point user-guides |


### Additional information

This project would be suitable for a technical writer familiar with mathematical modelling and working with Python and Sphinx. Any battery specific modelling experience is desirable, but could be picked up during the project as long as the writer has a general modelling background.
