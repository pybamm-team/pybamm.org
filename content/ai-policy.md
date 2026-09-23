---
title: AI Policy
shortcutDepth: 2
summary: How generative AI tools may (and may not) be used when contributing to PyBaMM.
---

{{< admonition note >}}
This policy is a draft and is open for discussion. If you have comments, please open a discussion on [GitHub](https://github.com/pybamm-team/PyBaMM/discussions) or raise it at a monthly developer meeting.
{{< /admonition >}}

## In short

- You are responsible for everything you submit, and you must be able to explain it.
- Say in the pull request if AI helped write it, and which parts.
- Do not paste confidential or unpublished data into these tools.
- Check equations, parameter values, and references against the literature yourself.
- Write to other people in your own words.
- Do not let an agent open pull requests in your name.

The rest of this page explains what each of these means in practice.

## Scope

By "AI" we mean generative AI tools: large language models, and the assistants, chatbots, code completion tools, and agents built on them, which can generate, edit, and review code, prose, and images. Spell-checkers, grammar correction, and translation tools are not covered by this policy, and you are welcome to use them.

This policy applies to contributions to the [PyBaMM repositories](https://github.com/pybamm-team) and to discussion on [Discourse](https://pybamm.discourse.group) and [Slack](https://pybamm.org/slack/). It covers code, documentation, examples, issues, pull requests, and reviews.

We are not opposed to these tools, and several of our contributors use them. What we ask is that a person remains responsible for everything submitted in their name.

## Responsibility

You are responsible for your contribution, however it was produced. An AI tool cannot take responsibility for anything, so you keep all of it.

You must be able to explain your contribution: the lines you added, the existing code they interact with, why the approach works, and what it trades off. If you cannot explain it, it is not ready to submit. "The model wrote it that way" is not an answer to a review comment.

Do not credit a tool as an author. AI tools are not co-authors on commits and not authors on papers. If you want to record that you used one, put it in the pull request description.

## Battery models, parameters, and references

PyBaMM is used to make decisions about real cells, so a wrong equation is worse here than an inelegant one.

Plausible-looking equations, parameter values, and citations are among the things these tools invent most readily. A generated reference may not exist; a generated parameter value may be dimensionally correct and physically wrong. Check every model change, parameter set, and reference against the primary literature yourself before you submit it, and cite the source you actually read.

## Confidential and unpublished data

Anything you paste into a hosted AI tool leaves your machine, and may be retained or used to train the service.

Do not paste in anything you could not post publicly in a GitHub issue. This includes proprietary cell data, unpublished measurements, parameter sets held under an agreement, and code your employer owns.

If you contribute as part of your job, check your employer's policy before you use these tools on work related to PyBaMM. This policy does not override it, and it does not give you permission you do not otherwise have.

## Disclosure

If AI tools helped materially with a contribution, say so in the pull request or issue description. A sentence is enough. Please state:

- which tool(s) you used;
- what you used them for, for example drafting an implementation, writing tests, refactoring, or writing documentation;
- which parts of the contribution are AI-generated.

We ask for this so reviewers know where to look hardest. It is not held against you, and disclosing does not make a contribution any less welcome.

You do not need to disclose editor autocomplete, or a tool you used only to look something up.

## Quality

Every contribution is held to the same standard, whether a person or a model wrote the first draft.

Generated code tends to be verbose, subtly wrong, or out of keeping with the code around it. Generated tests tend to assert that the code does what it does, rather than what it should do. Generated documentation often reads well and says little. All of this takes a reviewer longer to check than it took you to produce, which is why we ask you to check it first.

Before opening a pull request, read your own diff line by line and ask whether you could defend each part of it in review. Please do not open pull requests speculatively to see whether CI passes, and please do not open many small generated pull requests at once. Submissions that are plainly unreviewed machine output will be closed without a detailed review.

## Copyright and licensing

PyBaMM is distributed under the [BSD 3-Clause licence](https://github.com/pybamm-team/PyBaMM/blob/develop/LICENSE.txt). By contributing, you confirm you have the right to license your contribution under it.

These models are trained on code and text under many different licences, and can reproduce parts of them. You are responsible for making sure what you submit does not infringe anyone's copyright. If part of your contribution comes from an existing source, say so and name the source and its licence. We may decline a contribution whose provenance we cannot establish.

## Communication

When you take part in issues, pull requests, reviews, Discourse posts, or Slack conversations, please write in your own words.

Translating your words into English, or fixing grammar and spelling, is welcome and always has been. We would rather hear from you imperfectly than not at all. What we ask you not to do is have a model speak for you: pasted output presented as your own reasoning, generated issue and pull request descriptions, or generated code reviews. People reply to those in good faith, and that time is wasted.

If you use an assistant to help you understand PyBaMM, check what it tells you against the [documentation](https://docs.pybamm.org) before passing it on to someone else.

## Agents

Do not point an autonomous agent at our repositories to open issues or pull requests on its own. Contributions submitted that way will be closed.

You are welcome to use an agent in your own work. The requirement is that you read what it produced, take responsibility for it under the sections above, and submit it from your own account.

This section is about generative AI agents. It does not cover the project's own routine automation, such as dependency updates, pre-commit autoupdates, and scheduled content updates, which run from workflows maintainers have configured and are merged by maintainers.

## Maintainers and reviewers

Maintainers are bound by this policy too. We do not merge code we do not understand.

A review posted under a maintainer's name is that maintainer's own judgement, and no maintainer approves a change they have not read. Where a review is machine-assisted, we will say so, on the same terms we ask of you.

## If we think a contribution breaks this policy

A maintainer will ask you about it first, in the pull request or issue. Usually that is the end of it.

If there is no reply, we close the contribution after 30 days, as we do for any issue awaiting a response. A closed contribution can be reopened if you come back and pick it up.

Persistent or deliberate disregard for this policy is referred to the [steering council](/governance/). Only conduct that is also a breach of the [Code of Conduct](/code-of-conduct/), such as harassment or dishonesty about another person, is handled under the Code of Conduct.

## Mentorship programmes

This policy applies in full to mentored programmes such as Google Summer of Code and Google Season of Docs, including your application and proposal.

These programmes exist so that you learn and so that we get to know you as a contributor. We care more about how you think than about how much code you produce. Use these tools to read code, look things up, and get unstuck, rather than to write your proposal or your patches. Google also publishes [guidance on AI tools in GSoC](https://developers.google.com/open-source/gsoc/resources/ai_guidance).

## Changes to this policy

These tools change quickly and this policy will change with them. We will review it at least once a year, and sooner if it stops matching what we actually do.

If you think something here is wrong, unclear, or unworkable, please tell us: open a [discussion](https://github.com/pybamm-team/PyBaMM/discussions), raise it at a monthly developer meeting, or email [pybamm@pybamm.org](mailto:pybamm@pybamm.org).

## Acknowledgements

This policy follows the AI policies of [NumPy](https://numpy.org/devdocs/dev/ai_policy.html) and [SciPy](https://scipy.github.io/devdocs/dev/conduct/ai_policy.html), and some of its wording is adapted from them, with thanks. It also draws on Google Summer of Code's [AI guidance](https://developers.google.com/open-source/gsoc/resources/ai_guidance).
