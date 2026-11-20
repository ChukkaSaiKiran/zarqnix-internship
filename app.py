"""Fetch a short summary of a public GitHub repository."""
import sys
import requests

def repo_summary(owner, name):
    url = f"https://api.github.com/repos/{owner}/{name}"
    response = requests.get(url, headers={"Accept": "application/vnd.github+json"}, timeout=10)
    response.raise_for_status()  # turns a 404 or 500 into an exception
    data = response.json()
    return {
        "name": data["full_name"],
        "stars": data["stargazers_count"],
        "language": data["language"],
        "description": data["description"],
    }



if __name__ == "__main__":
    owner = sys.argv[1] if len(sys.argv) > 1 else "python"
    name = sys.argv[2] if len(sys.argv) > 2 else "cpython"

    try:
        print(repo_summary(owner, name))
    except requests.exceptions.HTTPError:
        print("Error: GitHub repository not found or request failed.")
    except requests.exceptions.RequestException as e:
        print("Network Error:", e)
