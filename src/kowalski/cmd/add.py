from datetime                 import datetime
from os                       import path
from kowalski.internal.config import KOWALSKI_PATH, EDITOR, KOWALSKI_FOLDER, GITHUB_USER, GITHUB_BRANCH, GITHUB_LOG_FILE
from kowalski.internal.run    import execute
from frontmatter              import load
from kowalski.internal.note   import Note
from kowalski.internal.git    import Git


def addCmd(content: str):
    created = datetime.now()
    updated = None
    name = created.strftime("%Y%m%d%H%M%S")
    if content is None:
        note_path = path.join(KOWALSKI_PATH, f"{name}.md")
        execute(f"{EDITOR} {note_path}")
        if path.exists(note_path):
            note_md = load(note_path)
            content = note_md.content
        else:
            return
    note = Note(name, created, updated, content)
    note_path = path.join(KOWALSKI_PATH, f"{name}.md")
    note.write(note_path)
    git = Git(KOWALSKI_PATH, GITHUB_USER, KOWALSKI_FOLDER, GITHUB_BRANCH, GITHUB_LOG_FILE)
    git.lean_commit("Added", name)
    print(note.description("short"))
    return note