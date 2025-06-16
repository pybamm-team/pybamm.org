# /// script
# requires-python = ">=3.12"
# dependencies = [
#     "requests",
# ]
# ///

# Description: This script generates the HTML for PyBaMM's maintainers and contributors
# using the GitHub GraphQL and REST APIs.

# The HTML is then used in the website's "Teams" page at https://pybamm.org/teams.
# Mostly adapted from the scientific-python-hugo-theme teams generation code.

import requests
import string
import os

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
PYBAMM_GSOC_STUDENTS = read_file(DIR / "teams" / "GSOC-STUDENTS")
PYBAMM_PAST_GSOC_STUDENTS = read_file(DIR / "teams" / "PAST-GSOC-STUDENTS")


def get_graphql_headers():
    """Get headers for GraphQL API requests"""
    token = os.getenv("GITHUB_TOKEN")

    if token:
        return {"Authorization": f"Bearer {token}", "Content-Type": "application/json"}
    else:
        raise RuntimeError(
            "No GITHUB_TOKEN found. This script requires it to access the GitHub API. "
            "Please set the GITHUB_TOKEN environment variable with a valid token."
        )


def get_user_batch_graphql(usernames):
    """Get user details for a batch of usernames"""
    if not usernames:
        return []

    headers = get_graphql_headers()
    users = []

    for i in range(0, len(usernames), 10):
        batch = usernames[i : i + 10]

        user_queries = []
        for j, username in enumerate(batch):
            user_queries.append(f"""
            user{j}: user(login: "{username}") {{
              login
              name
              url
              avatarUrl
            }}
            """)

        query = f"""
        query {{
            {" ".join(user_queries)}
        }}
        """

        response = requests.post(
            "https://api.github.com/graphql", headers=headers, json={"query": query}
        )

        if response.status_code != 200:
            print(f"GraphQL query failed: {response.status_code}")
            print(response.text)
            continue

        data = response.json()

        if "errors" in data:
            print(f"GraphQL errors: {data['errors']}")
            continue

        for _, user_data in data["data"].items():
            users.append(
                {
                    "login": user_data["login"],
                    "name": user_data["name"] or user_data["login"],
                    "html_url": user_data["url"],
                    "avatar_url": user_data["avatarUrl"],
                }
            )

    return users


def query_contributors():
    # Get the list of contributors from the endpoint iteratively until we get
    # an empty response. This still uses the GitHub REST API and paginates
    # the results, because the GraphQL API does not list committers in the
    # same way across nodes.
    contributors_list = []
    page = 1

    headers = {}
    token = os.getenv("GITHUB_TOKEN")
    if token:
        headers["Authorization"] = f"Bearer {token}"
        headers["Accept"] = "application/vnd.github+json"
        headers["X-GitHub-Api-Version"] = "2022-11-28"

    while True:
        url = f"https://api.github.com/repos/pybamm-team/pybamm/contributors?per_page=100&page={page}"
        try:
            print(f"Fetching contributors page {page}...")
            response = requests.get(url, headers=headers, timeout=30)
            if response.status_code != 200:
                print(f"HTTP Error {response.status_code}: {response.text}")
                break
            if not response.text.strip():
                print("Empty response, no more pages")
                break

            try:
                contributors = response.json()
            except requests.exceptions.JSONDecodeError as e:
                print(f"JSON decode error: {e}")
                print(f"Response text: {response.text}...")
                break

            if not contributors or contributors == []:
                print(f"Reached end of contributors at page {page}")
                break

            contributors_list.extend(contributors)
            print(
                f"Found {len(contributors)} contributors on page {page} (total: {len(contributors_list)})"
            )
            page += 1

        except Exception as e:
            print(f"Unexpected error: {e}")
            break

    print(f"Total contributors found: {len(contributors_list)}")
    return contributors_list


PYBAMM_CONTRIBUTORS = query_contributors()


def get_contributors():
    """
    Get the "login", "html_url", and "avatar_url" fields for each contributor, which
    excludes maintainers, maintainer trainees, and bots.
    """
    contributors = [
        contributor["login"]
        for contributor in PYBAMM_CONTRIBUTORS
        # Exclude other teams
        if contributor["login"] not in PYBAMM_MAINTAINERS
        and contributor["login"] not in PYBAMM_EMERITUS_MAINTAINERS
        and contributor["login"] not in PYBAMM_MAINTAINER_TRAINEES
        and contributor["login"] not in PYBAMM_GSOC_STUDENTS
        and contributor["login"] not in PYBAMM_PAST_GSOC_STUDENTS
        # Exclude all bots (pre-commit-ci, allcontributors, dependabot, et cetera)
        and not contributor["login"].endswith("[bot]")
    ]

    return get_user_batch_graphql(contributors)


def get_maintainers():
    """
    Get the "login", "html_url", and "avatar_url" fields for each maintainer from the
    list of maintainers.
    """
    maintainers = [
        maintainer["login"]
        for maintainer in PYBAMM_CONTRIBUTORS
        if maintainer["login"] in PYBAMM_MAINTAINERS
        if maintainer["login"] not in PYBAMM_EMERITUS_MAINTAINERS
    ]

    return get_user_batch_graphql(maintainers)


