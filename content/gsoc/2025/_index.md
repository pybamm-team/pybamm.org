---
title: PyBaMM GSoC 2025 Project Ideas
summary: This page contains project ideas for PyBaMM's participation in the Google Summer of Code program in 2025. These projects are intended to be suitable for students or professionals who are new to PyBaMM or to open-source software development in general, and wish to work on a project that will be beneficial to PyBaMM and its community.
---

{{< admonition note >}}

We are planning on taking part in Google Summer of Code 2025. We will keep updating our project ideas and add potential ones here as soon as they are available. Stay tuned and keep following this page for updates!

The projects below are arranged in descending order of priority.
{{< /admonition >}}

## Adding type hints to PyBaMM models

PyBaMM (Python Battery Mathematical Modelling) has evolved significantly since 2019 as a framework for battery modeling applications. While the focus on performance optimization has led to impressive speed improvements across PyBaMM and the time taken from conducting an experiment to its industrial impact, it has introduced complexity that can make code validation and maintenance challenging. This project aims to systematically introduce static typing to PyBaMM's codebase, particularly focusing on the `pybamm.models` component and surrounding areas, to enhance code safety and improve the developer experience.

The current lack of type hints in PyBaMM creates several challenges. Silent failures in the validation of model arguments often only surface at runtime, making debugging difficult and time-consuming. New contributors frequently struggle to understand the expected input and output types for functions and methods, leading to a steeper learning curve. This absence also limits IDE support for code completion and error detection, making model development less efficient for researchers. Additionally, maintaining API consistency across different parts of the API becomes more challenging without clear type definitions, and numerical operations can fail unexpectedly due to unclear data type expectations.

Hence, this project seeks to implement a comprehensive typing system to improve PyBaMM's codebase. By enhancing code reliability through static type checking, we can catch errors earlier in the development process. The addition of clear type signatures will serve as implicit documentation, making the codebase more accessible to new contributors. This improvement in tooling support will accelerate development workflows and make maintenance and refactoring tasks more manageable. Furthermore, the typing system will facilitate better integration with downstream scientific libraries that rely on PyBaMM, such as PyBOP and other upcoming projects.

The scope could be expanded to include more sophisticated items towards a stretch goal if time permits. This might include creating separate type stub files for improved modularity, developing custom types for battery-specific validation, and extending type coverage to additional modules beyond the core models.

### Technical details

The implementation of the typing system will require careful evaluation of different approaches by the mentee, and they can explore either inline type hints in existing code, or separate `.pyi` stub files for backward compatibility, or the creation of a standalone `pybamm-stubs` package, or potentially a hybrid approach combining multiple methods. Each approach has its own trade-offs in terms of maintenance burden, backward compatibility, and ease of implementation – the mentee is expected to survey the existing strategy adopted by Scientific Python libraries and choose the most suitable approach for PyBaMM.

