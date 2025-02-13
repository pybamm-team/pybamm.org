---
title: PyBaMM GSoC 2025 Project Ideas
summary: This page contains project ideas for PyBaMM's participation in the Google Summer of Code program in 2025. These projects are intended to be suitable for students who are new to PyBaMM or to open-source software development in general, and wish to work on a project that will be beneficial to PyBaMM and its community.
---

{{< admonition note >}}

We are planning on taking part in Google Summer of Code 2025. We will keep updating our project ideas and add potential ones here as soon as they are available. Stay tuned and keep following this page for updates!

{{< /admonition >}}

## Adding type hints to PyBaMM models

PyBaMM (Python Battery Mathematical Modelling) has evolved significantly since 2019 as a framework for battery modeling applications. While the focus on performance optimization has led to impressive speed improvements across PyBaMM and the time taken from conducting an experiment to its industrial impact, it has introduced complexity that can make code validation and maintenance challenging. This project aims to systematically introduce static typing to PyBaMM's codebase, particularly focusing on the `pybamm.models` component and surrounding areas, to enhance code safety and improve the developer experience.

The current lack of type hints in PyBaMM creates several challenges. Silent failures in the validation of model arguments often only surface at runtime, making debugging difficult and time-consuming. New contributors frequently struggle to understand the expected input and output types for functions and methods, leading to a steeper learning curve. This absence also limits IDE support for code completion and error detection, making model development less efficient for researchers. Additionally, maintaining API consistency across different parts of the API becomes more challenging without clear type definitions, and numerical operations can fail unexpectedly due to unclear data type expectations.

Hence, this project seeks to implement a comprehensive typing system to improve PyBaMM's codebase. By enhancing code reliability through static type checking, we can catch errors earlier in the development process. The addition of clear type signatures will serve as implicit documentation, making the codebase more accessible to new contributors. This improvement in tooling support will accelerate development workflows and make maintenance and refactoring tasks more manageable. Furthermore, the typing system will facilitate better integration with downstream scientific libraries that rely on PyBaMM, such as PyBOP and other upcoming projects.

The scope could be expanded to include more sophisticated items towards a stretch goal if time permits. This might include creating separate type stub files for improved modularity, developing custom types for battery-specific validation, and extending type coverage to additional modules beyond the core models.

### Technical details

The implementation of the typing system will require careful evaluation of different approaches by the student, and they can explore either inline type hints in existing code, or separate `.pyi` stub files for backward compatibility, or the creation of a standalone `pybamm-stubs` package, or potentially a hybrid approach combining multiple methods. Each approach has its own trade-offs in terms of maintenance burden, backward compatibility, and ease of implementation – the student is expected to survey the existing strategy adopted by Scientific Python libraries and choose the most suitable approach for PyBaMM.

Previously, type hints were added to the expression tree via [pybamm-team/pybamm#3578](https://github.com/pybamm-team/PyBaMM/issues/3578), which can serve as a reference for the student.

The type system design will require particular attention to several key areas. The student may need to create custom types for battery-specific parameters, ensuring they accurately represent the domain concepts. The system must handle NumPy array types and dimensional analysis effectively, define clear type hierarchies for different battery models, and manage type compatibility with scientific computing libraries. The implementation of generic types for flexible model arguments will also prove to be essential for maintaining the PyBaMM framework's versatility.

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

## Mutation testing PyBaMM with mutmut

Mutation testing checks your tests' effectiveness by making minor modifications to the codebase and running the test suite. The tests are not specific or good enough if they pass with the changes made by the mutation testing framework. [mutmut](https://mutmut.readthedocs.io) is a mutation testing library for Python that has recently been adopted in testing suite of large projects.

PyBaMM (Python Battery Mathematical Modelling) has a considerably huge testing suite, which often ends up having weak or flaky tests that bump up the coverage but do not test the code thoroughly. Mutation testing would be an effective way to check whether the tests work. Moreover, this is an exploratory project, and the mentee will actively make design decisions that will pave the way for either adoption or rejection of occasional mutation testing of PyBaMM. Finally, the mentee will be guided by the mentors to fix the problems identified by mutmut, thus making the test suite better with each run.

### Technical details

mutmut is an intelligent testing framework with a browser/terminal TUI making it easy to identify "mutants" and apply them using simple commands. The library also remembers the tests that have been checked so that you can fix them incrementally. The mentee will need to use the browser/terminal TUI interactively, find bad tests, report them, and possibly fix them.

mutmut can also execute tests smartly and parallelly, making the execution fast. Once the mentee is familiar with the entire workflow, they can utilize the parallel execution capabilities to speed up the workflow and report failures quickly.

### Expected outcomes

- Testing report: An iterative report showcasing which tests are good and which tests are bad

- Fixed tests: The problems pointed out by mutmut are fixed iteratively

- Validation: CI passes on each pull request and the coverage does not go down; tests look more maintainable for the longer run (that is, they are easier to extend or debug)

### Desired skills

- Some experience with unit testing in Python
- Python programming experience, Git version control, and GitHub workflow for open-source projects
- An affinity for experimenting with new testing and infrastructure tools
- Some understanding of continuous integration providers (GitHub Actions, etc.) and mutation testing is beneficial, but not required

### Difficulty

**Moderate**. This project is suitable for a 175-hour duration.

### Potential mentors

* [Saransh Chopra](https://Saransh-cpp.github.io/)

<!-- * [Pradyot Ranjan](https://github.com/prady0t/)
* [Agriya Khetarpal](https://github.com/agriyakhetarpal/)
* [Valentin Sulzer](https://github.com/valentinsulzer)
* [Robert Timms](https://github.com/rtimms)
* [Arjun Verma](https://arjxnpy.vercel.app/)
* [Ferran Brosa Planella](https://www.brosaplanella.xyz/) -->
