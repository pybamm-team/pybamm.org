import nox
import os
import sys
import shutil

nox.options.reuse_existing_virtualenvs = True
nox.options.default_venv_backend = "none"
nox.options.sessions = ["themes", "html", "serve-dev"]

@nox.session(name="themes")
def run_themes(session):
    """Clone or check if the 'themes' directory exists in the project's root."""
    themes_dir = "themes"
    if not os.path.exists(themes_dir) or not os.listdir(themes_dir):
        session.log(f"Cloning https://github.com/scientific-python/scientific-python-hugo-theme into {themes_dir}")
        session.run("git",
            "submodule",
            "update",
            "--init",
            "--recursive",
            external=True,
        )
    else:
        session.log("'themes/' already exists in the project's root.")


@nox.session(name="html")
def build_html(session):
    """Build the Hugo site using the 'hugo' command."""
    try:
        session.run("hugo")
    except Exception:
        session.error("The extended version of Hugo is not installed")


@nox.session(name="serve")
def serve(session):
    """Serve the Hugo site using the 'hugo server' command."""
    session.run("hugo", "--printI18nWarnings", "server")


@nox.session(name="serve-dev")
def serve_dev(session):
    """Serve the Hugo site with fast render disabled."""
    session.run("hugo", "--printI18nWarnings", "server", "--disableFastRender")


@nox.session(name="clean")
def clean_build(session):
    """Remove the 'public' folder if it exists."""
    base_directory = os.getcwd()
    build_dir = os.path.join(base_directory, "public")
    # Check if the "public" folder exists
    if os.path.exists(build_dir):
        shutil.rmtree(build_dir)
        session.log('The "public" folder has been successfully removed.')
    else:
        session.log('The "public" folder does not exist.')


@nox.session(name="teams", venv_backend="virtualenv")
def generate_teams(session):
    """Install 'requests' and run 'generate_teams.py'."""
    session.install("requests")
    session.run("python", "scripts/generate_teams.py")
    session.notify("lint")


@nox.session(name="lint")
def lint(session):
    """Install 'pre-commit' and run linting on all files."""
    session.install("pre-commit")
    session.run("pre-commit", "run", "--all-files")
