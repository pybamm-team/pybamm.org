# Description: This script generates the HTML for PyBaMM's maintainers and contributors
# using the GitHub API.

# The HTML is then used in the website's "Teams" page at https://pybamm.org/teams.
# Mostly adapted from the scientific-python-hugo-theme teams generation code.

import requests
import string

# A list of emeritus maintainers, current maintainers, and maintainer trainees
# hard-coded in alphabetical order

PYBAMM_MAINTAINERS = [
    "brosaplanella",
    "martinjrobins",
    "priyanshuone6",
    "rtimms",
    "Saransh-cpp",
    "tinosulzer",
    "TomTranter",
]

PYBAMM_EMERITUS_MAINTAINERS = [
    "Scottmar93",
    "tlestang",
]

PYBAMM_MAINTAINER_TRAINEES = [
    "Afgr1087",
    "DrSOKane",
    "RuiheLi",
    "smitasahu2",
]


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
        # Exclude the pre-commit-ci and allcontributors bots
        and contributor["login"] != "pre-commit-ci[bot]"
        and contributor["login"] != "allcontributors[bot]"
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
    <div class="members">
        ${members}
    </div>
</div>
"""
)

# Displays the members of a specific team
member_template = string.Template(
"""
        <div class="member">
            <a href="${url}" class="name">
                <div class="photo">
                    <img
                        src="${avatarUrl}"
                        loading="lazy"
                        alt="Avatar of ${name}"
                    />
                </div>
                ${name}
            </a>
        </div>
"""
)

# Generate the HTML in static/teams/maintainers.html, overwriting as necessary
print("Generating maintainers...")
with open("static/teams/maintainers.html", "w") as file:
    file.write(
        team_template.substitute(
            team_name="Maintainers",
            members="\n".join(
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
with open("static/teams/emeritus-maintainers.html", "w") as file:
    file.write(
        team_template.substitute(
            team_name="Emeritus Maintainers",
            members="\n".join(
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
with open("static/teams/maintainer-trainees.html", "w") as file:
    file.write(
        team_template.substitute(
            team_name="Maintainer Trainees",
            members="\n".join(
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
            members="\n".join(
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
