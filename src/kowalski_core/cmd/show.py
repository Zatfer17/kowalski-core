from kowalski_core.internal.config import KOWALSKI_PATH
from os                            import path
from frontmatter                   import load
from kowalski_core.internal.note   import Note



def showCmd(note_name: str):
    note_path = path.join(KOWALSKI_PATH, f"{note_name}.md")
    note_md = load(note_path)
    note = Note(note_name, note_md["created"], note_md["updated"], note_md.content)
    print(note.description("long"))
    return note