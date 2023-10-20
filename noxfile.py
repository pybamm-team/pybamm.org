import nox
import os
import sys

nox.options.reuse_existing_virtualenvs = True

@nox.session(name="themes")
def run_themes(session):
    session.run("git",
                "submodule",
                "update",
                "--init",
                "--recursive",
                external=True,
            )