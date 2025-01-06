from os                       import path, remove
from kowalski.internal.config import KOWALSKI_PATH, KOWALSKI_FOLDER, GITHUB_USER, GITHUB_BRANCH, GITHUB_LOG_FILE
from kowalski.internal.git    import Git


def removeCmd(note_name: str):
    note_path = path.join(KOWALSKI_PATH, f"{note_name}.md")
    try:
        remove(note_path)
        git = Git(KOWALSKI_PATH, GITHUB_USER, KOWALSKI_FOLDER, GITHUB_BRANCH, GITHUB_LOG_FILE)
        git.lean_commit("Removed", note_name)
    except OSError:
        pass