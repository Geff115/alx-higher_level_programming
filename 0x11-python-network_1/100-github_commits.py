#!/usr/bin/python3
"""
This Python script lists 10 commits
using the repository name, and owner name
"""


import sys
import requests


def list_commits(repo, owner):
    """
    Fetches the repository and the owner
    """

    url = f"https://api.github.com/repos/{owner}/{repo}/commits"
    response = requests.get(url)
    commits = response.json()
    for commit in commits[:10]:
        sha = commit.get('sha')
        author = commit.get('commit').get('author').get('name')
        print(f"{sha}: {author}")


if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: ./script.py <repository_name> <owner_name>")
        sys.exit(1)
    repo_name = sys.argv[1]
    owner_name = sys.argv[2]
    list_commits(repo_name, owner_name)
