---
Title: Ankit Meda — Google Summer of Code 2024 Final Report
Subtitle: Migrate to `scikit-build-core`
Summary: This is the final report for Ankit Meda's Google Summer of Code 2023 project with PyBaMM, NumFOCUS. I worked on migrating PyBaMM's build backend to `scikit-build-core`.
Date: 2024-08-26
ShortcutDepth: 2
---

[![Google Summer of Code](https://img.shields.io/badge/Google_Summer_of_Code-2024-fbbd05?colorA=565656&logo=data:image/svg+xml;base64,PD94bWwgdmVyc2lvbj0iMS4wIiBlbmNvZGluZz0idXRmLTgiPz4KPCEtLSBHZW5lcmF0b3I6IEFkb2JlIElsbHVzdHJhdG9yIDE5LjIuMSwgU1ZHIEV4cG9ydCBQbHVnLUluIC4gU1ZHIFZlcnNpb246IDYuMDAgQnVpbGQgMCkgIC0tPgo8c3ZnIHZlcnNpb249IjEuMSIgaWQ9IkxheWVyXzExIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHhtbG5zOnhsaW5rPSJodHRwOi8vd3d3LnczLm9yZy8xOTk5L3hsaW5rIiB4PSIwcHgiIHk9IjBweCIKCSB2aWV3Qm94PSIwIDAgMTkyIDE5MiIgc3R5bGU9ImVuYWJsZS1iYWNrZ3JvdW5kOm5ldyAwIDAgMTkyIDE5MjsiIHhtbDpzcGFjZT0icHJlc2VydmUiPgo8c3R5bGUgdHlwZT0idGV4dC9jc3MiPgoJLnN0MHtmaWxsOiNGQkJDMDU7fQo8L3N0eWxlPgo8Zz4KCTxwYXRoIGNsYXNzPSJzdDAiIGQ9Ik0xNTguMSwzMy43aC0zNi40TDk2LDhMNzAuMywzMy43SDMzLjl2MzYuNEw4LjIsOTUuOWwyNS43LDI1LjdWMTU4aDM2LjRMOTYsMTgzLjdsMjUuNy0yNS43aDM2LjR2LTM2LjQKCQlsMjUuNy0yNS43bC0yNS43LTI1LjdWMzMuN3ogTTE1OC43LDk1LjljMCwzNC42LTI4LjEsNjIuNy02Mi43LDYyLjdzLTYyLjctMjguMS02Mi43LTYyLjdTNjEuNCwzMy4yLDk2LDMzLjIKCQlTMTU4LjcsNjEuMywxNTguNyw5NS45eiIvPgoJPHBhdGggY2xhc3M9InN0MCIgZD0iTTk2LDQxLjJjLTMwLjIsMC01NC43LDI0LjUtNTQuNyw1NC43YzAsMzAuMiwyNC41LDU0LjcsNTQuNyw1NC43YzMwLjIsMCw1NC43LTI0LjUsNTQuNy01NC43CgkJQzE1MC43LDY1LjcsMTI2LjIsNDEuMiw5Niw0MS4yeiBNNzkuOSw3NS42djlMNjUuNCw5NS45bDE0LjUsMTEuM3Y5bC0xLTAuN0w1Ny40LDk4LjdMNTYsOTcuNnYtMy40bDEuNC0xLjFsMjEuNS0xNi43TDc5LjksNzUuNgoJCUw3OS45LDc1LjZ6IE0xMDUuNyw3MC40TDkzLjgsMTIzbC0wLjEsMC40aC03LjRsMC40LTJsMTEuOS01Mi41bDAuMS0wLjRoNy40TDEwNS43LDcwLjR6IE0xMzYsOTcuNmwtMS40LDEuMUwxMTMsMTE1LjRsLTEsMC43di05CgkJbDE0LjUtMTEuM2wtMTQuNS0xMS4zdi05djBsMSwwLjdMMTM0LjUsOTNsMS40LDEuMVY5Ny42eiIvPgo8L2c+Cjwvc3ZnPgo=)]( https://g.co/gsoc )
[![NumFOCUS](https://img.shields.io/badge/organisation-NumFOCUS-orange.svg?style=flat&colorA=007D8A&colorB=E1523D&logo=data:image/png;base64,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)]( https://numfocus.org )
[![PyBaMM](https://img.shields.io/badge/sub%E2%80%93organisation-PyBaMM-blue?logo=data:image/svg+xml;base64,PHN2ZyBpZD0iTGF5ZXJfMSIgZGF0YS1uYW1lPSJMYXllciAxIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHhtbG5zOnhsaW5rPSJodHRwOi8vd3d3LnczLm9yZy8xOTk5L3hsaW5rIiB2aWV3Qm94PSIwIDAgMTc0IDIwMCI+PGRlZnM+PHN0eWxlPi5jbHMtMXtmaWxsOnVybCgjbGluZWFyLWdyYWRpZW50KTt9LmNscy0ye2ZpbGw6dXJsKCNsaW5lYXItZ3JhZGllbnQtMik7fS5jbHMtM3tmaWxsOiMyNDRmNzI7fS5jbHMtNHtmaWxsOnVybCgjbGluZWFyLWdyYWRpZW50LTMpO30uY2xzLTV7ZmlsbDp1cmwoI2xpbmVhci1ncmFkaWVudC00KTt9LmNscy02e2ZpbGw6dXJsKCNsaW5lYXItZ3JhZGllbnQtNSk7fS5jbHMtN3tmaWxsOnVybCgjbGluZWFyLWdyYWRpZW50LTYpO308L3N0eWxlPjxsaW5lYXJHcmFkaWVudCBpZD0ibGluZWFyLWdyYWRpZW50IiB4MT0iNDguMDMiIHkxPSI0Ny41IiB4Mj0iMTc3LjkzIiB5Mj0iMTIyLjUiIGdyYWRpZW50VW5pdHM9InVzZXJTcGFjZU9uVXNlIj48c3RvcCBvZmZzZXQ9IjAiIHN0b3AtY29sb3I9IiNmZmQ0M2IiLz48c3RvcCBvZmZzZXQ9IjEiIHN0b3AtY29sb3I9IiNmZmU4NzMiLz48L2xpbmVhckdyYWRpZW50PjxsaW5lYXJHcmFkaWVudCBpZD0ibGluZWFyLWdyYWRpZW50LTIiIHgxPSIxMy4zOSIgeTE9IjY3LjUiIHgyPSIxNDMuMjkiIHkyPSIxNDIuNSIgeGxpbms6aHJlZj0iI2xpbmVhci1ncmFkaWVudCIvPjxsaW5lYXJHcmFkaWVudCBpZD0ibGluZWFyLWdyYWRpZW50LTMiIHgxPSIwLjQiIHkxPSIxMjUiIHgyPSI4NyIgeTI9IjEyNSIgZ3JhZGllbnRVbml0cz0idXNlclNwYWNlT25Vc2UiPjxzdG9wIG9mZnNldD0iMCIgc3RvcC1jb2xvcj0iIzMwNjk5OCIvPjxzdG9wIG9mZnNldD0iMSIgc3RvcC1jb2xvcj0iIzRiOGJiZSIvPjwvbGluZWFyR3JhZGllbnQ+PGxpbmVhckdyYWRpZW50IGlkPSJsaW5lYXItZ3JhZGllbnQtNCIgeDE9IjE2OS4yNyIgeTE9IjU3LjUiIHgyPSI3NC4wMSIgeTI9IjIuNSIgZ3JhZGllbnRVbml0cz0idXNlclNwYWNlT25Vc2UiPjxzdG9wIG9mZnNldD0iMCIgc3RvcC1jb2xvcj0iIzZmYTJjYiIvPjxzdG9wIG9mZnNldD0iMSIgc3RvcC1jb2xvcj0iIzRiOGJiZSIvPjwvbGluZWFyR3JhZGllbnQ+PGxpbmVhckdyYWRpZW50IGlkPSJsaW5lYXItZ3JhZGllbnQtNSIgeDE9IjEzNC42MyIgeTE9Ijc3LjUiIHgyPSIzOS4zNyIgeTI9IjIyLjUiIHhsaW5rOmhyZWY9IiNsaW5lYXItZ3JhZGllbnQtNCIvPjxsaW5lYXJHcmFkaWVudCBpZD0ibGluZWFyLWdyYWRpZW50LTYiIHgxPSI5OS45OSIgeTE9Ijk3LjUiIHgyPSI0LjczIiB5Mj0iNDIuNSIgeGxpbms6aHJlZj0iI2xpbmVhci1ncmFkaWVudC00Ii8+PC9kZWZzPjxwb2x5Z29uIGNsYXNzPSJjbHMtMSIgcG9pbnRzPSIxNTYuMjggMTYwIDY5LjY4IDExMCA2OS42OCAxMCAxNTYuMjggNjAgMTU2LjI4IDE2MCIvPjxwb2x5Z29uIGNsYXNzPSJjbHMtMiIgcG9pbnRzPSIxMjEuNjQgMTgwIDM1LjA0IDEzMCAzNS4wNCAzMCAxMjEuNjQgODAgMTIxLjY0IDE4MCIvPjxwb2x5Z29uIGNsYXNzPSJjbHMtMyIgcG9pbnRzPSIxNTYuMjggMTYwIDE1Ni4yOCA2MCAxNzMuNiA1MCAxNzMuNiAxNTAgMTU2LjI4IDE2MCIvPjxwb2x5Z29uIGNsYXNzPSJjbHMtMyIgcG9pbnRzPSIxMjEuNjQgMTgwIDEyMS42NCA4MCAxMzguOTYgNzAgMTM4Ljk2IDE3MCAxMjEuNjQgMTgwIi8+PHBvbHlnb24gY2xhc3M9ImNscy0zIiBwb2ludHM9Ijg3IDIwMCA4NyAxMDAgMTA0LjMyIDkwIDEwNC4zMiAxOTAgODcgMjAwIi8+PHBvbHlnb24gY2xhc3M9ImNscy00IiBwb2ludHM9Ijg3IDIwMCAwLjQgMTUwIDAuNCA1MCA4NyAxMDAgODcgMjAwIi8+PHBvbHlnb24gY2xhc3M9ImNscy01IiBwb2ludHM9IjY5LjY4IDEwIDE1Ni4yOCA2MCAxNzMuNiA1MCA4NyAwIDY5LjY4IDEwIi8+PHBvbHlnb24gY2xhc3M9ImNscy02IiBwb2ludHM9IjM1LjA0IDMwIDEyMS42NCA4MCAxMzguOTYgNzAgNTIuMzYgMjAgMzUuMDQgMzAiLz48cG9seWdvbiBjbGFzcz0iY2xzLTciIHBvaW50cz0iMC40IDUwIDg3IDEwMCAxMDQuMzIgOTAgMTcuNzIgNDAgMC40IDUwIi8+PC9zdmc+Cg==)]( https://pybamm.org )

[![Blogs](https://img.shields.io/badge/Hashnode-2962FF?style=for-the-badge&logo=hashnode&logoColor=white)]( https://ankittriesblogging.hashnode.dev/ )
[![Project page on the Google Summer of Code website](https://img.shields.io/badge/%20view%20project%20-darkmagenta)]( https://summerofcode.withgoogle.com/programs/2024/projects/YyLzWWqr )
[![Proposal on Google Docs](https://img.shields.io/badge/%20view%20proposal%20-palevioletred)]( https://docs.google.com/document/d/1U-oFjZutIhSVkKv-cHOQ8snQlOkr3YLZSJUEzZ2P86g/edit?usp=sharing )

<br>

[![View my GitHub profile](https://img.shields.io/badge/GitHub-100000?style=flat&logo=github&logoColor=white)]( https://github.com/cringeyburger )
[![View my LinkedIn profile](https://img.shields.io/badge/LinkedIn-0077B5?style=linkedin&logo=linkedin&logoColor=white)]( https://www.linkedin.com/in/ankit-meda/ )

---

This page serves as a permalink to the final report that provides details of Ankit Meda’s project in the Google Summer of Code 2024 programme.

## 📖 TL; DR

During the community bonding and coding periods, I accomplished several key tasks that contributed to the overall success of the project:

- **Migrated Build Backend:** Transitioned the build backend from `setuptools` and `wheel` to `scikit-build-core`, improving flexibility.
- **Cross-Platform Support:** Ensured continued support for all platforms, including Windows, macOS, Linux, and Docker builds.
- **Revamped Installation Instructions:** Updated the installation guide, including a comprehensive new section on installing PyBaMM from source on a native Windows platform.
- **Custom Library Installation:** Enabled users to install `SUNDIALS` and `SuiteSparse` libraries in custom directories, enhancing flexibility.
- **Proof of Concept for `ccache` Integration:** Developed and tested a proof of concept for integrating `ccache` to optimize build times on local systems and CI builds.
- **Streamlined CI Workflows:** Simplified and optimized CI test and build workflows for greater efficiency.
- **Enabled Editable-Partial Rebuilds:** Implemented support for editable-partial rebuilds, significantly speeding up the development process.
- **Updated Build Scripts:** Modified build scripts to align with the new build process, ensuring smooth integration and operation.

## 🔋 About PyBaMM

PyBaMM is an open-source Python package for the mathematical modelling of batteries and running fast, flexible, and accurate simulations for myriads of battery models. Its mission is to accelerate battery modelling research by providing open-source tools for multi-institutional, interdisciplinary collaboration; it is fiscally sponsored by NumFOCUS and The Faraday Institution in the U.K. The use of the software in academia and industry has been prolific since its inception—it has been used at a multitude of universities, research institutions, and commercial research labs in collaborative settings.

## 📄 Project abstract

The primary goal of this project was to transition PyBaMM’s build system from the traditional `setuptools` and `wheel` setup to the more modern and flexible `scikit-build-core`. This migration involved not only deprecating the old build system but also enhancing build configurations, writing new scripts, and updating existing ones to comply with the conventions of `scikit-build-core`. Ensuring compatibility across all supported platforms and architectures was a key focus, guaranteeing that PyBaMM operates seamlessly regardless of the environment. Additionally, significant improvements were made to the CI tests and build processes to align them with the new build system, ensuring reliable continuous integration.

### 🚀 Motivation

The motivation behind migrating PyBaMM’s build system to `scikit-build-core` stems from the need to adopt a more modern, efficient, and reliable build infrastructure. The new build backend offers several significant advantages:

- **Enhanced Compiler Support and Usability:** `scikit-build-core` provides better support for various compilers, making it easier to manage and build the project across different environments. This is crucial for a project like PyBaMM that supports multiple platforms, including Windows, macOS, Linux, and Docker.
- **Reliable Build Caching:** The new system includes reliable build caching mechanisms that significantly reduce installation times. This improvement is particularly beneficial for continuous integration workflows and for developers working on frequent updates.
- **Alignment with the Scientific Python Ecosystem:** As the broader Scientific Python community gradually migrates to modern build systems, it is essential for PyBaMM to keep pace. This transition ensures compatibility with future ecosystem developments and maintains PyBaMM's relevance in the scientific computing domain.

### 🍀 Benefits to the community

The migration of PyBaMM’s build system to `scikit-build-core` brings several key benefits to the broader community, enhancing both the user and developer experience. The new build system ensures that PyBaMM remains fully compatible with all major platforms — Windows, macOS, Linux, and Docker. This broad support enables a wider range of users to seamlessly install and use PyBaMM in their preferred environments, fostering greater adoption. With the introduction of reliable build caching, users can expect significantly faster installation and compilation times.

Developers contributing to PyBaMM will benefit from the modern build infrastructure, which offers better compiler support and simplified build scripts. These improvements make the development process more efficient, lowering the barrier to entry for new contributors and encouraging more community involvement.
As packagers and libraries in the Scientific Python ecosystem transition to modern build systems like `scikit-build-core`, PyBaMM’s migration ensures continued compatibility and alignment with the latest industry standards. This forward-looking approach positions PyBaMM to integrate smoothly with other scientific tools and libraries, enhancing its utility and interoperability within the scientific community.

## 🧑‍💻 Work done

The first significant milestone was the successful migration of PyBaMM’s build system from `setuptools` and `wheel` to `scikit-build-core`. This involved a thorough overhaul of the `pyproject.toml` configuration in alignment with the new build system’s conventions for compilation and linkage. After this, extensive testing was conducted locally and on continuous integration (CI) platforms, including updating GitHub CI workflows, dependencies, and build commands.

Next, attention was turned to improving the installation process for the `SUNDIALS` and `SuiteSparse` libraries. The fixed installation location was transitioned from `~/.local` to a more organized structure within the project directory under `sundials_KLU_libs`. Users were given the option to install the libraries in a custom directory by exporting the `INSTALL_DIR` environment variable to the location of the custom directory. This required updating the build configuration to ensure CMake could correctly locate and recognize the libraries in their new location.

Subsequently, adjustments were made to the `nox` session commands to accommodate the new build system. The introduction of `tomlkit`, a TOML table parser, was a critical enhancement that facilitated the installation of build-time dependencies during editable-rebuilds, ensuring a smooth development workflow with no build isolation.

Following these changes, improvements were made to the CI testing process. Ensuring that all previously functioning tests continued to work seamlessly under the new build system was a straightforward but essential task.

Finally, the focus shifted to optimizing the benchmarks. By leveraging the custom `SUNDIALS` installation option through the `INSTALL_DIR` environment variable, necessary adjustments for benchmarks were efficiently implemented, ensuring the benchmarks operated as expected under the new system.

## 📑 A list of issues opened and pull requests submitted

This list includes both issues and pull requests related to my project, such as infrastructure improvements, documentation enhancements, general bug fixes, and other refinements.

### 🛠️ Issues


- ([pybamm-team/PyBaMM #3564](https://github.com/pybamm-team/PyBaMM/issues/3564))                         Tracking issue: migrate to `scikit-build-core`
- ([pybamm-team/PyBaMM #4101](https://github.com/pybamm-team/PyBaMM/pull/4101))                         Included `CMakeLists.txt`

### 👷 Pull requests


- ([pybamm-team/PyBaMM #3044](https://github.com/pybamm-team/PyBaMM/pull/4242))                         `scikit-build-core` CI Builds (draft)
- ([pybamm-team/PyBaMM #3082](https://github.com/pybamm-team/PyBaMM/pull/4352))                         Migrate to `scikit-build-core`

## 🔮 Future work

- **Extension of Support to ARM-Based Linux Platforms:** To increase the portability and accessibility of the software, one key area of future work is extending support to ARM-based Linux platforms. This will involve configuring and testing the build system to ensure compatibility with ARM architecture, particularly focusing on optimizing performance for ARM CPUs.

- **Enhanced CI Workflows with `ccache` for Faster Builds:** To improve the efficiency of the continuous integration (CI) pipelines, implementing `ccache` within the CI workflows will be essential. `ccache` caches previous compilations, which significantly reduces build times by avoiding redundant compilations of unchanged code.

- **Custom vcpkg Registry for SuiteSparse Using OpenBLAS:** Currently, SuiteSparse relies on LAPACK, but transitioning to a custom `vcpkg` registry that uses OpenBLAS instead could lead to performance improvements, especially on systems where OpenBLAS is better optimized. Future work will involve creating and maintaining this custom registry, ensuring that it seamlessly integrates with the existing build system.

## Acknowledgements

I want to thank everyone who has participated in this transformative experience over the summer. First and foremost, I am deeply thankful to Google Summer of Code, NumFOCUS, and the PyBaMM team for providing me with this extraordinary opportunity. This experience has enhanced my skills, and I gained hands-on knowledge in open-source software development.

Contributing to the development of open-source scientific software has been incredibly rewarding. The insights and knowledge I have gained throughout this journey are truly invaluable.

I am immensely grateful to my mentors, [Agriya Khetarpal](https://github.com/agriyakhetarpal), [Arjun Verma](https://github.com/arjxn-py), and [Saransh Chopra](https://github.com/Saransh-cpp), for their unwavering support, patience, and guidance throughout the project. Their expertise and feedback were instrumental in overcoming challenges and achieving our objectives.
I thoroughly enjoyed discussing my project with fellow GSoC student [Santhosh](https://github.com/santacodes). His support and insights were greatly appreciated, and our conversations were both enriching and encouraging.
I also thank [Eric G. Kratz](https://github.com/kratman) for his review of my work and for offering valuable insights.

Thank you all for your encouragement and dedication throughout this project.

## 🔭 References

- The GitHub repository for PyBaMM: https://github.com/pybamm-team/PyBaMM
- The PyBaMM documentation: https://docs.pybamm.org
- The GitHub repository for `scikit-build-core`: https://scikit-build-core.readthedocs.io/en/stable/getting_started.html
