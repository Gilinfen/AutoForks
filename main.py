import requests
import os
from datetime import datetime
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


def fork_repo(repo_full_name, token, index):
    """Fork a specified GitHub repository and log the result."""
    url = f"https://api.github.com/repos/{repo_full_name}/forks"
    headers = {"Authorization": f"token {token}"}
    try:
        response = requests.post(url, headers=headers)
        current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        if response.status_code == 202:
            result = (
                f"{index + 1}. Successfully forked {repo_full_name} at {current_time}"
            )
        else:
            result = f"{index + 1}. Failed to fork {repo_full_name}, status code: {response.status_code} at {current_time}"
    except requests.exceptions.RequestException as e:
        result = f"{index + 1}. Request failed for {repo_full_name}, error: {e} at {current_time}"
    print(result)
    return result


def auto_fork_repos(username, token, forked_repos):
    """Automatically forks a list of repositories and logs each attempt."""
    for index, repo in enumerate(forked_repos):
        fork_repo(repo, token, index)


def main():
    username = os.getenv("USERNAME")
    token = os.getenv("TOKEN")
    forked_repos = get_all_forks(username, token)
    auto_fork_repos(username, token, forked_repos)


if __name__ == "__main__":
    main()
