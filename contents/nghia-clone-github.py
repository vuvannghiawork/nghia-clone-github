import os
import requests
import subprocess


if __name__ == "__main__":
    # folder_path
    folder_path = r"C:\Users\Admin\Desktop\NghiaGithub"

    # username
    username = "vuvannghiawork"
    repo_ignore = [
        "nghia-template",
    ]

    if not os.path.exists(folder_path):
        print("Folder does not exist")
        exit()
    os.chdir(folder_path)

    # get all repos
    repos = []
    page = 1
    while True:
        url = f'https://api.github.com/users/{username}/repos?page={page}&per_page=100'
        response = requests.get(url)
        if response.status_code != 200:
            break
        page_repos = response.json()
        if not page_repos:
            break
        repos.extend([repo['name'] for repo in page_repos])
        page += 1
    print(repos)

    # clone all repos
    for repo in repos:
        if repo in repo_ignore:
            continue
        subprocess.run(['git', 'clone', f'https://github.com/{username}/{repo}.git'])
