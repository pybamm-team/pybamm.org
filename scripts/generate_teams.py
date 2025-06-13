# /// script
# requires-python = ">=3.12"
# dependencies = [
#     "requests",
# ]
# ///

# Description: This script generates the HTML for PyBaMM's maintainers and contributors
# using the GitHub API.

# The HTML is then used in the website's "Teams" page at https://pybamm.org/teams.
# Mostly adapted from the scientific-python-hugo-theme teams generation code.

import requests
import string

from pathlib import Path

DIR = Path(__file__).parent.parent


def read_file(file_path):
    """Read a file and return a list of strings, split by lines."""
    with open(file_path) as file:
        return file.read().splitlines()


# Create a list of emeritus maintainers, current maintainers, and maintainer trainees


PYBAMM_MAINTAINERS = read_file(DIR / "teams" / "MAINTAINERS")
PYBAMM_EMERITUS_MAINTAINERS = read_file(DIR / "teams" / "EMERITUS-MAINTAINERS")
PYBAMM_MAINTAINER_TRAINEES = read_file(DIR / "teams" / "MAINTAINER-TRAINEES")


def query_contributors():
    # Get the list of contributors from the endpoint iteratively until we get
    # an empty response
    contributors_list = []
    page = 1
    while True:
        contributors = requests.get(
            f"https://api.github.com/repos/pybamm-team/pybamm/contributors?per_page=100&page={page}"
        ).json()
        if contributors == []:
            break
        else:
            contributors_list += contributors
            page += 1
    return contributors_list


PYBAMM_CONTRIBUTORS = query_contributors()


def get_contributors():
    """
    Get the "login", "html_url", and "avatar_url" fields for each contributor, which
    excludes maintainers, maintainer trainees, and bots.
    """
    return [
        {
        "login": contributor["login"],
        "html_url": contributor["html_url"],
        "avatar_url": contributor["avatar_url"]
        }
        for contributor in PYBAMM_CONTRIBUTORS
        # Exclude maintainers and maintainer trainees
        if contributor["login"] not in PYBAMM_MAINTAINERS
        and contributor["login"] not in PYBAMM_EMERITUS_MAINTAINERS
        and contributor["login"] not in PYBAMM_MAINTAINER_TRAINEES
        # Exclude all bots (pre-commit-ci, allcontributors, dependabot, et cetera)
        and not contributor["login"].endswith("[bot]")
    ]


def get_maintainers():
    """
    Get the "login", "html_url", and "avatar_url" fields for each maintainer from the
    list of maintainers.
    """
    return [
        {
        "login": maintainer["login"],
        "html_url": maintainer["html_url"],
        "avatar_url": maintainer["avatar_url"],
        }
        for maintainer in PYBAMM_CONTRIBUTORS
        if maintainer["login"] in PYBAMM_MAINTAINERS
        if maintainer["login"] not in PYBAMM_EMERITUS_MAINTAINERS
    ]


def get_emeritus_maintainers():
    """
    Get the "login", "html_url", and "avatar_url" fields for each emeritus maintainer
    from the list of emeritus maintainers.
    """
    return [
        {
        "login": emeritus_maintainer["login"],
        "html_url": emeritus_maintainer["html_url"],
        "avatar_url": emeritus_maintainer["avatar_url"],
        }
        for emeritus_maintainer in PYBAMM_CONTRIBUTORS
        if emeritus_maintainer["login"] in PYBAMM_EMERITUS_MAINTAINERS
    ]


def get_maintainer_trainees():
    """
    Get "login", "html_url", and "avatar_url" fields for each maintainer trainee.
    """

    # Get the GitHub user info for each maintainer trainee instead because some
    # of them are not in the contributors list yet
    maintainer_trainees = []
    for maintainer_trainee in PYBAMM_MAINTAINER_TRAINEES:
        maintainer_trainees.append(
            requests.get(f"https://api.github.com/users/{maintainer_trainee}").json()
        )

    return [
        {
        "login": maintainer_trainee["login"],
        "html_url": maintainer_trainee["html_url"],
        "avatar_url": maintainer_trainee["avatar_url"],
        }
        for maintainer_trainee in maintainer_trainees
    ]

