---
title: "Arjun Verma — Google Summer of Code 2023 Final Report"
subtitle: "Dockerizing & Simplifying PyBaMM's Installation"
summary: "This is the final report for Arjun Verma's Google Summer of Code 2023 project with PyBaMM, NumFOCUS. I worked on Dockerizing & Simplifying PyBaMM's Installation."
date: 2023-08-22
shortcutDepth: 2
# WARNING: THE LINK TO THIS PAGE SHOULD NEVER BE CHANGED WITHOUT THE EXISTENCE OF A HUGO PERMALINK, AN ALIAS IN THE FRONTMATTER, OR WITHOUT THE EXISTENCE OF A PERMANENT (STATUS CODE 301) REDIRECTION RULE IN THE _redirects FILE AND A CORRESPONDING ENTRY IN THE netlify.toml FILE. THIS IS TO ENSURE THAT THE LINK TO THIS PAGE IS NEVER BROKEN SINCE IT ACCOUNTS FOR ARJUN VERMA'S GSoC 2023 FINAL REPORT AND IS LINKED TO FROM THE GOOGLE SUMMER OF CODE WEBSITE AS THE WORK PRODUCT SUBMISSION.
---

[![Google Summer of Code](https://img.shields.io/badge/Google_Summer_of_Code-2023-fbbd05?colorA=565656&logo=data:image/svg+xml;base64,PD94bWwgdmVyc2lvbj0iMS4wIiBlbmNvZGluZz0idXRmLTgiPz4KPCEtLSBHZW5lcmF0b3I6IEFkb2JlIElsbHVzdHJhdG9yIDE5LjIuMSwgU1ZHIEV4cG9ydCBQbHVnLUluIC4gU1ZHIFZlcnNpb246IDYuMDAgQnVpbGQgMCkgIC0tPgo8c3ZnIHZlcnNpb249IjEuMSIgaWQ9IkxheWVyXzExIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHhtbG5zOnhsaW5rPSJodHRwOi8vd3d3LnczLm9yZy8xOTk5L3hsaW5rIiB4PSIwcHgiIHk9IjBweCIKCSB2aWV3Qm94PSIwIDAgMTkyIDE5MiIgc3R5bGU9ImVuYWJsZS1iYWNrZ3JvdW5kOm5ldyAwIDAgMTkyIDE5MjsiIHhtbDpzcGFjZT0icHJlc2VydmUiPgo8c3R5bGUgdHlwZT0idGV4dC9jc3MiPgoJLnN0MHtmaWxsOiNGQkJDMDU7fQo8L3N0eWxlPgo8Zz4KCTxwYXRoIGNsYXNzPSJzdDAiIGQ9Ik0xNTguMSwzMy43aC0zNi40TDk2LDhMNzAuMywzMy43SDMzLjl2MzYuNEw4LjIsOTUuOWwyNS43LDI1LjdWMTU4aDM2LjRMOTYsMTgzLjdsMjUuNy0yNS43aDM2LjR2LTM2LjQKCQlsMjUuNy0yNS43bC0yNS43LTI1LjdWMzMuN3ogTTE1OC43LDk1LjljMCwzNC42LTI4LjEsNjIuNy02Mi43LDYyLjdzLTYyLjctMjguMS02Mi43LTYyLjdTNjEuNCwzMy4yLDk2LDMzLjIKCQlTMTU4LjcsNjEuMywxNTguNyw5NS45eiIvPgoJPHBhdGggY2xhc3M9InN0MCIgZD0iTTk2LDQxLjJjLTMwLjIsMC01NC43LDI0LjUtNTQuNyw1NC43YzAsMzAuMiwyNC41LDU0LjcsNTQuNyw1NC43YzMwLjIsMCw1NC43LTI0LjUsNTQuNy01NC43CgkJQzE1MC43LDY1LjcsMTI2LjIsNDEuMiw5Niw0MS4yeiBNNzkuOSw3NS42djlMNjUuNCw5NS45bDE0LjUsMTEuM3Y5bC0xLTAuN0w1Ny40LDk4LjdMNTYsOTcuNnYtMy40bDEuNC0xLjFsMjEuNS0xNi43TDc5LjksNzUuNgoJCUw3OS45LDc1LjZ6IE0xMDUuNyw3MC40TDkzLjgsMTIzbC0wLjEsMC40aC03LjRsMC40LTJsMTEuOS01Mi41bDAuMS0wLjRoNy40TDEwNS43LDcwLjR6IE0xMzYsOTcuNmwtMS40LDEuMUwxMTMsMTE1LjRsLTEsMC43di05CgkJbDE0LjUtMTEuM2wtMTQuNS0xMS4zdi05djBsMSwwLjdMMTM0LjUsOTNsMS40LDEuMVY5Ny42eiIvPgo8L2c+Cjwvc3ZnPgo=)](https://g.co/gsoc)
[![NumFOCUS](https://img.shields.io/badge/organisation-NumFOCUS-orange.svg?style=flat&colorA=007D8A&colorB=E1523D&logo=data:image/png;base64,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)](https://numfocus.org)
[![PyBaMM](https://img.shields.io/badge/sub%E2%80%93organisation-PyBaMM-blue?logo=data:image/svg+xml;base64,PHN2ZyBpZD0iTGF5ZXJfMSIgZGF0YS1uYW1lPSJMYXllciAxIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHhtbG5zOnhsaW5rPSJodHRwOi8vd3d3LnczLm9yZy8xOTk5L3hsaW5rIiB2aWV3Qm94PSIwIDAgMTc0IDIwMCI+PGRlZnM+PHN0eWxlPi5jbHMtMXtmaWxsOnVybCgjbGluZWFyLWdyYWRpZW50KTt9LmNscy0ye2ZpbGw6dXJsKCNsaW5lYXItZ3JhZGllbnQtMik7fS5jbHMtM3tmaWxsOiMyNDRmNzI7fS5jbHMtNHtmaWxsOnVybCgjbGluZWFyLWdyYWRpZW50LTMpO30uY2xzLTV7ZmlsbDp1cmwoI2xpbmVhci1ncmFkaWVudC00KTt9LmNscy02e2ZpbGw6dXJsKCNsaW5lYXItZ3JhZGllbnQtNSk7fS5jbHMtN3tmaWxsOnVybCgjbGluZWFyLWdyYWRpZW50LTYpO308L3N0eWxlPjxsaW5lYXJHcmFkaWVudCBpZD0ibGluZWFyLWdyYWRpZW50IiB4MT0iNDguMDMiIHkxPSI0Ny41IiB4Mj0iMTc3LjkzIiB5Mj0iMTIyLjUiIGdyYWRpZW50VW5pdHM9InVzZXJTcGFjZU9uVXNlIj48c3RvcCBvZmZzZXQ9IjAiIHN0b3AtY29sb3I9IiNmZmQ0M2IiLz48c3RvcCBvZmZzZXQ9IjEiIHN0b3AtY29sb3I9IiNmZmU4NzMiLz48L2xpbmVhckdyYWRpZW50PjxsaW5lYXJHcmFkaWVudCBpZD0ibGluZWFyLWdyYWRpZW50LTIiIHgxPSIxMy4zOSIgeTE9IjY3LjUiIHgyPSIxNDMuMjkiIHkyPSIxNDIuNSIgeGxpbms6aHJlZj0iI2xpbmVhci1ncmFkaWVudCIvPjxsaW5lYXJHcmFkaWVudCBpZD0ibGluZWFyLWdyYWRpZW50LTMiIHgxPSIwLjQiIHkxPSIxMjUiIHgyPSI4NyIgeTI9IjEyNSIgZ3JhZGllbnRVbml0cz0idXNlclNwYWNlT25Vc2UiPjxzdG9wIG9mZnNldD0iMCIgc3RvcC1jb2xvcj0iIzMwNjk5OCIvPjxzdG9wIG9mZnNldD0iMSIgc3RvcC1jb2xvcj0iIzRiOGJiZSIvPjwvbGluZWFyR3JhZGllbnQ+PGxpbmVhckdyYWRpZW50IGlkPSJsaW5lYXItZ3JhZGllbnQtNCIgeDE9IjE2OS4yNyIgeTE9IjU3LjUiIHgyPSI3NC4wMSIgeTI9IjIuNSIgZ3JhZGllbnRVbml0cz0idXNlclNwYWNlT25Vc2UiPjxzdG9wIG9mZnNldD0iMCIgc3RvcC1jb2xvcj0iIzZmYTJjYiIvPjxzdG9wIG9mZnNldD0iMSIgc3RvcC1jb2xvcj0iIzRiOGJiZSIvPjwvbGluZWFyR3JhZGllbnQ+PGxpbmVhckdyYWRpZW50IGlkPSJsaW5lYXItZ3JhZGllbnQtNSIgeDE9IjEzNC42MyIgeTE9Ijc3LjUiIHgyPSIzOS4zNyIgeTI9IjIyLjUiIHhsaW5rOmhyZWY9IiNsaW5lYXItZ3JhZGllbnQtNCIvPjxsaW5lYXJHcmFkaWVudCBpZD0ibGluZWFyLWdyYWRpZW50LTYiIHgxPSI5OS45OSIgeTE9Ijk3LjUiIHgyPSI0LjczIiB5Mj0iNDIuNSIgeGxpbms6aHJlZj0iI2xpbmVhci1ncmFkaWVudC00Ii8+PC9kZWZzPjxwb2x5Z29uIGNsYXNzPSJjbHMtMSIgcG9pbnRzPSIxNTYuMjggMTYwIDY5LjY4IDExMCA2OS42OCAxMCAxNTYuMjggNjAgMTU2LjI4IDE2MCIvPjxwb2x5Z29uIGNsYXNzPSJjbHMtMiIgcG9pbnRzPSIxMjEuNjQgMTgwIDM1LjA0IDEzMCAzNS4wNCAzMCAxMjEuNjQgODAgMTIxLjY0IDE4MCIvPjxwb2x5Z29uIGNsYXNzPSJjbHMtMyIgcG9pbnRzPSIxNTYuMjggMTYwIDE1Ni4yOCA2MCAxNzMuNiA1MCAxNzMuNiAxNTAgMTU2LjI4IDE2MCIvPjxwb2x5Z29uIGNsYXNzPSJjbHMtMyIgcG9pbnRzPSIxMjEuNjQgMTgwIDEyMS42NCA4MCAxMzguOTYgNzAgMTM4Ljk2IDE3MCAxMjEuNjQgMTgwIi8+PHBvbHlnb24gY2xhc3M9ImNscy0zIiBwb2ludHM9Ijg3IDIwMCA4NyAxMDAgMTA0LjMyIDkwIDEwNC4zMiAxOTAgODcgMjAwIi8+PHBvbHlnb24gY2xhc3M9ImNscy00IiBwb2ludHM9Ijg3IDIwMCAwLjQgMTUwIDAuNCA1MCA4NyAxMDAgODcgMjAwIi8+PHBvbHlnb24gY2xhc3M9ImNscy01IiBwb2ludHM9IjY5LjY4IDEwIDE1Ni4yOCA2MCAxNzMuNiA1MCA4NyAwIDY5LjY4IDEwIi8+PHBvbHlnb24gY2xhc3M9ImNscy02IiBwb2ludHM9IjM1LjA0IDMwIDEyMS42NCA4MCAxMzguOTYgNzAgNTIuMzYgMjAgMzUuMDQgMzAiLz48cG9seWdvbiBjbGFzcz0iY2xzLTciIHBvaW50cz0iMC40IDUwIDg3IDEwMCAxMDQuMzIgOTAgMTcuNzIgNDAgMC40IDUwIi8+PC9zdmc+Cg==)](https://pybamm.org)

[![Blogs](https://img.shields.io/badge/Hashnode-2962FF?style=for-the-badge&logo=hashnode&logoColor=white)](https://arjxnpy.hashnode.dev/)
[![Project page on the Google Summer of Code website](https://img.shields.io/badge/%20view%20project%20-darkmagenta)](https://summerofcode.withgoogle.com/programs/2023/projects/vKlUTys3)
[![Proposal on Google Docs](https://img.shields.io/badge/%20view%20proposal%20-palevioletred)](https://docs.google.com/document/d/18IAFpu4T5gIGe7R2TBqa6y4ZnuuxyiF4g7PAQ09aQ3c)

<br>

[![View my Twitter profile](https://img.shields.io/badge/Twitter-1DA1F2?style=flat&logo=twitter&logoColor=white)](https://twitter.com/ArjxnPy)
[![View my GitHub profile](https://img.shields.io/badge/GitHub-100000?style=flat&logo=github&logoColor=white)](https://github.com/arjxn-py)
[![View my LinkedIn profile](https://img.shields.io/badge/LinkedIn-0077B5?style=linkedin&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/arjun-verma-758608226/)

---

This page serves as a permalink to the final report that provides details of Arjun Verma’s project in the Google Summer of Code 2023 programme.

## 📖 TL;DR

A summary of some of the tasks I achieved throughout the community bonding and the coding periods is given below.

- Migration of testing infrastructure from `tox` to `nox`
- Various improvements to existing infrastructure & Segregate optional dependencies
- Add or replace several pre-commit hooks to auto format the code
- Dockerize PyBaMM
- Significant Improvements to documentation including simplifying the installation instructions

## 🔋 About PyBaMM

PyBaMM is an open-source Python package for the mathematical modelling of batteries and running fast, flexible, and accurate simulations for myriads of battery models. Its mission is to accelerate battery modelling research by providing open-source tools for multi-institutional, interdisciplinary collaboration; it is fiscally sponsored by NumFOCUS and The Faraday Institution in the U.K. The use of the software in academia and industry has been prolific since its inception—it has been used at a multitude of universities, research institutions, and commercial research labs in collaborative settings.

## 📄 Project abstract

The primary focus of this project was to streamline the installation process of PyBaMM by containerizing it with Docker, simplifying the setup from source code. Additionally, the testing framework transitioned from tox to nox. An essential aspect of the project involved introducing optional dependencies for PyBaMM, allowing users to have customized and lightweight versions of PyBaMM tailored for specific tasks or use cases.

### 🚀 Motivation

The core motivation behind this project was to streamline the installation process by offering a simplified approach to installing from source. This involved providing a one-command installation that includes a pre-configured development environment with the desired solvers already installed.Furthermore, the project aimed to create a lightweight version of PyBaMM, which includes only the essential dependencies necessary for specific tasks.

### 🍀 Benefits to the community

This project offers a range of significant advantages aimed at enhancing the user experience and improving the development process. By containerizing PyBaMM and simplifying its installation through Docker, it provides a streamlined one-command setup that reduces complexity and setup time. The transition to Docker also ensures consistent environments across different systems, reducing potential compatibility issues. The inclusion of a PyBaMM Lite version with essential dependencies allows users to create lightweight configurations tailored to specific tasks, optimizing resource usage. These improvements collectively contribute to a more accessible, user-friendly installation process, fostering user engagement, enabling faster contributions, and advancing the PyBaMM ecosystem.

## 🧑‍💻 Work done

The first major accomplishment was the migration of the testing infrastructure from tox to nox. This transition brought about enhanced testing capabilities, improved efficiency, and greater reliability in assessing PyBaMM's codebase. The adoption of nox as the testing framework further contributed to a more robust development process.

In addition to testing improvements, the project introduced the concept of optional dependencies. This feature allows users to tailor their PyBaMM environment by selecting specific dependencies based on their requirements. This approach empowers users to create lightweight and specialized versions of PyBaMM that cater to their specific use cases, promoting efficient and resource-conscious development.

To ensure code quality and adherence to best practices, the project added more pre-commit hooks. These hooks automate code formatting, linting, and other checks, thereby enhancing the code review process and maintaining consistent coding standards throughout the development lifecycle.

One of the key achievements was the Dockerization of PyBaMM. By containerizing PyBaMM using Docker, the project simplified the installation process, making it easier for users to set up and deploy PyBaMM in various environments. This containerization approach eliminates potential installation hurdles and provides a consistent environment for users.

Lastly, the project successfully pushed PyBaMM Docker images to Docker Hub. This step not only showcases the project's commitment to accessibility but also makes it convenient for users to access and deploy PyBaMM Docker images from a centralized repository.

## 📑 A list of issues opened and pull requests submitted

This list contains issues and pull requests that are both specific to and not specific to my project: they contain infrastructure improvements, documentation improvements, general bug fixes, and enhancements.

### 🛠️ Issues

- ([pybamm-team/PyBaMM #2813](https://github.com/pybamm-team/PyBaMM/issues/2813))                         adding nbQA support for example notebooks
- ([pybamm-team/PyBaMM #2953](https://github.com/pybamm-team/PyBaMM/issues/2953))                         scikits odes installation
- ([pybamm-team/PyBaMM #2962](https://github.com/pybamm-team/PyBaMM/issues/2962))                         pybamm_install_odes is not tested anywhere
- ([pybamm-team/PyBaMM #3035](https://github.com/pybamm-team/PyBaMM/issues/3035))                         Splitting the required dependencies into optional dependencies
- ([pybamm-team/PyBaMM #3146](https://github.com/pybamm-team/PyBaMM/issues/3146))                         Make jax, jaxlib, and scikits.odes "extra requires" in setup.py
- ([pybamm-team/PyBaMM #3124](https://github.com/pybamm-team/PyBaMM/issues/3124))                         [Bug]: benchmarks are failing
- ([pybamm-team/PyBaMM #3048](https://github.com/pybamm-team/PyBaMM/issues/3048))                         Improve the nox CI
- ([pybamm-team/BPX    #38](https://github.com/pybamm-team/BPX/issues/38))                                  Migrate to Pydantic>2
- ([pybamm-team/PyBaMM #3049](https://github.com/pybamm-team/PyBaMM/issues/3049))                         Migrate or conjugate pyproject.toml with setup.py


### 👷 Pull requests

- ([pybamm-team/PyBaMM #2973](https://github.com/pybamm-team/PyBaMM/pull/2973))                         Test scikit.odes installation nightly
- ([pybamm-team/PyBaMM #3005](https://github.com/pybamm-team/PyBaMM/pull/3005))                         Migrate from tox 3.28 to nox
- ([pybamm-team/PyBaMM #3044](https://github.com/pybamm-team/PyBaMM/pull/3044))                         Create Optional Dependencies
- ([pybamm-team/PyBaMM #3082](https://github.com/pybamm-team/PyBaMM/pull/3082))                         Refactor env variables in a single function
- ([pybamm-team/PyBaMM #3084](https://github.com/pybamm-team/PyBaMM/pull/3084))                         Add pre-commit session & add default sessions
- ([pybamm-team/PyBaMM #3104](https://github.com/pybamm-team/PyBaMM/pull/3104))                         Document other useful nox commands
- ([pybamm-team/PyBaMM #3105](https://github.com/pybamm-team/PyBaMM/pull/3105))                         Installing pybamm[all] in jupyter notebooks
- ([pybamm-team/PyBaMM #3110](https://github.com/pybamm-team/PyBaMM/pull/3110))                         Add nbqa support for example notebooks
- ([pybamm-team/PyBaMM #3144](https://github.com/pybamm-team/PyBaMM/pull/3144))                         Make pandas optional
- ([pybamm-team/PyBaMM #3145](https://github.com/pybamm-team/PyBaMM/pull/3145))                         Fix Failing Benchmarks
- ([pybamm-team/PyBaMM #3162](https://github.com/pybamm-team/PyBaMM/pull/3162))                         Migrate from black to ruff --fix
- ([pybamm-team/PyBaMM #3163](https://github.com/pybamm-team/PyBaMM/pull/3163))                         Make jax & odes optional
- ([pybamm-team/PyBaMM #3180](https://github.com/pybamm-team/PyBaMM/pull/3180))                         Add blacken-docs as pre-commit hook for code-blocks in docs
- ([pybamm-team/PyBaMM #3192](https://github.com/pybamm-team/PyBaMM/pull/3192))                         Add more precommits
- ([pybamm-team/PyBaMM #3223](https://github.com/pybamm-team/PyBaMM/pull/3223))                         Dockerize PyBaMM
- ([pybamm-team/PyBaMM #3235](https://github.com/pybamm-team/PyBaMM/pull/3235))                         Clean up installation guides
- ([pybamm-team/PyBaMM #3106](https://github.com/pybamm-team/PyBaMM/pull/3106))                         Add max_step arg in basesolver (draft)
- ([pybamm-team/PyBaMM #3053](https://github.com/pybamm-team/PyBaMM/pull/3053))                         Add pyproject.toml to the project  (draft)
- ([pybamm-team/BPX      #39](https://github.com/pybamm-team/BPX/pull/39))                                Migrate to Pydantic>2 (draft)
- ([pybamm-team/BPX      #35](https://github.com/pybamm-team/BPX/pull/35))                                Temporarily pin pydantic<2 to fix PyBaMM build

## 🔮 Future work

- **Automated Docker Image Builds and DockerHub Integration:** Develop an automated process for building PyBaMM Docker images and seamlessly pushing them to DockerHub using continuous integration (CI) pipelines. This enhancement will ensure that up-to-date PyBaMM images are readily available for deployment and usage by the community.

- **Contribution to Nightly Release Infrastructure:** Further contribute to the implementation of nightly builds and releases on a custom PyPI index. Collaborate on versioning strategies, improve wheel-building infrastructure, and facilitate the smooth upload of nightly builds to the third-party PyPI index.

- **Exploration of Migration to pyproject.toml:** Investigate the feasibility and benefits of migrating PyBaMM's packaging configuration from setup.py to the modern pyproject.toml format. This transition could involve leveraging new build-backends like meson-py or scikit-build to enhance packaging compatibility and maintainability.

## Acknowledgements

I extend my heartfelt gratitude to the Google Summer of Code program, NumFOCUS, and the entire PyBaMM Team for providing me with a remarkable and enriching experience during this productive summer. This journey marked my first significant contribution to the development and maintenance of open-source scientific software on such a significant scale. The learnings I acquired throughout this process have been invaluable.

I am deeply honored to have had the privilege of being mentored by the esteemed PyBaMM Steering Council members, [Ferran Brosa Planella](https://www.brosaplanella.xyz/) and [Saransh Chopra](https://saransh-cpp.github.io). Their guidance and unwavering support not only in technical matters but also in fostering a positive and collaborative environment have been truly uplifting.

I wish to express my sincere appreciation to [Valentin Sulzer](https://sites.google.com/view/valentinsulzer) and [Robert Timms](https://www.robertwtimms.com/) for their invaluable reviews and guidance throughout various stages of my contributions to PyBaMM. The collective effort of the PyBaMM team, their insights, and collaborative spirit have been the driving force behind the accomplishments achieved during this project.

I also had the pleasure of collaborating with [Agriya](https://github.com/agriyakhetarpal), my fellow student at GSoC. Our interactions during discussions on issues and pull requests exemplified the essence of open-source collaboration.

## 🔭 References

- The GitHub repository for PyBaMM: https://github.com/pybamm-team/PyBaMM
- The PyBaMM documentation: https://docs.pybamm.org
- The DockerHub repository for PyBaMM: https://hub.docker.com/repository/docker/pybamm/pybamm/general
