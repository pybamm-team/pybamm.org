---
title: AI Policy
shortcutDepth: 2
summary: How generative AI tools may (and may not) be used when contributing to PyBaMM.
---

{{< admonition note >}}
This policy is a draft and is open for discussion. If you have comments, please open a discussion on [GitHub](https://github.com/pybamm-team/PyBaMM/discussions) or raise it at a monthly developer meeting.
{{< /admonition >}}

## Scope

By "AI" we mean generative AI tools: large language models and the assistants, chatbots, code completion tools, and autonomous agents built on top of them, which can generate, edit, translate, and review code, prose, and images.

This policy applies to every contribution to the PyBaMM project - code, documentation, examples, issues, pull requests, reviews, and discussions - in the [PyBaMM repositories](https://github.com/pybamm-team), on [Discourse](https://pybamm.discourse.group), and on [Slack](https://pybamm.org/slack/).

We are not opposed to these tools, and several of our contributors use them. We do insist that a human being remains responsible for everything submitted in their name. The rest of this page sets out what that means in practice.

## Responsibility

You are responsible for your contribution, regardless of how it was produced. An AI tool is not a co-author and is not accountable for anything; you are.

You must understand your contribution and be able to explain it - not only the lines you added, but the existing code they interact with, why the approach is correct, and what the trade-offs are. It is not acceptable to open a pull request that you cannot explain yourself. If a reviewer asks why a change was made and the honest answer is "the model wrote it that way", the contribution is not ready.

The same applies to the physics and mathematics that PyBaMM implements. Battery models have physical meaning, and plausible-looking equations, parameter values, and citations are exactly the kind of thing these tools invent. Every model change, parameter set, and reference must be checked against the literature by you before it is submitted.

## Disclosure

If AI tools helped materially with a contribution, say so in the pull request or issue description. A sentence is enough. Please state:

- which tool(s) you used;
- what you used them for (for example, generating an initial implementation, writing tests, refactoring, or drafting documentation);
- which parts of the contribution are AI-generated.

We ask for this because it helps reviewers know where to look hardest, not to disqualify your work. Contributions found to have used AI substantially without disclosure may be closed.

Routine use of an editor's autocomplete, spell-checking, or grammar correction does not need to be disclosed.

## Quality

Every contribution is held to the same standard, whether a person or a model wrote the first draft. AI-generated code is often verbose, subtly wrong, or inconsistent with the surrounding code; AI-generated tests often assert that the implementation does what it does rather than what it should do; AI-generated documentation often reads fluently while saying nothing.

Reviewer time is the scarcest resource this project has. Submissions that are largely unreviewed machine output - what other projects have taken to calling "AI slop" - will be closed without a detailed review. Please do not open pull requests speculatively to see whether they pass CI, and please do not open a large number of small AI-generated pull requests at once.

Before you open a pull request, read your own diff line by line and ask whether you would be comfortable defending it in review. If you would not, do not submit it yet.

## Copyright and licensing

PyBaMM is distributed under the [BSD 3-Clause licence](https://github.com/pybamm-team/PyBaMM/blob/develop/LICENSE.txt), and by contributing you confirm that you have the right to license your contribution under it.

Generative models are trained on large bodies of code and text under a variety of licences, and can reproduce parts of them. You are responsible for ensuring that what you submit does not infringe anyone's copyright and is compatible with our licence. If any part of your contribution derives from an existing source, say so and identify the source and its licence. We reserve the right to decline any contribution whose provenance we cannot be confident about.

## Communication

Human-to-human communication is what makes this a community rather than a codebase. When you take part in issues, pull requests, reviews, Discourse posts, or Slack conversations, please write in your own words.

Using AI to translate your words into English, or to correct grammar and spelling, is welcome and always has been - we would much rather hear from you imperfectly than not at all. What we ask you not to do is have a model speak on your behalf: pasted model output presented as your own reasoning, auto-generated issue and pull request descriptions, or AI-written code reviews. These consume the time of everyone who replies to them in good faith.

Similarly, if you use an assistant to help you understand PyBaMM, please check its answers against the [documentation](https://docs.pybamm.org) before relaying them to someone else. Confidently wrong answers about battery modelling spread quickly.

## Autonomous agents

Autonomous agents that open issues or pull requests against PyBaMM repositories without a person having reviewed and understood the result are not permitted, and such contributions will be closed.

You are welcome to use an agent as part of your own workflow. The requirement is that a human reviews what it produced, takes responsibility for it under the sections above, and submits it under their own account.

## Maintainers and reviewers

The obligations above apply to maintainers as well: we do not merge code we do not understand, and we do not review contributions with AI.

Maintainers may ask a contributor to explain their submission, and may close a contribution that appears to be substantially unreviewed machine output, or whose provenance is unclear. This is a judgement about the contribution, not about the person, and it is not an accusation - the aim is to keep review capacity available for work that is ready for it. Repeated disregard for this policy is handled under the [Code of Conduct](/code-of-conduct/).

## Mentorship programmes

If you are applying to or taking part in a mentored programme with PyBaMM, such as Google Summer of Code or Google Season of Docs, this policy applies to your contributions in full, including your application and any proposal.

The point of these programmes is that you learn and that we get to know you as a contributor, so we care much more about how you think than about how much code you produce. Use these tools to read code, look things up, and get unstuck - not to write your proposal or your patches for you. See also Google's [guidance on AI tools in GSoC](https://developers.google.com/open-source/gsoc/resources/ai_guidance).

## Feedback

This policy will change as the tools do. If you think something here is wrong, unclear, or unworkable, please tell us - open a [discussion](https://github.com/pybamm-team/PyBaMM/discussions), raise it at a monthly developer meeting, or email [pybamm@pybamm.org](mailto:pybamm@pybamm.org).

## Acknowledgements

This policy draws on the AI policies of [NumPy](https://numpy.org/devdocs/dev/ai_policy.html) and [SciPy](https://scipy.github.io/devdocs/dev/conduct/ai_policy.html), and on Google Summer of Code's [AI guidance](https://developers.google.com/open-source/gsoc/resources/ai_guidance).
