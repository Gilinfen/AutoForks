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
        if response.status_code != 200:
            print(f"Failed to retrieve repos: {response.text}")
            break
        repos = response.json()
        if not repos:
            break
        forked_repos.extend([repo["full_name"] for repo in repos if repo["fork"]])
        page += 1
    return forked_repos


def fork_repo(repo_full_name, token, index):
    """Fork a specified GitHub repository and log the result."""
    current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    try:
        url = f"https://api.github.com/repos/{repo_full_name}/forks"
        headers = {"Authorization": f"token {token}"}
        response = requests.post(url, headers=headers)
        if response.status_code == 202:
            result = (
                f"{index + 1}. Successfully forked {repo_full_name} at {current_time}"
            )
        else:
            result = f"{index + 1}. Failed to fork {repo_full_name}, status code: {response.status_code} at {current_time}"
    except requests.exceptions.RequestException as e:
        result = f"{index + 1}. Request failed for {repo_full_name}, error: {e} at {current_time}"
    except Exception as e:
        result = f"{index + 1}. An error occurred: {e} at {current_time}"
    print(result)
    return result


def auto_fork_repos(username, token, forked_repos):
    """Automatically forks a list of repositories and logs each attempt."""
    log_entries = []
    for index, repo in enumerate(forked_repos):
        result = fork_repo(repo, token, index)
        log_entries.append(result)
    save_to_md(log_entries)


def save_to_md(data):
    """Save log data to a Markdown file in the logs directory with the current timestamp."""
    now = datetime.now()
    filename = f"logs/{now.strftime('%Y-%m-%d-%H-%M-%S')}.md"
    os.makedirs(os.path.dirname(filename), exist_ok=True)
    with open(filename, "w") as f:
        for entry in data:
            f.write(f"{entry}\n")


def main():
    username = os.getenv("USERNAME")
    token = os.getenv("TOKEN")
    try:
        forked_repos = get_all_forks(username, token)
        auto_fork_repos(username, token, forked_repos)
    except Exception as e:
        print(f"Error during the execution: {e}")


if __name__ == "__main__":
    main()