Previously, type hints were added to the expression tree via [pybamm-team/pybamm#3578](https://github.com/pybamm-team/PyBaMM/issues/3578), which can serve as a reference for the mentee. There are a few other related tasks, such as using NumPy's typing module appropriately ([pybamm-team/pybamm#4512](https://github.com/pybamm-team/PyBaMM/issues/4512)) and adding a type checker ([mypy](https://mypy.readthedocs.io)) in the CI, that can be used by applicants to familiarise themselves with PyBaMM's current typing infrastructure.

The type system design will require particular attention to several key areas. The mentee may need to create custom types for battery-specific parameters, ensuring they accurately represent the domain concepts. The system must handle NumPy array types and dimensional analysis effectively, define clear type hierarchies for different battery models, and manage type compatibility with scientific computing libraries. The implementation of generic types for flexible model arguments will also prove to be essential for maintaining the PyBaMM framework's versatility.

### Expected outcomes

- Type system architecture: documentation of typing strategy and conventions, type hierarchy design for battery models, integration plan with existing codebase

- Implementation: type hints for core pybamm.models API, custom type definitions for battery-specific components as needed, a short migration guide for adding types to other modules

- Validation: CI integration with type checkers (Mypy, Pyright, basedmypy) as pre-commit hooks, documentation for type checking workflow and updates to the contributing guide

- Documentation: Updated API documentation with type information, and a guide for downstream libraries on utilizing type information provided by PyBaMM

### Desired skills

- Some experience with static typing in Python is beneficial, but not required.
- Python programming experience, Git version control, and GitHub workflow for open-source projects
- An affinity for reading lots of code and documentation
- An interest in scientific computing and battery modeling (prior experience not required)
- As a plus, knowledge on how to use scientific computing libraries (NumPy, SciPy)
- Some understanding of continuous integration providers (GitHub Actions, etc.) is beneficial, but not required.

### Difficulty

**Easy**. This project is suitable for a 175-hour duration.

### Potential mentors

* [Saransh Chopra](https://Saransh-cpp.github.io/)
* [Agriya Khetarpal](https://github.com/agriyakhetarpal/)

<!-- * [Valentin Sulzer](https://github.com/valentinsulzer)
* [Robert Timms](https://github.com/rtimms)
* [Arjun Verma](https://arjxnpy.vercel.app/)
* [Ferran Brosa Planella](https://www.brosaplanella.xyz/) -->

## Refactoring PyBaMM's testing suite with pytest plugins and hypothesis

PyBaMM (Python Battery Mathematical Modelling) used `unittest` as its testing framework until last year. However, thanks to the efforts from [@prady0t](https://github.com/prady0t), it now uses `pytest.` `pytest` is a modern and community-maintained testing framework for Python that is more flexible and feature-rich than the built-in `unittest` module. Migrating such a huge codebase from `unittest` to `pytest` was an exceptional feat; however, because of limited time and resources, we could not leverage several amazing things that `pytest` offers. There have been efforts to introduce `pytest` specific features, but these efforts have been distributed, and now the codebase is at an awkward stage where some tests utilize `pytest`'s capabilities and some do not.

PyBaMM currently uses different tools/functionalities to do the same thing at different places in the testing suite. This project aims to standardize the tesing suite to use one tool for one job, most likely, a `pytest` compatible tool. Moreover, the project will also require choosing the right tools (by researching multiple testing tools available on the internet) and writing instructions for these then standardized tools in documentation. Besides `pytest`, there are several other testing issues that can be used to get familiar with PyBaMM's testing suite, such as [modernizing NumPy array assertion tests](https://github.com/pybamm-team/PyBaMM/issues/4488). Mentee can use their proposal to suggest additional `pytest` plugins and features that they think will benefit PyBaMM's testing suite.

Furthermore, [Hypthesis](https://hypothesis.readthedocs.io) is a modern property-based testing implementation for Python. Property-based testing is a testing method that automatically generates and tests a wide range of inputs, often missed by tests written by humans, ensuring robust tests and helping developers find edge cases more easily. The library creates unit tests. In a nutshell, Hypothesis can parametrize test, running test function over a wide range of matching data from a "search strategy" established by the library. Through paratemerization, Hypothesis can catch bugs which might go unnoticed by writing manual inputs for the tests. There have been a few efforts ([pybamm-team/PyBaMM#4703](https://github.com/pybamm-team/PyBaMM/issues/4703), [pybamm-team/PyBaMM#4724](https://github.com/pybamm-team/PyBaMM/pull/4724)) to add property-based testing, and this project would aim to identify all the test functions that can benefit from and use `Hypothesis` to implement property-based testing.

### Technical details

`pytest` includes several beneficial features, such as parameterization of tests and using fixtures. There are multiple ongoing efforts to utilize `pytest`'s features better within PyBaMM ([parameterization and fixtures](https://github.com/pybamm-team/PyBaMM/issues/4502), [removing shared.py](https://github.com/pybamm-team/PyBaMM/pull/4401), [more fixtures](https://github.com/pybamm-team/PyBaMM/issues/4837)), but we still have a long way to go. The project will start by picking up existing issues and cherry-picking PRs that are working towards a better testing suite, then slowly take over to create custom `pytest` fixtures or even plugins if required. The mentee will also be tasked to update the deprecated/outdated libraries and syntax used in the testing suite, such as `numpy.assert_almost_equal` statements. Therefore, the project requires auditing the entire testing suite, pointing out outdated, redundant, or deprecated tools and libraries being used, and replacing them with more modern (or `pytest`) solutions.

`Hypothesis` provides several easy-to-use decorators. Once the mentee has identified functions that will benefit from property-based testing, they can use decorators provided by `Hypothesis` to give the identified test functions set of properties. The project might require some minimal updates in PyBaMM's CI to accommodate for new plugins and libraries; hence, the mentee will be involved in writing YAML files for GitHub Actions.

### Expected outcomes

- Efficient tests: Tests that act exactly how they act right now, but are better organised and use the right tool for the right job (instead of using an arbitrary tool that does the job)

- Implementation: Refactoring tests using `pytest` plugins and features; audit of the testing suite; using `Hypothesis` wherever it can be used; no outdated syntax remaining

- CI integration: Running `hypothesis` tests on GitHub Actions or using tools such as [oss-fuzz to run property-based tests continuously on the cloud](https://google.github.io/oss-fuzz/getting-started/new-project-guide/python-lang/#hypothesis)

- Validation: CI passes on each pull request and the coverage does not go down; tests look more maintainable for the longer run (that is, they are easier to extend or debug)

- Documentation: Updated contributing guide to reflect the new testing conventions for future developers

### Desired skills

- Some experience with unit testing using `pytest` in Python
- Python programming experience, Git version control, and GitHub workflow for open-source projects
- An affinity for experimenting with new testing and infrastructure tools
- As a plus, knowledge on how to use scientific computing libraries (NumPy, SciPy)
- Some experience with using `pytest` plugins is beneficial, but not required
- Some understanding of continuous integration providers (GitHub Actions, etc.), coverage tools (Codecov, `pytest-cov`, etc.), and property-based testing is beneficial, but not required

### Difficulty

**Medium**. This project is suitable for a 175-hour duration.

### Potential mentors

* [Saransh Chopra](https://Saransh-cpp.github.io/)

<!-- * [Pradyot Ranjan](https://github.com/prady0t/)
* [Agriya Khetarpal](https://github.com/agriyakhetarpal/)
* [Valentin Sulzer](https://github.com/valentinsulzer)
* [Robert Timms](https://github.com/rtimms)
* [Arjun Verma](https://arjxnpy.vercel.app/)
* [Ferran Brosa Planella](https://www.brosaplanella.xyz/) -->
