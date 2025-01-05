from git                           import Repo
from kowalski_core.internal.config import KOWALSKI_FOLDER, KOWALSKI_PATH, GITHUB_USER, GITHUB_BRANCH


def pull():
    repo = Repo(KOWALSKI_PATH)
    origin = repo.remote(name='origin')
    origin.set_url(f"git@github.com:{GITHUB_USER}/{KOWALSKI_FOLDER}.git")
    origin.fetch()
    origin.pull(refspec=GITHUB_BRANCH)

def commit(message: str, name: str):
    repo = Repo(KOWALSKI_PATH)
    repo.git.add(all=True)
    commit_message = f"{message} Note {name}.md"
    repo.index.commit(commit_message)

def push():
    repo = Repo(KOWALSKI_PATH)
    origin = repo.remote(name='origin')
    origin.set_url(f"git@github.com:{GITHUB_USER}/{KOWALSKI_FOLDER}.git")
    origin.push(refspec=GITHUB_BRANCH)