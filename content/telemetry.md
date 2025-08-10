---
title: Telemetry
shortcutDepth: 2
summary: Information about the telemetry collection system in PyBaMM
---

From release 24.11 onwards, PyBaMM includes an **opt-in** telemetry collection system to help us better understand how PyBaMM is being used. This system collects anonymous usage data, such as the version of PyBaMM being used, the operating system, and the Python version. This data will help us make informed decisions about the future of PyBaMM. We would like to assure you that no personal data is collected, and the data is only used by the PyBaMM team. Here are some details:

- **What is collected**: Basic usage information like PyBaMM version, Python version, and which functions are run.
- **Why**: To understand how PyBaMM is used and prioritize development efforts.
- **Permanent opt-out**: To disable telemetry permanently, set the environment variable `PYBAMM_DISABLE_TELEMETRY=true` (or any value other than `false`) or use `pybamm.telemetry.disable()` in your code. You can also select "no" when PyBaMM asks if you would like to enable telemetry.
- **Privacy**: No personal information (name, email, etc) or sensitive information (parameter values, simulation results, etc) is ever collected. The data is used only by the PyBaMM team and is not shared with any third parties. The data is stored securely and is only accessible to the PyBaMM team. Please read PostHog's policy on [GDPR compliance](https://posthog.com/docs/privacy/gdpr-compliance) for more.
