from os import getenv, path

HOME = getenv("HOME")
EDITOR = getenv("EDITOR")
KOWALSKI_FOLDER = ".kowalski"
KOWALSKI_PATH = path.join(HOME, KOWALSKI_FOLDER)
GITHUB_LOG_FILE = path.join(HOME, KOWALSKI_FOLDER, ".logs")

# Update
GITHUB_USER = "Zatfer17"
GITHUB_BRANCH = "main"
MODEL = "gpt-4o-mini"