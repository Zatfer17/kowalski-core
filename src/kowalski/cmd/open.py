from kowalski.internal.config import KOWALSKI_PATH, EDITOR, KOWALSKI_FOLDER, GITHUB_USER, GITHUB_BRANCH, GITHUB_LOG_FILE
from kowalski.internal.run    import execute
from os                       import path
from frontmatter              import load
from kowalski.internal.note   import Note
from kowalski.internal.git    import Git


def openCmd(note_name: str):
    note_path = path.join(KOWALSKI_PATH, f"{note_name}.md")
    execute(f"{EDITOR} {note_path}")
    note_md = load(note_path)
    note = Note(note_name, note_md["created"], note_md["updated"], note_md.content)
    note.refresh_updated()
    note.write(note_path)
    git = Git(KOWALSKI_PATH, GITHUB_USER, KOWALSKI_FOLDER, GITHUB_BRANCH, GITHUB_LOG_FILE)
    git.lean_commit("Updated", note_name)
    print(note.description("short"))
    return note