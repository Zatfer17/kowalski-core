from glob                          import glob
from os                            import path
from kowalski_core.internal.config import KOWALSKI_PATH
from frontmatter                   import load
from datetime                      import datetime
from kowalski_core.internal.note   import Note


def listCmd(limit: int):
    notes_paths = glob(path.join(KOWALSKI_PATH, "*.md"))
    notes_paths = sorted(notes_paths, reverse=True)
    notes_paths = notes_paths[:limit]
    notes = []
    for p in notes_paths:
        note_md = load(p)
        note_name = p.split("/")[-1].replace(".md", "")
        note = Note(note_name, note_md["created"], note_md["updated"], note_md.content)
        notes.append(note)
        print(note.description("short"))
    return notes