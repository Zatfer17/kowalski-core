from kowalski_core.internal.config import KOWALSKI_PATH
from os                            import path
from frontmatter                   import load
from kowalski_core.internal.note   import Note



def showCmd(note_id: str):

    note_path = path.join(KOWALSKI_PATH, f"{note_id}.md")
    note_md = load(note_path)
    note = Note(note_md['id'], note_md['created'], note_md['modified'], note_md.content)

    print(note.description('long'))

    return note