import subprocess
import sys

def install_package(package):
    try:
        subprocess.check_call([sys.executable, "-m", "pip", "install", package])
    except subprocess.CalledProcessError as e:
        print(f"Failed to install {package}: {e}")
        sys.exit(1)

try:
    from git import Repo, InvalidGitRepositoryError
except ModuleNotFoundError:
    print("GitPython not found. Installing it now...")
    install_package("GitPython")
    from git import Repo, InvalidGitRepositoryError

import os

def load_repo(path='.'):
    try:
        return Repo(path)
    except InvalidGitRepositoryError:
        print("Not a git repository. Please run this script inside a git repo directory.")
        sys.exit(1)

def show_current_branch(repo):
    print(f'Current branch: {repo.active_branch.name}')

def show_latest_commit(repo):
    commit = repo.head.commit
    print(f'Latest commit: {commit.hexsha[:7]} - "{commit.message.strip()}" by {commit.author.name}')

def show_status(repo):
    changed_files = [item.a_path for item in repo.index.diff(None)]
    staged_files = [item.a_path for item in repo.index.diff('HEAD')]
    untracked = repo.untracked_files

    print("\nChanges not staged for commit:")
    if changed_files:
        for f in changed_files:
            print(f"  modified: {f}")
    else:
        print("  None")

    print("\nChanges to be committed:")
    if staged_files:
        for f in staged_files:
            print(f"  staged: {f}")
    else:
        print("  None")

    print("\nUntracked files:")
    if untracked:
        for f in untracked:
            print(f"  {f}")
    else:
        print("  None")

def show_commit_history(repo, n=5):
    print(f"\nLast {n} commits:")
    for commit in list(repo.iter_commits(max_count=n)):
        date_str = commit.committed_datetime.strftime('%Y-%m-%d %H:%M')
        print(f"{commit.hexsha[:7]} | {commit.author.name} | {date_str} | {commit.message.strip()}")

def main():
    repo = load_repo()
    show_current_branch(repo)
    show_latest_commit(repo)
    show_status(repo)
    show_commit_history(repo)

if __name__ == "__main__":
    main()
