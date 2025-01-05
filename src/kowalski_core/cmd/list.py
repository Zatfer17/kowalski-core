from glob                          import glob
from os                            import path
from kowalski_core.internal.config import KOWALSKI_PATH
from frontmatter                   import load
from datetime                      import datetime
from kowalski_core.internal.note   import Note


def listCmd():

    notes_paths = glob(path.join(KOWALSKI_PATH, "*.md"))

    notes = []

    for p in notes_paths:

        note_md = load(p)

        note = Note(id, note_md['created'], note_md['modified'], note_md.content)
        notes.append(note.id)

        print(note.description('short'))

    return notes