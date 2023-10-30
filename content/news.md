---
title: PyBaMM Newsroom
shortcutDepth: 1
newsHeader: "Battery Modelling Webinar Series 2021"
date: 2021-07-06
toc: true
---

<!-- Format for adding news is: -->
<!-- ## Title -->
<!-- _Date_ -->
<!-- Content -->

<!-- Change date and heading in YAML frontmatter for homepage -->

<!-- Note: follow reverse order while updating, sort in descending order of recency -->

## Release notes 23.9
_October 31, 2023_

PyBaMM 23.9 is finally here! This release marks the change to a new release schedule with three releases a year, aiming to publish the new versions at the end of January, May and September (ish). We would like to thank all the contributors that made this release possible.

The full list of changes can be found in the CHANGELOG file, but here we provide a deeper overview of the main features of this release.

### Installation of optional dependencies
The number of required dependencies for PyBaMM has now been reduced to: [NumPy](https://numpy.org/), [SciPy](https://docs.scipy.org/doc/scipy/), [CasADi](https://web.casadi.org/docs/) and [Xarray](https://docs.xarray.dev/en/stable/). This will be the only dependencies installed when running
```bash
pip install pybamm
```

In addition, PyBaMM has a number of optional dependencies for different functionalities. If using `pip`, optional PyBaMM dependencies can be installed as optional extras, e.g.
```bash
pip install pybamm[dev,plot]
```
where `[dev,plot]` specify the optional sets of dependencies to install (see [the docs](https://docs.pybamm.org/en/latest/source/user_guide/installation/index.html#optional-dependencies) for more information about all the options). 

To install all optional dependencies the command is
```bash
pip install pybamm[all]
```

### SEI and plating models for both electrodes
From this version onwards, SEI (including SEI on cracks) and lithium plating models an be included in both the positive and the negative electrodes by passing a tuple of options, e.g.
```python3
model = pybamm.lithium_ion.DFN({"SEI": ("reaction limited", "reaction limited")})
``` 

To maintain the previous functionality, if a tuple is not given and `"working electrode"` is set to `"both"` (i.e. a full cell) then the setting will be applied only to the negative electrode. This change allows to use degradation models in half-cells, as shown in [this example notebook](https://docs.pybamm.org/en/latest/source/examples/notebooks/models/half-cell.html).

Note that this functionality introduced a breaking change as now all the variables corresponding to SEI, SEI on cracks and lithium plating have domains, e.g. `SEI thickness [m]` is no longer valid and `Negative SEI thickness [m]` or `Positive SEI thickness [m]` need to be used instead.

### Empirical hysteresis models
Another feature available in this version is empirical hysteresis for the particle diffusivity and the intercalation exchange-current density, which add to the existing functionality for hysteresis of the open-circuit potential. This means that these parameter functions can now be defined separately for lithiation and delithiation.

This functionality can be enabled by passing additional options to the model:
```python3
model = pybamm.lithium_ion.SPMe(
    {
        "open-circuit potential": ("current sigmoid", "single"),
        "exchange-current density": ("current sigmoid", "single"),
        "diffusivity": ("current sigmoid", "single"),
    }
)
```
where the tuples specify different behaviours for each electrode. The parameter values then need to be updated to provide the values for lithiation and delithiation accordingly, as shown in [this example script](https://github.com/pybamm-team/PyBaMM/blob/develop/examples/scripts/emperical_hysteresis.py).

### NumPy functions
NumPy functions now work with PyBaMM symbols, which means they can be used directly (e.g. `np.exp(pybamm.Symbol("a"))`) instead of calling the PyBaMM function (e.g. `pybamm.exp(pybamm.Symbol("a"))`). Additionally, NumPy arrays are now automatically converted to PyBaMM arrays, so the former can be combined with PyBaMM objects.

### MSMR model
The Multi-Species Multi-Reaction (MSMR) model, from [Baker & Verbrugge (2018)](https://iopscience.iop.org/article/10.1149/2.0771816jes) is now available in PyBaMM. The syntax of the model is
```python3
model = pybamm.lithium_ion.MSMR({"number of MSMR reactions": ("6", "4")})
```
and the number of reactions in each electrode needs to be specified (in this case we use 6 reactions in the negative electrode and 4 reactions in the positive one). An example of this model, with detailed explanation, can be found [in this notebook](https://docs.pybamm.org/en/latest/source/examples/notebooks/models/MSMR.html).

### Thermal pouch model
The notation around thermal models for pouch cells has now been improved. The main breaking change is that now the `"lumped"` thermal option always uses the parameters `"Cell cooling surface area [m2]"`, `"Cell volume [m3]"` and `"Total heat transfer coefficient [W.m-2.K-1]"` to compute the cell cooling regardless of the chosen `"cell geometry"` option. When accounting for a pouch cell, the correct values for these parameters must be provided by the user. 

The example notebooks for [thermal models](https://docs.pybamm.org/en/latest/source/examples/notebooks/models/thermal-models.html) and [pouch cell models](https://docs.pybamm.org/en/latest/source/examples/notebooks/models/pouch-cell-model.html) have now been updated to reflect these changes.


## Battery Modelling Webinar Series 2021
_July 06, 2021_

Robert Timms (University of Oxford) presented work on "Reduced-order 3D models of lithium-ion cells" today at the weekly Battery Modeling Webinar Series. The webinar attracts an audience from across the world with interests spanning a diverse range of battery-related topics.

The talk gave an overview of how to develop a range of 3D battery models of varying fidelity and complexity useful for describing the electrochemical and thermal behavior of pouch, jelly-roll, and prismatic cells. All of the reduced-order pouch cell models are available in PyBaMM now and can be compared in the [Pouch cell model example notebook](https://docs.pybamm.org/en/latest/source/examples/notebooks/models/pouch-cell-model.html). Keep your eyes peeled for jelly-roll models in a future release!

Thanks to all those who attended, and for all the useful questions and comments. Thanks also to Shashank Sripad and Alec Bills for hosting.

As usual, you can find slides for the talk ([PDF](https://github.com/pybamm-team/pybamm-supporting-material/blob/master/2021-07-BMWS-slides/RT_BMWS_06July.pdf)), and try out PyBaMM for yourself by going to [Examples](https://github.com/pybamm-team/PyBaMM/tree/develop/examples/) (to see the
examples) or [Google Colab](https://colab.research.google.com/github/pybamm-team/PyBaMM/blob/develop) (to run them online).



## PyBaMM JORS paper
_June 09, 2021_

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
_March 31, 2021_

Today the PyBaMM team presented a poster at the Oxford Battery Modelling Symposium 2021. The third edition of the OBMS ran virtually with Prof. Yue Qi (Brown University), Prof. Daniel Steingart (Columbia University) and Dr. Birger Horstmann (Helmholtz Institute Ulm) as keynote speakers.

The poster can be found in the [pybamm supporting material](https://github.com/pybamm-team/pybamm-supporting-material/blob/master/2021-03-OBMS-poster/OBMS21_pybamm.pdf) and it outlines the main features of PyBaMM along with some case studies, including thermal models (pouch and cylindrical cells) and degradation models (SEI, plating and cracking). The poster contains many links to the relevant code and papers.

You may try out PyBaMM for yourself by going to [Examples](https://github.com/pybamm-team/PyBaMM/tree/develop/examples/) (to see the examples) or [Google Colab](https://colab.research.google.com/github/pybamm-team/PyBaMM/blob/develop) (to run them online).



## PyBaMM v0.4.0 Release
_March 29, 2021_

PyBaMM version 0.4.0 has now been released. This release introduces:

* Several new models, including reversible and irreversible plating submodels, submodels for loss of active material, Yang et al.'s (2017) coupled SEI/plating/pore clogging model, and the Newman-Tobias model.
* Internal optimizations for solving models, particularly for simulating experiments, with more accurate event detection and more efficient numerical methods and post-processing.
* Parallel solutions of a model with different inputs.
* A cleaner installation process for Mac when installing from PyPI, no longer requiring a Homebrew installation of Sundials.
* Improved plotting functionality, including adding a new 'voltage component' plot.
* Several other new features, optimizations, and bug fixes, summarized below.

For more information, please see the full [CHANGELOG](https://github.com/pybamm-team/PyBaMM/blob/v0.4.0/CHANGELOG.md).



## PyBaMM v0.3.0 Release
_December 01, 2020_

PyBaMM version 0.3.0 has now been released. This release introduces a new aging model for particle swelling and cracking, a new reduced-order model (TSPMe), and a parameter set for A123 LFP cells. Additionally, there have been several backend optimizations to speed up model creation and solving, and other minor features and bug fixes.

For more information, please see the full [CHANGELOG](https://github.com/pybamm-team/PyBaMM/blob/v0.3.0/CHANGELOG.md).



## Faraday Institution Conference 2020
_November 24, 2020_

Robert Timms (University of Oxford) presented PyBaMM today in the Faraday Institution Annual Conference that took place online.

The talk introduced the main features of PyBaMM's framework and then presented different real case studies. These case studies showcased how PyBaMM can be used to simulate mechanical, thermal and degradation effects.

The recording of the talk is available on [YouTube](https://www.youtube.com/watch?v=1YlFr930Cv8&ab_channel=PyBaMM). Try out PyBaMM for yourself by going to [Examples](https://github.com/pybamm-team/PyBaMM/tree/develop/examples/) (to see the examples) or [Google Colab](https://colab.research.google.com/github/pybamm-team/PyBaMM/blob/develop) (to run them online, with no local installation). If you have any questions, please feel free to [contact us](/contact).

{{< youtube id="1YlFr930Cv8" class="workshop" levelOffset=4 >}}{{< /youtube >}}



## Battery Modelling Webinar Series
_September 08, 2020_

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
