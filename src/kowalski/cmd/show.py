import os

from frontmatter import load

from kowalski.internal.config import load_config
from kowalski.internal.note   import Note


def show_cmd(note: str):
    
    PATH, _ = load_config()

    note_path = os.path.join(PATH, note)

    md = load(note_path)
    note = Note(md["name"], md["created"], md["tags"], md.content)

    print(note.format())