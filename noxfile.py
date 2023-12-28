import nox
import os
import sys

nox.options.reuse_existing_virtualenvs = True

@nox.session(name="themes")
def run_themes(session):
    themes_dir = "themes"
    if not os.path.exists(themes_dir) or not os.listdir(themes_dir):
        session.run("git",
            "submodule",
            "update",
            "--init",
            "--recursive",
            external=True,
        )
    else:
        print("'themes/' already exists in the project's root.")


@nox.session(name="html")
def build_html(session):
    # Ideally hugo must be pre-installed
    if sys.platform=="linux":
        session.run("apt", "install", "hugo", external=True)
    session.run("hugo")


@nox.session(name="serve")
def serve(session):
    session.run("hugo", "--printI18nWarnings", "server")


@nox.session(name="serve-dev")
def serve_dev(session):
    session.run("hugo", "--printI18nWarnings", "server", "--disableFastRender")


@nox.session(name="teams")
def generate_teams(session):
    session.run("python", "scripts/generate_teams.py")