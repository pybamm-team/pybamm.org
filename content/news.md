---
title: PyBaMM Newsroom
shortcutDepth: 2
newsHeader: "Battery Modelling Webinar Series 2021"
date: 2021-07-06
---

<!-- Format for adding news is: -->
<!-- ## Title -->
<!-- ###### Date -->
<!-- Text -->

<!-- Change date and heading in YAML frontmatter for homepage -->

<!-- Note: follow reverse order while updating, sort in descending order of recency -->

## Release notes 23.9
###### October 06, 2023

PyBaMM 23.9 is finally here! This release marks the change to a new release schedule with three releases a year, aiming to publish the new versions at the end of January, May and September (ish). We would like to thank all the contributors that made this release possible.

The full list of changes can be found in the CHANGELOG file, but here we provide a deeper overview of the main features of this release.

### Installation

### SEI and plating models for both electrodes

### Hysteresis

### Solver improvements

### Numpy functions

### MSMR model

### Thermal pouch model

## Battery Modelling Webinar Series 2021
###### July 06, 2021

Robert Timms (University of Oxford) presented work on "Reduced-order 3D models of lithium-ion cells" today at the weekly Battery Modeling Webinar Series. The webinar attracts an audience from across the world with interests spanning a diverse range of battery-related topics.

The talk gave an overview of how to develop a range of 3D battery models of varying fidelity and complexity useful for describing the electrochemical and thermal behavior of pouch, jelly-roll, and prismatic cells. All of the reduced-order pouch cell models are available in PyBaMM now and can be compared in the [Pouch cell model example notebook](https://docs.pybamm.org/en/latest/source/examples/notebooks/models/pouch-cell-model.html). Keep your eyes peeled for jelly-roll models in a future release!

Thanks to all those who attended, and for all the useful questions and comments. Thanks also to Shashank Sripad and Alec Bills for hosting.

As usual, you can find slides for the talk ([PDF](https://github.com/pybamm-team/pybamm-supporting-material/blob/master/2021-07-BMWS-slides/RT_BMWS_06July.pdf)), and try out PyBaMM for yourself by going to [Examples](https://github.com/pybamm-team/PyBaMM/tree/develop/examples/) (to see the
examples) or [Google Colab](https://colab.research.google.com/github/pybamm-team/PyBaMM/blob/develop) (to run them online).



## PyBaMM JORS paper
###### June 09, 2021

Our introductory paper is now out in the Journal of Open Research Software! This paper explains the motivation and design philosophy behind PyBaMM. Find it here: https://doi.org/10.5334/jors.309

&nbsp;

The paper can be cited in APA format as follows:

```
Sulzer, V., Marquis, S. G., Timms, R., Robinson, M., & Chapman, S. J. (2021). Python Battery Mathematical Modelling (PyBaMM) (Version 23.4.1) [Computer software]. https://doi.org/10.5334/jors.309
```

&nbsp;

or with BibTeX, as:

```
@software{Sulzer_Python_Battery_Mathematical_2021,
author = {Sulzer, Valentin and Marquis, Scott G. and Timms, Robert and Robinson, Martin and Chapman, S. Jon},
doi = {10.5334/jors.309},
month = jun,
title = {{Python Battery Mathematical Modelling (PyBaMM)}},
url = {https://github.com/pybamm-team/PyBaMM},
version = {23.4.1},
year = {2021}
}
```



## Oxford Battery Modelling Symposium 2021
###### March 31, 2021

Today the PyBaMM team presented a poster at the Oxford Battery Modelling Symposium 2021. The third edition of the OBMS ran virtually with Prof. Yue Qi (Brown University), Prof. Daniel Steingart (Columbia University) and Dr. Birger Horstmann (Helmholtz Institute Ulm) as keynote speakers.

The poster can be found in the [pybamm supporting material](https://github.com/pybamm-team/pybamm-supporting-material/blob/master/2021-03-OBMS-poster/OBMS21_pybamm.pdf) and it outlines the main features of PyBaMM along with some case studies, including thermal models (pouch and cylindrical cells) and degradation models (SEI, plating and cracking). The poster contains many links to the relevant code and papers.

You may try out PyBaMM for yourself by going to [Examples](https://github.com/pybamm-team/PyBaMM/tree/develop/examples/) (to see the examples) or [Google Colab](https://colab.research.google.com/github/pybamm-team/PyBaMM/blob/develop) (to run them online).



## PyBaMM v0.4.0 Release
###### March 29, 2021

PyBaMM version 0.4.0 has now been released. This release introduces:

* Several new models, including reversible and irreversible plating submodels, submodels for loss of active material, Yang et al.'s (2017) coupled SEI/plating/pore clogging model, and the Newman-Tobias model.
* Internal optimizations for solving models, particularly for simulating experiments, with more accurate event detection and more efficient numerical methods and post-processing.
* Parallel solutions of a model with different inputs.
* A cleaner installation process for Mac when installing from PyPI, no longer requiring a Homebrew installation of Sundials.
* Improved plotting functionality, including adding a new 'voltage component' plot.
* Several other new features, optimizations, and bug fixes, summarized below.

For more information, please see the full [CHANGELOG](https://github.com/pybamm-team/PyBaMM/blob/v0.4.0/CHANGELOG.md).



## PyBaMM v0.3.0 Release
###### December 01, 2020

PyBaMM version 0.3.0 has now been released. This release introduces a new aging model for particle swelling and cracking, a new reduced-order model (TSPMe), and a parameter set for A123 LFP cells. Additionally, there have been several backend optimizations to speed up model creation and solving, and other minor features and bug fixes.

For more information, please see the full [CHANGELOG](https://github.com/pybamm-team/PyBaMM/blob/v0.3.0/CHANGELOG.md).



## Faraday Institution Conference 2020
###### November 24, 2020

Robert Timms (University of Oxford) presented PyBaMM today in the Faraday Institution Annual Conference that took place online.

The talk introduced the main features of PyBaMM's framework and then presented different real case studies. These case studies showcased how PyBaMM can be used to simulate mechanical, thermal and degradation effects.

The recording of the talk is available on [YouTube](https://www.youtube.com/watch?v=1YlFr930Cv8&ab_channel=PyBaMM). Try out PyBaMM for yourself by going to [Examples](https://github.com/pybamm-team/PyBaMM/tree/develop/examples/) (to see the examples) or [Google Colab](https://colab.research.google.com/github/pybamm-team/PyBaMM/blob/develop) (to run them online, with no local installation). If you have any questions, please feel free to [contact us](/contact).

{{< youtube id="1YlFr930Cv8" class="workshop" levelOffset=4 >}}{{< /youtube >}}



## Battery Modelling Webinar Series
###### September 08, 2020

Valentin Sulzer (University of Michigan) presented PyBaMM today at the weekly
Battery Modeling Webinar Series, an event which attracts audience from across
the world with a wide range of interests.

The talk outlined PyBaMM's mission as an open-source framework for
collaborative battery modeling, and gave an overview of the fast, flexible, and
reliable modeling structure. A series of case studies showcasing a wide range
of applications of PyBaMM was presented, concluding with a live demonstration
of the software.

Thank you to everyone who joined, and to the many who asked insightful
questions - and especially to Venkat Subramanian for a great impromptu
discussion at the end on benchmark times for solving the DFN. Thanks also to
David Howey, Shashank Sripad, and Venkat Viswanathan for hosting and moderating.

As usual, you can find slides for the talk ([PDF](https://github.com/pybamm-team/pybamm-supporting-material/blob/master/2020-09-BMWS-slides/2020-09-BMWS-PyBaMM.pdf) or [PPTX](https://github.com/pybamm-team/pybamm-supporting-material/blob/master/2020-09-BMWS-slides/2020-09-BMWS-PyBaMM.pptx))
and try out PyBaMM for yourself by going to [Examples](https://github.com/pybamm-team/PyBaMM/tree/develop/examples/) (to see the
examples) or [Google Colab](https://colab.research.google.com/github/pybamm-team/PyBaMM/blob/develop) (to run them online).
