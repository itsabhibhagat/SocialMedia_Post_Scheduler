import requests
from datetime import datetime, timedelta
from config import MY_GITHUB_USERNAME, MY_GITHUB_TOKEN
import base64

def get_yesterday_commits():
    headers = {"Authorization": f"token {MY_GITHUB_TOKEN}"}
    since = (datetime.utcnow() - timedelta(days=1)).isoformat() + "Z"

    repos_url = f"https://api.github.com/users/{MY_GITHUB_USERNAME}/repos"
    repos = requests.get(repos_url, headers=headers).json()

    activities = []

    for repo in repos:
        repo_name = repo["name"]
        commits_url = f"https://api.github.com/repos/{MY_GITHUB_USERNAME}/{repo_name}/commits?since={since}"

        try:
            commits_response = requests.get(commits_url, headers=headers)
            commits = commits_response.json()

            # Handle error response from GitHub API
            if isinstance(commits, dict) and commits.get("message"):
                if commits.get("message") != "Git Repository is empty.":
                    print(f"Error in {repo_name}: {commits.get('message')}")
                continue

            for commit in commits:
                sha = commit["sha"]
                commit_detail_url = f"https://api.github.com/repos/{MY_GITHUB_USERNAME}/{repo_name}/commits/{sha}"
                detail = requests.get(commit_detail_url, headers=headers).json()

                files_changed = detail.get("files", [])
                file_summaries = []

                for f in files_changed:
                    filename = f.get("filename")
                    patch = f.get("patch", "No patch available")
                    short_patch = patch[:500]  # Limit patch size for GPT prompt
                    file_summaries.append(f"File: {filename}\nChanges:\n{short_patch}\n")

                if file_summaries:
                    full_change = "\n".join(file_summaries)
                    activities.append({
                        "repo": repo_name,
                        "url": commit["html_url"],
                        "message": commit["commit"]["message"],
                        "summary": full_change
                    })

        except Exception as e:
            print(f"Error in {repo_name}: {e}")
            continue

    return activities
    # return [
    #     {
    #         "repo": "portfolio-website",
    #         "url": "https://github.com/your-username/portfolio-website/commit/456def",
    #         "message": "Added new project section and updated contact form",
    #         "summary": "Implemented a new section to showcase recent projects with animations. Also fixed validation issues in the contact form using regex."
    #     }
    # ]

