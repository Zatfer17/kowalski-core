from kowalski_core.internal.config import KOWALSKI_PATH, EDITOR
from kowalski_core.internal.run    import execute
from os                            import path
from frontmatter                   import load
from kowalski_core.internal.note   import Note


def editCmd(note_name: str):
    note_path = path.join(KOWALSKI_PATH, f"{note_name}.md")
    execute(f"{EDITOR} {note_path}")
    note_md = load(note_path)
    note = Note(note_name, note_md["created"], note_md["updated"], note_md.content)
    note.refresh_updated()
    note.write(note_path)
    print(note.description("short"))
    return note