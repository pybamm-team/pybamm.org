---
title: PyBaMM 25.10 has been released!
summary: PyBaMM version 25.10 has now been released with several new features and improvements.
date: 2025-10-29
shortcutDepth: 1
---

PyBaMM 25.10 has now been released! We would like to thank all the [contributors](https://pybamm.org/teams/) who made this release possible.

The full list of changes can be found in the [CHANGELOG](https://pybamm.org/changelog/) file, but here we provide a deeper overview of the main features of this release.

## Fundamental variable for SEI models changed to concentration
_Implemented by [Simon O'Kane](https://github.com/DrSOKane)_

SEI models have been updated to use concentration as the fundamental variable (i.e. the variable PyBaMM solves for) instead of thickness. This change improves the physical accuracy of the models, and allows for better consistency with other submodels.  and allows for better representation of SEI growth dynamics.

## Updates in hysteresis parameters
_Implemented by [Rob Timms (Ionworks)](https://github.com/rtimms)_

The hysteresis decay rate has been updated to be a "true" decay  rate and the models adjusted accordingly. Behaviour should be unchanged for users, but the parameter values will need to be updated to match previous behaviour.

## Improvements to the IDAKLU solver
_Implemented by [Marc Berliner (Ionworks)](https://github.com/MarcBerliner)_

The IDAKLU solver now has an optional method to fail the simulation if the solver is not making progress. This is useful when the parameters are ill-conditioned and the solver is making very slow progress, such as in optimisation. These can be enabled by the kwargs `"num_steps_no_progress"` and `"t_no_progress"`. For more information, please see the [IDAKLU solver documentation](https://docs.pybamm.org/en/stable/source/api/solvers/idaklu_solver.html).

## Improvements to the composite electrode models
_Implemented by [Alec Bills](https://github.com/aabills) and [Rob Timms (Ionworks)](https://github.com/rtimms)_

The composite electrode models have been improved to support algebraic and differential surface form submodels. An SoH submodel has also been added for composite electrodes, which allows the user to specify the initial stoichiometries of the active materials from a given voltage.
