from kowalski.internal.run    import execute_with_stdout
from os                       import path
from kowalski.internal.config import KOWALSKI_PATH
from frontmatter              import load
from kowalski.internal.note   import Note


def listCmd(keyword: str, limit: int):
    if " " in keyword:
        keyword = f'"{keyword}"'
    notes_paths = execute_with_stdout(f"grep -ril {keyword} {KOWALSKI_PATH}")
    notes_paths = [line for line in notes_paths.splitlines() if line.strip()]
    notes_paths = [note for note in notes_paths if ".md" in note]
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