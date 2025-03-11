---
title: PyBaMM GSoC 2025 Project Ideas
summary: This page contains project ideas for PyBaMM's participation in the Google Summer of Code program in 2025. These projects are intended to be suitable for students who are new to PyBaMM or to open-source software development in general, and wish to work on a project that will be beneficial to PyBaMM and its community.
---

<!--  ## Adding type hints to PyBaMM models

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

!!Needs a primary mentor!!
* [Agriya Khetarpal](https://github.com/agriyakhetarpal/)
* [Arjun Verma](https://arjxnpy.vercel.app/)

* [Valentin Sulzer](https://github.com/valentinsulzer)
* [Robert Timms](https://github.com/rtimms)
* [Ferran Brosa Planella](https://www.brosaplanella.xyz/) -->

<hr>

## Adding a spirally wound geometry for thermal simulations in PyBaMM

With the increasing demand for high-performance batteries, accurate thermal modeling of battery behavior is essential. A key challenge is the interaction between electrochemical and thermal dynamics in complicated battery geometries, which affects performance, safety, and lifespan. This project aims to develop a framework for the addition of coupled electrochemical-thermal simulations in PyBaMM in higher-dimensional geometries (e.g. cylindrical)

This project aims to couple the electrochemical models already available in PyBaMM, such as the SPM or DFN, with a higher-dimensional thermal model. As a proof of concept, the model will be used to simulate temperature distributions throughout the cell under different operating conditions.

As a first step, a 3D thermal model will be implemented in PyBaMM with a constant heat source term. This will require adding new 3D meshes and spatial methods to PyBaMM (ideally by adding an existing 3D Finite Volume package as a dependency, such as Gmsh, Meshlib, Salome, etc). Next, this thermal model will be coupled with an electrochemical model, which will provide the heat source term. Finally, the coupling will be made two-way so that the lumped temperature from the 3D model feeds back into the electrochemical model.

As a stretch goal, the project will explore the integration of 3D temperature profiles obtained from the spirally wound 3D thermal model back into the electrochemical model. This would enable feedback coupling, where the electrochemical model depends on the temperature distribution of the 3D model, providing a foundation for more complex coupling strategies in future research.

### Expected outcomes

The expected outcome of this study is a proof-of-concept 3D thermal model implemented in PyBaMM, along with the necessary meshing and discretization capabilities. It includes a computational framework for electrochemical-thermal coupling on new cell geometries, and the implementation of a spirally wound geometry for thermal simulations in PyBaMM.

### Desired skills

- Python programming experience, Git version control, and GitHub workflow for open-source projects
- An interest in scientific computing and battery modeling
- Experience with numerical methods for solving differential equations
- Experience with meshing libraries (e.g. Finite Volumes or Finite Elements) is desirable but not required
- As a plus, knowledge of how to use scientific computing libraries (NumPy, SciPy, SUNDIALS)

### Difficulty

**Hard**. This project is suitable for a 350-hour duration.

### Potential mentors

- [Robert Timms](https://github.com/rtimms)
- [Nachiketh Grandhi](https://www.linkedin.com/in/nachiketh-grandhi-76393222a/)

<hr>

## Adding a dispatching mechanism for third-party models

With a constantly expanding user base and community, including and working with third-party battery models has become a hassle for PyBaMM users. This project aims to develop a standardized framework for the integration, distribution, and dynamic utilization of third-party battery models implemented with PyBaMM, addressing current limitations in accessibility for users with varying technical backgrounds.

This project serves as an extension of the [cookiecutter project (GSoC 2024)](https://github.com/pybamm-team/pybamm-cookie), which aimed to reduce the entry barrier for building and distributing PyBaMM projects with the community. This project will build on top of the 2024 project, aiming to establish a standardized model distribution and dispatching framework with seamless PyBaMM integration. The project will define guidelines for structuring models and documentation to facilitate easy distribution and dynamic loading of models. The models will be distributed via model [entry points](https://packaging.python.org/en/latest/specifications/entry-points/) through a new dispatching API for PyBaMM.

Additionally, the mentee may need to enhance the [existing `copier` template](https://github.com/pybamm-team/pybamm-cookie) to enforce standardized plugin structures for third-party models, as a parallel primary goal of this project. The packaging and distribution system of the template will be refactored to comply with the new model entry points/dispatch API of PyBaMM. To streamline model retrieval, the mentee will have to design a system incorporating a serverless indexing mechanism for pulling third-party models using the PyBaMM third-party model registries, the registries would contain compatibility and constraint scope. The project will also implement caching and lazy loading mechanisms to optimize performance as a stretch goal. Read [fsspec](https://filesystem-spec.readthedocs.io/en/latest/features.html) for reference.

The student will have an opportunity to learn software engineering with Python, including adding features, writing tests, writing user-facing documentation, designing examples, and building CI/CD pipelines. Additionally, their work will be a significant open-source contribution to scientific computing and and expanding battery modeling research as it will create an easy to use PyBaMM development ecosystem that any researcher could adopt, modify and distribute.

### Expected Outcomes

- A dispatch API that could pass parameters/arguments from PyBaMM to third-party models for seamless integration. The dispatch API would also serve as a mechanism for setting constraints and compatibility checks to verify the parameters before passing them to the loaded model.
- A centralized model registry where constraints for different models can be set up. The constraints in the registry can be defined as JSON or through a configuration file defining information about the model. These constraints should be pre-loaded for checks before loading the model itself.
- Refactored entry points API to accommodate the dispatch API. The entry point would also serve as a loader for these third-party models that are not contained within PyBaMM, collectively, the entry points API and the dispatch API will form a framework for integrating, packaging, and distributing battery models amongst PyBaMM users.
- Updates to the copier template, making it compatible with the new dispatch API, simplifying the setup processes for writing custom models, and better project generation support.
- An effective user experience for using third-party PyBaMM models.
- A detailed and easy to read guide and documentation on building and distributing custom PyBaMM models.
- A caching and lazy loading mechanism for the entry points for efficiency.

### Desired Skills

- Python programming experience, Git version control, and GitHub workflow for open-source projects
- Experience with implementing entry points, building and distributing pure-Python packages is beneficial but not required
- Familiarity with `cookiecutter`/`copier` templates and their templating engines
- An interest in scientific computing and battery modeling

### Difficulty

**Medium**. This project is suitable for a 350-hour duration.

### Potential mentors

- [Santhosh Sundaram](https://github.com/santacodes)
- [Valentin Sulzer](https://sites.google.com/view/valentinsulzer)
- [Agriya Khetarpal](https://github.com/agriyakhetarpal)

### References for custom models and entry points API in PyBaMM
- https://docs.pybamm.org/en/v22.8/tutorials/add-model.html
- https://train.rse.ox.ac.uk/material/HPCu/libraries/pybamm
- [WIP] https://github.com/pybamm-team/PyBaMM/pull/4490

### References from other sources and attributions
This project is inspired by the ongoing dispatching efforts in projects like NetworkX and scikit-image. NetworkX focuses on dispatching graph algorithms across different backends, while scikit-image aims to dispatch public API functions that perform specific image processing tasks. In contrast, our approach involves dispatching an entire model class—along with its public and private attributes—to another, making our implementation distinct. The student working on this project is encouraged to bring their ideas to the table and not restrict themselves to this description.

- https://scientific-python.org/specs/spec-0002/
- https://networkx.org/documentation/latest/reference/backends.html
- https://github.com/scikit-learn/scikit-learn/pull/25535

<hr>

## Open project idea(s)

We are also open to the inclusion of open project ideas for PyBaMM and candidates are encouraged to propose their own projects, if they feel at any time that our idea list does not currently cater to their interests and passions. If you have a project idea that you think would be beneficial to PyBaMM and its community, please feel free to reach out to us on our [Slack workspace](https://pybamm.org/slack/) in the `#gsoc-main` channel.

The project should be validated by getting in touch with potential mentors early, publicly, to ensure that its goals are realistic and within the scope of PyBaMM's roadmap, i.e., the project should also be beneficial to the PyBaMM community and should be able to be completed within the GSoC timeline.

The requirements for the inclusion of said project must include:

- A mentor within the PyBaMM maintainers team and the greater community who would be available and willing to support the project with code reviews, frequent meetings decided at a time with you during the coding period, and by offering general guidance and feedback within the scope of mentorship.
- A clear project description, including the expected outcomes, the technical details, the desired skills, and the difficulty level of the project, similar to the project ideas listed on this page.
- Proposed project length and timeline, including milestones and deliverables, which should be clearly defined and agreed upon by the mentor and the student (you). It should be either a **175-hour** or **350-hour** project, and not any other duration.
