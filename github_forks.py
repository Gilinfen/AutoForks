import requests
import json
import os
from dotenv import load_dotenv

# 加载环境变量
load_dotenv()


def get_all_forks(username, token):
    """Retrieve all forked repositories for a given GitHub username."""
    page = 1
    forked_repos = []

    while True:
        url = f"https://api.github.com/users/{username}/repos?type=owner&per_page=100&page={page}"
        headers = {"Authorization": f"token {token}"}
        response = requests.get(url, headers=headers)
        repos = response.json()

        if not repos:
            break

        forked_repos.extend([repo["full_name"] for repo in repos if repo["fork"]])

        page += 1

    return forked_repos


def save_to_json(filename, data):
    """Save data to a JSON file."""
    with open(filename, "w") as f:
        json.dump(data, f, indent=4)


def main():
    username = os.getenv("USERNAME")
    token = os.getenv("TOKEN")
    forked_repos = get_all_forks(username, token)
    save_to_json("forked_repositories.json", forked_repos)
    print("Forked repositories have been saved to 'forked_repositories.json'")


if __name__ == "__main__":
    main()
