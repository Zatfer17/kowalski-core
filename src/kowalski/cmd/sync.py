from kowalski.internal.config import KOWALSKI_FOLDER, KOWALSKI_PATH, GITHUB_USER, GITHUB_BRANCH, GITHUB_LOG_FILE
from kowalski.internal.git    import Git


def syncCmd():
    git = Git(KOWALSKI_PATH, GITHUB_USER, KOWALSKI_FOLDER, GITHUB_BRANCH, GITHUB_LOG_FILE)
    git.initialize()
    git.commit()
    git.pull()
    git.push()