# The team name can be either of the following:
# emeritus maintainers, maintainers, maintainer trainees, or contributors
team_template = string.Template(
"""
<div class="team">
    <h3 id="${team_name}"class="name title">
    ${team_name}
    </h3>
        <div class="sd-container-fluid sd-mb-4 false">
            <div class="sd-row sd-row-cols-2 sd-row-cols-xs-2 sd-row-cols-sm-3 sd-row-cols-md-4 sd-row-cols-lg-5 sd-g-2 sd-g-xs-2 sd-g-sm-3 sd-g-md-4 sd-g-lg-5">${members}</div>
        </div>
</div>
"""
)

# Displays the members of a specific team
member_template = string.Template(
"""
        <div class="sd-col sd-d-flex-row">
            <div class="sd-card sd-w-100 sd-shadow-sm sd-card-hover text-center">
                <div class="sd-card-body">
                <img src="${avatarUrl}" alt="Avatar of ${name}"/>
                    ${name}
                </div>
            <a class="sd-stretched-link" href="${url}"></a>
            </div>
        </div>
"""
)

# Generate the HTML in static/teams/maintainers.html, overwriting as necessary
print("Generating maintainers...")
print("Current maintainers are:", PYBAMM_MAINTAINERS)
with open("static/teams/maintainers.html", "w") as file:
    file.write(
        team_template.substitute(
            team_name="Maintainers",
            members="".join(
                [
                    member_template.substitute(
                        url=maintainer["html_url"],
                        avatarUrl=maintainer["avatar_url"],
                        name=maintainer["login"],
                    )
                    for maintainer in get_maintainers()
                ]
            ),
        )
    )

# Generate the HTML in static/teams/emeritus-maintainers.html, overwriting as necessary
print("Generating emeritus maintainers...")
print("Emeritus maintainers are:", PYBAMM_EMERITUS_MAINTAINERS)
with open("static/teams/emeritus-maintainers.html", "w") as file:
    file.write(
        team_template.substitute(
            team_name="Emeritus Maintainers",
            members="".join(
                [
                    member_template.substitute(
                        url=emeritus_maintainer["html_url"],
                        avatarUrl=emeritus_maintainer["avatar_url"],
                        name=emeritus_maintainer["login"],
                    )
                    for emeritus_maintainer in get_emeritus_maintainers()
                ]
            ),
        )
    )

# Generate the HTML in static/teams/maintainer-trainees.html, overwriting as necessary
print("Generating maintainer trainees...")
print("Maintainer trainees are:", PYBAMM_MAINTAINER_TRAINEES)
with open("static/teams/maintainer-trainees.html", "w") as file:
    file.write(
        team_template.substitute(
            team_name="Maintainer Trainees",
            members="".join(
                [
                    member_template.substitute(
                        url=maintainer_trainee["html_url"],
                        avatarUrl=maintainer_trainee["avatar_url"],
                        name=maintainer_trainee["login"],
                    )
                    for maintainer_trainee in get_maintainer_trainees()
                ]
            ),
        )
    )

# Generate the HTML in static/teams/contributors.html, overwriting as necessary
print("Generating contributors...")
with open("static/teams/contributors.html", "w") as file:
    file.write(
        team_template.substitute(
            team_name="Contributors",
            members="".join(
                [
                    member_template.substitute(
                        url=contributor["html_url"],
                        avatarUrl=contributor["avatar_url"],
                        name=contributor["login"],
                    )
                    for contributor in get_contributors()
                ]
            ),
        )
    )

print("HTML files generated successfully in static/teams/. Please commit the changes.")
