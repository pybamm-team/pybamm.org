---
title: PyBaMM 24.X has been released!
summary: PyBaMM version 24.X has now been released with several new features and improvements.
date: 2024-11-04 # change later
shortcutDepth: 1
---

PyBaMM 24.X has now been released! This off-band release slightly differs from the previous release schedule conforming to three releases a year and marks the fourth release of 2024. We would like to thank all the [contributors](https://pybamm.org/teams/) who made this release possible.

The full list of changes can be found in the [CHANGELOG](https://pybamm.org/changelog/) file, but here we provide a deeper overview of the main features of this release.

## Telemetry data collection announcement

With this release, we have introduced a new **opt-in** telemetry collection system to help us better understand how PyBaMM is being used. This system collects anonymous usage data, such as the version of PyBaMM being used, the operating system, and the Python version. This data will help us make informed decisions about the future of PyBaMM. We would like to assure you that no personal data is collected, and the data is only used by the PyBaMM team. Here are some details:

- **What is collected**: Basic usage information like PyBaMM version, Python version, and which functions are run.
- **Why**: To understand how PyBaMM is used and prioritize development efforts.
- **Permanent opt-out**: To disable telemetry permanently, set the environment variable `PYBAMM_DISABLE_TELEMETRY=true` (or any value other than `false`) or use `pybamm.telemetry.disable()` in your code. You can also select "no" when PyBaMM asks if you would like to enable telemetry.
- **Privacy**: No personal information (name, email, etc) or sensitive information (parameter values, simulation results, etc) is ever collected. The data is used only by the PyBaMM team and is not shared with any third parties. The data is stored securely and is only accessible to the PyBaMM team. Please read PostHog's policy on [GDPR compliance](https://posthog.com/docs/privacy/gdpr-compliance) for more.