def get_emeritus_maintainers():
    """
    Get the "login", "html_url", and "avatar_url" fields for each emeritus maintainer
    from the list of emeritus maintainers.
    """
    emeritus_maintainers = [
        emeritus_maintainer["login"]
        for emeritus_maintainer in PYBAMM_CONTRIBUTORS
        if emeritus_maintainer["login"] in PYBAMM_EMERITUS_MAINTAINERS
    ]

    return get_user_batch_graphql(emeritus_maintainers)


def get_maintainer_trainees():
    """
    Get "login", "html_url", and "avatar_url" fields for each maintainer trainee.
    """

    # Get the GitHub user info for each maintainer trainee instead because some
    # of them are not in the contributors list yet
    return get_user_batch_graphql(PYBAMM_MAINTAINER_TRAINEES)


def get_gsoc_students():
    """
    Get "login", "html_url", and "avatar_url" fields for each GSoC student.
    """
    gsoc_students = [
        contributor["login"]
        for contributor in PYBAMM_CONTRIBUTORS
        if contributor["login"] in PYBAMM_GSOC_STUDENTS
    ]

    return get_user_batch_graphql(gsoc_students)


def get_past_gsoc_students():
    """
    Get "login", "html_url", and "avatar_url" fields for each past GSoC student.
    """
    past_gsoc_students = [
        contributor["login"]
        for contributor in PYBAMM_CONTRIBUTORS
        if contributor["login"] in PYBAMM_PAST_GSOC_STUDENTS
    ]

    return get_user_batch_graphql(past_gsoc_students)


# The team name can be either of the following:
# emeritus maintainers, maintainers, maintainer trainees, current GSoC students, past GSoC students, and contributors


def create_team_id(team_name: str) -> str:
    """Create a URL-friendly ID from team name (lowercase, replace spaces with hyphens)"""
    return team_name.lower().replace(" ", "-")


team_template = string.Template(
"""
<h3 id="${team_id}">${team_name}<a class="headerlink" href="#${team_id}" title="Link to this heading">#</a></h3>
<div class="sd-container-fluid sd-mb-4 false">
    <div class="sd-row sd-row-cols-2 sd-row-cols-xs-2 sd-row-cols-sm-3 sd-row-cols-md-4 sd-row-cols-lg-5 sd-g-2 sd-g-xs-2 sd-g-sm-3 sd-g-md-4 sd-g-lg-5">${members}</div>
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
    team_name = "Maintainers"
    file.write(
        team_template.substitute(
            team_name=team_name,
            team_id=create_team_id(team_name),
            members="".join(
                [
                    member_template.substitute(
                        url=maintainer["html_url"],
                        avatarUrl=maintainer["avatar_url"],
                        name=maintainer["name"],
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
    team_name = "Emeritus Maintainers"
    file.write(
        team_template.substitute(
            team_name=team_name,
            team_id=create_team_id(team_name),
            members="".join(
                [
                    member_template.substitute(
                        url=emeritus_maintainer["html_url"],
                        avatarUrl=emeritus_maintainer["avatar_url"],
                        name=emeritus_maintainer["name"],
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
    team_name = "Maintainer Trainees"
    file.write(
        team_template.substitute(
            team_name=team_name,
            team_id=create_team_id(team_name),
            members="".join(
                [
                    member_template.substitute(
                        url=maintainer_trainee["html_url"],
                        avatarUrl=maintainer_trainee["avatar_url"],
                        name=maintainer_trainee["name"],
                    )
                    for maintainer_trainee in get_maintainer_trainees()
                ]
            ),
        )
    )

# Generate the HTML in static/teams/gsoc-students.html, overwriting as necessary
print("Generating GSoC students...")
print("Current GSoC students are:", PYBAMM_GSOC_STUDENTS)
with open("static/teams/gsoc-students.html", "w") as file:
    team_name = "Current Google Summer of Code students"
    file.write(
        team_template.substitute(
            team_name=team_name,
            team_id=create_team_id(team_name),
            members="".join(
                [
                    member_template.substitute(
                        url=contributor["html_url"],
                        avatarUrl=contributor["avatar_url"],
                        name=contributor["name"],
                    )
                    for contributor in get_gsoc_students()
                ]
            ),
        )
    )

# Generate the HTML in static/teams/past-gsoc-students.html, overwriting as necessary
print("Generating past GSoC students...")
print("Past GSoC students are:", PYBAMM_PAST_GSOC_STUDENTS)
with open("static/teams/past-gsoc-students.html", "w") as file:
    team_name = "Past Google Summer of Code students"
    file.write(
        team_template.substitute(
            team_name=team_name,
            team_id=create_team_id(team_name),
            members="".join(
                [
                    member_template.substitute(
                        url=contributor["html_url"],
                        avatarUrl=contributor["avatar_url"],
                        name=contributor["name"],
                    )
                    for contributor in get_past_gsoc_students()
                ]
            ),
        )
    )

# Generate the HTML in static/teams/contributors.html, overwriting as necessary
print("Generating contributors...")
with open("static/teams/contributors.html", "w") as file:
    team_name = "Contributors"
    file.write(
        team_template.substitute(
            team_name=team_name,
            team_id=create_team_id(team_name),
            members="".join(
                [
                    member_template.substitute(
                        url=contributor["html_url"],
                        avatarUrl=contributor["avatar_url"],
                        name=contributor["name"],
                    )
                    for contributor in get_contributors()
                ]
            ),
        )
    )

print(f"Generated {len(PYBAMM_CONTRIBUTORS)} contributors.")

print("HTML files generated successfully in static/teams/. Please commit the changes.")
