---
title: "Julian Evers — Google Summer of Code 2023 Final Report"
subtitle: "Techno-economic analysis"
summary: "This is the final report for Julian Evers's Google Summer of Code 2023 project with PyBaMM, NumFOCUS. I worked on a library for techno-economic analysis that can be combined with existing PyBaMM functionality"
date: 2023-11-06
shortcutDepth: 2
# WARNING: THE LINK TO THIS PAGE SHOULD NEVER BE CHANGED WITHOUT THE EXISTENCE OF A HUGO PERMALINK, AN ALIAS IN THE FRONTMATTER, OR WITHOUT THE EXISTENCE OF A PERMANENT (STATUS CODE 301) REDIRECTION RULE IN THE _redirects FILE AND A CORRESPONDING ENTRY IN THE netlify.toml FILE. THIS IS TO ENSURE THAT THE LINK TO THIS PAGE IS NEVER BROKEN SINCE IT ACCOUNTS FOR JULIAN EVERS'S GSoC 2023 FINAL REPORT AND IS LINKED TO FROM THE GOOGLE SUMMER OF CODE WEBSITE AS THE WORK PRODUCT SUBMISSION.
---

[![Google Summer of Code](https://img.shields.io/badge/Google_Summer_of_Code-2023-fbbd05?colorA=565656&logo=data:image/svg+xml;base64,PD94bWwgdmVyc2lvbj0iMS4wIiBlbmNvZGluZz0idXRmLTgiPz4KPCEtLSBHZW5lcmF0b3I6IEFkb2JlIElsbHVzdHJhdG9yIDE5LjIuMSwgU1ZHIEV4cG9ydCBQbHVnLUluIC4gU1ZHIFZlcnNpb246IDYuMDAgQnVpbGQgMCkgIC0tPgo8c3ZnIHZlcnNpb249IjEuMSIgaWQ9IkxheWVyXzExIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHhtbG5zOnhsaW5rPSJodHRwOi8vd3d3LnczLm9yZy8xOTk5L3hsaW5rIiB4PSIwcHgiIHk9IjBweCIKCSB2aWV3Qm94PSIwIDAgMTkyIDE5MiIgc3R5bGU9ImVuYWJsZS1iYWNrZ3JvdW5kOm5ldyAwIDAgMTkyIDE5MjsiIHhtbDpzcGFjZT0icHJlc2VydmUiPgo8c3R5bGUgdHlwZT0idGV4dC9jc3MiPgoJLnN0MHtmaWxsOiNGQkJDMDU7fQo8L3N0eWxlPgo8Zz4KCTxwYXRoIGNsYXNzPSJzdDAiIGQ9Ik0xNTguMSwzMy43aC0zNi40TDk2LDhMNzAuMywzMy43SDMzLjl2MzYuNEw4LjIsOTUuOWwyNS43LDI1LjdWMTU4aDM2LjRMOTYsMTgzLjdsMjUuNy0yNS43aDM2LjR2LTM2LjQKCQlsMjUuNy0yNS43bC0yNS43LTI1LjdWMzMuN3ogTTE1OC43LDk1LjljMCwzNC42LTI4LjEsNjIuNy02Mi43LDYyLjdzLTYyLjctMjguMS02Mi43LTYyLjdTNjEuNCwzMy4yLDk2LDMzLjIKCQlTMTU4LjcsNjEuMywxNTguNyw5NS45eiIvPgoJPHBhdGggY2xhc3M9InN0MCIgZD0iTTk2LDQxLjJjLTMwLjIsMC01NC43LDI0LjUtNTQuNyw1NC43YzAsMzAuMiwyNC41LDU0LjcsNTQuNyw1NC43YzMwLjIsMCw1NC43LTI0LjUsNTQuNy01NC43CgkJQzE1MC43LDY1LjcsMTI2LjIsNDEuMiw5Niw0MS4yeiBNNzkuOSw3NS42djlMNjUuNCw5NS45bDE0LjUsMTEuM3Y5bC0xLTAuN0w1Ny40LDk4LjdMNTYsOTcuNnYtMy40bDEuNC0xLjFsMjEuNS0xNi43TDc5LjksNzUuNgoJCUw3OS45LDc1LjZ6IE0xMDUuNyw3MC40TDkzLjgsMTIzbC0wLjEsMC40aC03LjRsMC40LTJsMTEuOS01Mi41bDAuMS0wLjRoNy40TDEwNS43LDcwLjR6IE0xMzYsOTcuNmwtMS40LDEuMUwxMTMsMTE1LjRsLTEsMC43di05CgkJbDE0LjUtMTEuM2wtMTQuNS0xMS4zdi05djBsMSwwLjdMMTM0LjUsOTNsMS40LDEuMVY5Ny42eiIvPgo8L2c+Cjwvc3ZnPgo=)](https://g.co/gsoc)
[![NumFOCUS](https://img.shields.io/badge/organisation-NumFOCUS-orange.svg?style=flat&colorA=007D8A&colorB=E1523D&logo=data:image/png;base64,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)](https://numfocus.org)
[![PyBaMM](https://img.shields.io/badge/sub%E2%80%93organisation-PyBaMM-blue?logo=data:image/svg+xml;base64,PHN2ZyBpZD0iTGF5ZXJfMSIgZGF0YS1uYW1lPSJMYXllciAxIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHhtbG5zOnhsaW5rPSJodHRwOi8vd3d3LnczLm9yZy8xOTk5L3hsaW5rIiB2aWV3Qm94PSIwIDAgMTc0IDIwMCI+PGRlZnM+PHN0eWxlPi5jbHMtMXtmaWxsOnVybCgjbGluZWFyLWdyYWRpZW50KTt9LmNscy0ye2ZpbGw6dXJsKCNsaW5lYXItZ3JhZGllbnQtMik7fS5jbHMtM3tmaWxsOiMyNDRmNzI7fS5jbHMtNHtmaWxsOnVybCgjbGluZWFyLWdyYWRpZW50LTMpO30uY2xzLTV7ZmlsbDp1cmwoI2xpbmVhci1ncmFkaWVudC00KTt9LmNscy02e2ZpbGw6dXJsKCNsaW5lYXItZ3JhZGllbnQtNSk7fS5jbHMtN3tmaWxsOnVybCgjbGluZWFyLWdyYWRpZW50LTYpO308L3N0eWxlPjxsaW5lYXJHcmFkaWVudCBpZD0ibGluZWFyLWdyYWRpZW50IiB4MT0iNDguMDMiIHkxPSI0Ny41IiB4Mj0iMTc3LjkzIiB5Mj0iMTIyLjUiIGdyYWRpZW50VW5pdHM9InVzZXJTcGFjZU9uVXNlIj48c3RvcCBvZmZzZXQ9IjAiIHN0b3AtY29sb3I9IiNmZmQ0M2IiLz48c3RvcCBvZmZzZXQ9IjEiIHN0b3AtY29sb3I9IiNmZmU4NzMiLz48L2xpbmVhckdyYWRpZW50PjxsaW5lYXJHcmFkaWVudCBpZD0ibGluZWFyLWdyYWRpZW50LTIiIHgxPSIxMy4zOSIgeTE9IjY3LjUiIHgyPSIxNDMuMjkiIHkyPSIxNDIuNSIgeGxpbms6aHJlZj0iI2xpbmVhci1ncmFkaWVudCIvPjxsaW5lYXJHcmFkaWVudCBpZD0ibGluZWFyLWdyYWRpZW50LTMiIHgxPSIwLjQiIHkxPSIxMjUiIHgyPSI4NyIgeTI9IjEyNSIgZ3JhZGllbnRVbml0cz0idXNlclNwYWNlT25Vc2UiPjxzdG9wIG9mZnNldD0iMCIgc3RvcC1jb2xvcj0iIzMwNjk5OCIvPjxzdG9wIG9mZnNldD0iMSIgc3RvcC1jb2xvcj0iIzRiOGJiZSIvPjwvbGluZWFyR3JhZGllbnQ+PGxpbmVhckdyYWRpZW50IGlkPSJsaW5lYXItZ3JhZGllbnQtNCIgeDE9IjE2OS4yNyIgeTE9IjU3LjUiIHgyPSI3NC4wMSIgeTI9IjIuNSIgZ3JhZGllbnRVbml0cz0idXNlclNwYWNlT25Vc2UiPjxzdG9wIG9mZnNldD0iMCIgc3RvcC1jb2xvcj0iIzZmYTJjYiIvPjxzdG9wIG9mZnNldD0iMSIgc3RvcC1jb2xvcj0iIzRiOGJiZSIvPjwvbGluZWFyR3JhZGllbnQ+PGxpbmVhckdyYWRpZW50IGlkPSJsaW5lYXItZ3JhZGllbnQtNSIgeDE9IjEzNC42MyIgeTE9Ijc3LjUiIHgyPSIzOS4zNyIgeTI9IjIyLjUiIHhsaW5rOmhyZWY9IiNsaW5lYXItZ3JhZGllbnQtNCIvPjxsaW5lYXJHcmFkaWVudCBpZD0ibGluZWFyLWdyYWRpZW50LTYiIHgxPSI5OS45OSIgeTE9Ijk3LjUiIHgyPSI0LjczIiB5Mj0iNDIuNSIgeGxpbms6aHJlZj0iI2xpbmVhci1ncmFkaWVudC00Ii8+PC9kZWZzPjxwb2x5Z29uIGNsYXNzPSJjbHMtMSIgcG9pbnRzPSIxNTYuMjggMTYwIDY5LjY4IDExMCA2OS42OCAxMCAxNTYuMjggNjAgMTU2LjI4IDE2MCIvPjxwb2x5Z29uIGNsYXNzPSJjbHMtMiIgcG9pbnRzPSIxMjEuNjQgMTgwIDM1LjA0IDEzMCAzNS4wNCAzMCAxMjEuNjQgODAgMTIxLjY0IDE4MCIvPjxwb2x5Z29uIGNsYXNzPSJjbHMtMyIgcG9pbnRzPSIxNTYuMjggMTYwIDE1Ni4yOCA2MCAxNzMuNiA1MCAxNzMuNiAxNTAgMTU2LjI4IDE2MCIvPjxwb2x5Z29uIGNsYXNzPSJjbHMtMyIgcG9pbnRzPSIxMjEuNjQgMTgwIDEyMS42NCA4MCAxMzguOTYgNzAgMTM4Ljk2IDE3MCAxMjEuNjQgMTgwIi8+PHBvbHlnb24gY2xhc3M9ImNscy0zIiBwb2ludHM9Ijg3IDIwMCA4NyAxMDAgMTA0LjMyIDkwIDEwNC4zMiAxOTAgODcgMjAwIi8+PHBvbHlnb24gY2xhc3M9ImNscy00IiBwb2ludHM9Ijg3IDIwMCAwLjQgMTUwIDAuNCA1MCA4NyAxMDAgODcgMjAwIi8+PHBvbHlnb24gY2xhc3M9ImNscy01IiBwb2ludHM9IjY5LjY4IDEwIDE1Ni4yOCA2MCAxNzMuNiA1MCA4NyAwIDY5LjY4IDEwIi8+PHBvbHlnb24gY2xhc3M9ImNscy02IiBwb2ludHM9IjM1LjA0IDMwIDEyMS42NCA4MCAxMzguOTYgNzAgNTIuMzYgMjAgMzUuMDQgMzAiLz48cG9seWdvbiBjbGFzcz0iY2xzLTciIHBvaW50cz0iMC40IDUwIDg3IDEwMCAxMDQuMzIgOTAgMTcuNzIgNDAgMC40IDUwIi8+PC9zdmc+Cg==)](https://pybamm.org)

[![Blogs](https://img.shields.io/badge/Medium-12100E?style=for-the-badge&logo=medium&logoColor=white)](https://medium.com/@julian.evers2)
[![Project page on the Google Summer of Code website](https://img.shields.io/badge/%20view%20project%20-darkmagenta)](https://summerofcode.withgoogle.com/programs/2023/projects/OE5AUkm6)
[![Proposal on Google Docs](https://img.shields.io/badge/%20view%20proposal%20-palevioletred)](https://docs.google.com/document/d/1OTXf-7Shuj972A4qViMDuU7ZqlFv9ennJLYCMSqt28I/edit?usp=sharing)

<br>

[![View my GitHub profile](https://img.shields.io/badge/GitHub-100000?style=flat&logo=github&logoColor=white)](https://github.com/julian-evers)

---

This page serves as a permalink to the final report that provides details of Julian Evers’s project in the Google Summer of Code 2023 programme.

## 📖 TL;DR

A summary of some of the tasks I achieved throughout the community bonding and the coding periods is given below.

- Adding a package for techno-economic analysis of batteries to the PyBaMM ecosystem; [PyBaMM-TEA](https://github.com/pybamm-team/pybamm-tea)
- Functionality for the calculation of cell metrics, such as gravimetric and volumetric energies (specific to various masses/volumes)
- The package can use PyBaMM's functionality, but does not require a full parameter-set and enables many input options

Much focus on electrode design:

- Calculation of masses and volumes, e.g., top-down or bottom-up calculation of inactive material densities
- Calculation of capacities and voltages considering stoichiometry/voltage limits and losses of lithium inventory

## 🔋 About PyBaMM

PyBaMM is an open-source Python package for the mathematical modelling of batteries and running fast, flexible, and accurate simulations for myriads of battery models. Its mission is to accelerate battery modelling research by providing open-source tools for multi-institutional, interdisciplinary collaboration; it is fiscally sponsored by NumFOCUS and The Faraday Institution in the U.K. The use of the software in academia and industry has been prolific since its inception—it has been used at a multitude of universities, research institutions, and commercial research labs in collaborative settings.

## 📄 Project abstract

The project aims at a techno-economic toolbox to analyze the influences of electrode-, cell- and process designs on e.g. cost per energy, which can utilize PyBaMM's functionality as for creating a Ragone plot. While it can be used with PyBaMM to estimate losses of lithium inventory (LLI) during formation and degradation, LLI can also be supplied as an input, so that a working parameter-set is not obligatory and also hypothetical chemistries can be modelled with the TEA. Similarly, also stoichiometries can be limited - alternatively to cutting-off voltages - so that capacity balancing can also be done with an average electrode potential as input instead of an OCV curve. An emphasis is on bottom-up calculation of electrode and separator densities, so that specific energies and costs can be described dependent on conductive additive- and binder weight fractions and densities. Generally, as with the density calculation, the TEA offers various input options e.g., the wet separator density can be calculated based on the dry separator density or the separator material density. The calculation of form factors, as well as costs and emissions originating from components and manufacturing steps is developing and will be continuously added to the repository. When adding new functionality - among other checks - all entries in printable dataframes are tested.

### 🚀 Motivation

The motivation for the work on the library is to create a techno-economic design tool for battery cells, that can be combined with PyBaMM. Thereby, fundamentals of electrode-, cell- and manufacturing process designs should be connected for a holistic techno-economic analysis of batteries.

### 🍀 Benefits to the community

The availability of a techno-economic analysis library connected with PyBaMM has a great chance of supporting people with the development of inexpensive and environmentally friendly batteries. The overview and combination of costs with electrode-, cell- and process design fundamentals could attract new users with diverse backgrounds to PyBaMM.

## 🧑‍💻 Work done

### 🏋🏽 Masses and volumes

Much time went into the (first) example notebook, which covers the mass and volume loadings of electrodes. The example notebook shows how a default PyBaMM parameter-set can be combined with an additional input-set to calculate/update densities, volume fractions/porosities, etc. to plot the mass and volume loadings against each other with a rectangle plot and print them - together with the densities - to a dataframe. PyBaMM parameter-sets include the (wet-) electrode density, porosity and active material volume fraction, when inputting the active material densities, the inactive material density is calculated top-down. Alternatively, the inactive material density can also be calculated bottom-up from binder and conductive additive density and weight fractions, then the (wet-) electrode density is updated accordingly. There are many more input options shown with the respective calculations in the notebook.

### ⚡️ Capacities and potentials

The capacities and potentials notebook gives an overview of the various input options for the electrode potentials and capacities. In PyBaMM, capacities are defined by the maximal concentrations of the particles [mol.m-3]. An alternative input with the (theoretical) gravimetric capacity [mA.h.g-1] has been added, which can be calculated from molar masses and updates the maximal concentrations. The stoichiometries at 0% and 100% can be calculated - as usual in PyBaMM - from the voltage cut-offs. Alternatively, the stoichiometry limits of one electrode can be set, which is useful for capacity balancing in case an average electrode voltage is supplied instead of a voltage curve or to set target capacities. The initial concentrations can also be set, e.g., based on the maximum amount of lithium from the positive electrode. This reinitialization can increase the amount of lithium inventory in PyBaMM parameter-sets, but the LLI can be set. The example notebook shows how practical active material capacities, stoichiometries, voltages, energies and more evolve with the LLI. Losses of active materials (LAM) will be added to the notebook, rate-dependent losses are not considered in the TEA, but can be estimated mechanistically with PyBaMM.

### 🏎️ Simulation's with PyBaMM

The combination of the TEA package with existing PyBaMM functionality is shown in the ragone example notebook, where the evolution of the gravimetric energy with the applied C-rate is plotted. The notebook is basically a copy of PyBaMM's rate capability notebook and serves as an example for the combination of PyBaMM-TEA with PyBaMM. More specific simulations can be added to benchmark rate capability - in the form of maximum pulse power at different SoC's or minimum charging time from 10% to 80% SoC, but also thermal behavior and degradation can be benchmarked.

### 🔋 Form factors

The form factor calculation is an essential part of the TEA and still needs to be added. From the cell design, the effective length of the electrode(s) is calculated, which determines absolute cell masses and capacities. Many cell designs can be modelled with three main classes: cylindric cells, stacked - not necessarily rectangular-shaped - and flat-winded cells with a hard or soft case. Thereby the electrode stack and outer housing mass can be calculated and excess volume and mass can be added. Also, excess electrolyte, excess electrode/capacity due to "anode-overhang" and various choices of outer layers could be modelled.

### 💵 Costs

The cost model is proposed to cover a large part of the project work and still needs to be added. It connects the electrode and cell design with the process design e.g., the choice of the active material and binder relate to the choice of the solvent and the form factor to the assembly cost. In the cost model, manufacturing and component costs have three input categories: _Material cost, Production cost and emissions_ which refer to different - single - functional units of the electrodes and cell and are put in relation to the energy throughput of the cell. The manufacturing process design can be decomposed into independent modules, for which costs can be assigned from the literature and which can be expanded e.g., with pack assembly and recycling. Optionally, cost inputs are described mechanistically e.g. considering electricity cost, scale and waste production.

## 📑 A full list of issues and pull requests from pybamm-tea

This list contains all issues and pull requests that are in the pybamm-tea repository at the time of writing the report.

### 🛠️ Issues

- ([pybamm-team/pybamm-tea  #1](https://github.com/pybamm-team/pybamm-tea/issues/1))                    Documentation
- ([pybamm-team/pybamm-tea  #2](https://github.com/pybamm-team/pybamm-tea/issues/2))                    Testing
- ([pybamm-team/pybamm-tea  #3](https://github.com/pybamm-team/pybamm-tea/issues/3))                    README
- ([pybamm-team/pybamm-tea  #4](https://github.com/pybamm-team/pybamm-tea/issues/4))                    Packaging
- ([pybamm-team/pybamm-tea  #6](https://github.com/pybamm-team/pybamm-tea/issues/6))                    Structure
- ([pybamm-team/pybamm-tea  #7](https://github.com/pybamm-team/pybamm-tea/issues/7))                    Set inputs in the class init
- ([pybamm-team/pybamm-tea  #8](https://github.com/pybamm-team/pybamm-tea/issues/8))                    Raise proper warning/errors instead of print statements
- ([pybamm-team/pybamm-tea #11](https://github.com/pybamm-team/pybamm-tea/issues/11))                   Legend entries don't display properly
- ([pybamm-team/pybamm-tea #14](https://github.com/pybamm-team/pybamm-tea/issues/14))                   Document calculations in TEA
- ([pybamm-team/pybamm-tea #15](https://github.com/pybamm-team/pybamm-tea/issues/15))                   Dict of list instead of list of dicts to populate data frames
- ([pybamm-team/pybamm-tea #19](https://github.com/pybamm-team/pybamm-tea/issues/19))                   Better testing


### 👷 Pull requests

- ([pybamm-team/pybamm-tea  #5](https://github.com/pybamm-team/pybamm-tea/pull/5))                      first draft
- ([pybamm-team/pybamm-tea  #9](https://github.com/pybamm-team/pybamm-tea/pull/9))                      Structure, readme, etc.
- ([pybamm-team/pybamm-tea #10](https://github.com/pybamm-team/pybamm-tea/pull/10))                     Update
- ([pybamm-team/pybamm-tea #12](https://github.com/pybamm-team/pybamm-tea/pull/12))                     update example
- ([pybamm-team/pybamm-tea #13](https://github.com/pybamm-team/pybamm-tea/pull/13))                     New notebook
- ([pybamm-team/pybamm-tea #16](https://github.com/pybamm-team/pybamm-tea/pull/16))                     Dataframe
- ([pybamm-team/pybamm-tea #17](https://github.com/pybamm-team/pybamm-tea/pull/17))                     legend visibility
- ([pybamm-team/pybamm-tea #18](https://github.com/pybamm-team/pybamm-tea/pull/18))                     Docs and testing
- ([pybamm-team/pybamm-tea #20](https://github.com/pybamm-team/pybamm-tea/pull/20))                     fix logo
- ([pybamm-team/pybamm-tea #21](https://github.com/pybamm-team/pybamm-tea/pull/21))                     fix logo
- ([pybamm-team/pybamm-tea #22](https://github.com/pybamm-team/pybamm-tea/pull/22))                     Test dataframe entries
- ([pybamm-team/pybamm-tea #23](https://github.com/pybamm-team/pybamm-tea/pull/23))                     New Notebooks (masses_and_volumes, capacities_and_potentials and ragone), documentation, testing
- ([pybamm-team/pybamm-tea #24](https://github.com/pybamm-team/pybamm-tea/pull/24))                     Form factors
- ([pybamm-team/pybamm-tea #25](https://github.com/pybamm-team/pybamm-tea/pull/25))                     Costs

## 🔮 Future work

- **Form factors:** Add functionality for different form factors, e.g., for a form factor with multiple, flat-winded cells inside one hard casing and create a database with typical input values for common form factors.

- **Cost models:** Decompose and describe manufacturing costs, e.g., by considering waste production

- **Sensitivity analysis:** Add standard deviations to the input values and create functionality for sensitivity analysis.

- **Cell metrics:** Create functions to estimate specific metrics with simulations, e.g., pulse power or charging time or many other cell metrics which utilize PyBaMM's functionality.

## Acknowledgements

The Google Summer of Code project with PyBaMM offered me so many insights into techno-economics of batteries, continuum modelling of battery cells and open-source modelling software development. I am incredibly thankful to [Robert Timms](https://www.robertwtimms.com/), [Jacqueline Edge](https://www.imperial.ac.uk/people/j.edge) and [Valentin Sulzer](https://sites.google.com/view/valentinsulzer) for the very supportive and enjoyable mentoring. The positive atmosphere and the understanding, even when there was no progress at times meant very much to me. Also I am very thankful that it was possible to extend the project timeline, which helped arranging the project with studying and working part-time. The conversations with the my fellow students at GSoC [Agriya](https://github.com/agriyakhetarpal) and [Arjun](https://github.com/arjxn-py), and with all the attendees in the monthly developer meetings felt like a huge privilege to me. I am grateful, that I can support the PyBaMM ecosystem and that I can continue the work on the TEA.

## 🔭 References

- The GitHub repository for pybamm-tea: https://github.com/pybamm-team/pybamm-tea
