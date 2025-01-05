from datetime                      import datetime
from os                            import path
from kowalski_core.internal.config import KOWALSKI_PATH
from kowalski_core.internal.note   import Note


def addCmd(content: str):
    created  = datetime.now()
    modified = None
    id       = created.strftime("%Y%m%d%H%M%S")

    note = Note(id, created, modified, content)

    note_path = path.join(KOWALSKI_PATH, f"{id}.md")
    note.write(note_path)
    
    print(note.description('short'))

    return note