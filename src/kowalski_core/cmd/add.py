from datetime                      import datetime
from os                            import path
from kowalski_core.internal.config import KOWALSKI_PATH, EDITOR
from kowalski_core.internal.run    import execute
from frontmatter                   import load
from kowalski_core.internal.note   import Note
from kowalski_core.internal.git    import commit


def addCmd(content: str):
    created = datetime.now()
    updated = None
    name = created.strftime("%Y%m%d%H%M%S")
    if content is None:
        note_path = path.join(KOWALSKI_PATH, f"{name}.md")
        execute(f"{EDITOR} {note_path}")
        note_md = load(note_path)
        content = note_md.content
    note = Note(name, created, updated, content)
    note_path = path.join(KOWALSKI_PATH, f"{name}.md")
    note.write(note_path)
    commit("Added", name)
    print(note.description("short"))
    return note