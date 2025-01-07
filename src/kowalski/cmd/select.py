from kowalski.internal.config import KOWALSKI_PATH
from os                       import path
from frontmatter              import load
from kowalski.internal.note   import Note


def selectCmd(note_name: str):
    note_path = path.join(KOWALSKI_PATH, f"{note_name}.md")
    note_md = load(note_path)
    return Note(note_name, note_md["created"], note_md["updated"], note_md.content)