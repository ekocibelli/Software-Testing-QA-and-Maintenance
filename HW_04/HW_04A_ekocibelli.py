"""
Created on Monday,2 19 2020
Author: Ejona Kocibelli
Project Description: Develop with the Perspective of the Tester in mind a program that gets a github account id and
                     prints out the repositories and commits.
"""

import requests
import json


def get_user_id():
    """Gets the user's id as an input from the user"""
    try:
        user_id = input("Enter GitHub ID:").lower()
        return user_id
    except ValueError:
        return "Oops!  That was no valid input. Try again..."


def get_user_data(user_id):
    """Gets user repositories and commits for each repository"""
    try:
        repo_url = requests.get(f"https://api.github.com/users/{user_id}/repos")
        if '"message":"Not Found"' in repo_url.text:  # check if the user exist
            return f"User {user_id} does not exist."
        else:
            user_info = {}
            repos_json = json.loads(repo_url.text)
            for obj in repos_json:
                user_info[obj['name']] = 0
            if len(user_info.keys()) == 0:  # check if the user has no repository
                return f"User {user_id} does not have any repository."
            else:
                for item in user_info.keys():
                    user_info[item] = len(
                        json.loads((requests.get(f'https://api.github.com/repos/{user_id}/{item}/commits')).text))
                for repository, commit_counts in user_info.items():
                    print(f"Repo: {repository} Number of commits: {commit_counts}")
            return user_info
    except ValueError:
        return 'Bad data.'


def main():
    """main function"""
    try:
        get_user_data(get_user_id())
    except ValueError:
        print('Bad data. Try again...')


if __name__ == '__main__':
    main()
