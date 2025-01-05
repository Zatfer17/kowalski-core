from os import getenv, path

HOME = getenv("HOME")
EDITOR = getenv("EDITOR")
KOWALSKI_FOLDER = getenv("KOWALSKI_DIR", ".kowalski")
KOWALSKI_PATH = path.join(HOME, KOWALSKI_FOLDER)
GITHUB_USER = 'Zatfer17'
GITHUB_BRANCH = 'main'