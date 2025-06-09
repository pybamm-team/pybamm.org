---
title: PyBaMM 25.6 has been released!
summary: PyBaMM version 25.6 has now been released with several new features and improvements.
date: 2025-05-27
shortcutDepth: 1
---

PyBaMM 25.6 has now been released! We would like to thank all the [contributors](https://pybamm.org/teams/) who made this release possible.

The full list of changes can be found in the [CHANGELOG](https://pybamm.org/changelog/) file, but here we provide a deeper overview of the main features of this release.

## MSMR parameters renamed
_Implemented by [Marc Berliner (Ionworks)](https://github.com/MarcBerliner)_

The parameters used in the MSMR model have been renamed to have more meaningful names (rather than just symbols), for example:
- "X_n_5" -> "Negative electrode host site occupancy fraction (5)"
- "X_p_l_3" -> "Positive electrode host site occupancy fraction (lithiation) (3)"
- "X_n_d_5" -> "Negative electrode host site occupancy fraction (delithiation) (5)"
- "Q_p_3" -> "Positive electrode host site occupancy capacity (3) [A.h]"
- "w_n_2" -> "Negative electrode host site ideality factor (2)"
- "U0_p_d_4" -> "Positive electrode host site standard potential (delithiation) (4) [V]"
- "a_p_d_5" -> "Positive electrode host site charge transfer coefficient (delithiation) (5)"
- "j0_ref_n_0" -> "Negative electrode host site reference exchange-current density (0) [A.m-2]"

This is not a breaking change, as the old names are still supported (with a deprecated warning), but it is recommended to use the new names in new code. The old names will be removed in a future release.

## Various solver improvements
_Implemented by [Marc Berliner (Ionworks)](https://github.com/MarcBerliner) and [Martin Robinson (Oxford RSE)](https://github.com/martinjrobins)_

This release also includes various smaller improvements to the solvers which overall improve performance and usability:
- All documentations, examples and tests have been updated to use the `pybamm.IDAKLUSolver`.
- Solvers now include an additional argument to change `on_extrapolation` behaviour to `"error"`, `"warn"`, or `"ignore"`, giving users more control over how extrapolation is handled when events are hit.
- The `pybamm.CasadiAlgebraicSolver` has been improved to be faster and more robust. The root solver is now cached to avoid repeated initialisation. A `step_tol` parameter has been added to control the tolerance for the Newton iteration step. The default has also been changed to a more relaxed value, making the solver more robust. Finally, the solver now uses Casadi's in-built success flags safeguarding against the solution containing `nan` or `inf` values.
- The calculation of variable sensitivities has been sped-up.

## Sensitivities are only supported by pybamm.IDAKLU solver
_Implemented by [Martin Robinson (Oxford RSE)](https://github.com/martinjrobins)_

The `pybamm.CasadiSolver` and`pybamm.ScipySolver` no longer support sensitivity calculation. This is because these solvers do not support sensitivities natively, like the `pybamm.IDAKLUSolver` and the existing implementation of sensitivities was not robust enough. Now that `pybamm.IDAKLUSolver` is the default solver, we decided to deprecate the sensitivity calculation in the other solvers as it created a lot of technical debt and confusion for users. If sensitivities are calculated with any solver other than `pybamm.IDAKLUSolver`, an error will be raised.
