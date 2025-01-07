from subprocess               import run
from kowalski.internal.config import KOWALSKI_PATH
from glob                     import glob
from frontmatter              import load
from kowalski.internal.note   import Note


def listCmd(keyword: str, limit: int):
    if keyword is None:
        notes_paths = glob(f"{KOWALSKI_PATH}/*.md")
    else:
        if " " in keyword:
            keyword = f'"{keyword}"'
        grep_paths = run(f"grep -ril {keyword} {KOWALSKI_PATH}", shell=True, capture_output=True, text=True).stdout
        grep_paths = [line for line in grep_paths.splitlines() if line.strip()]
        find_paths = run(f"find {KOWALSKI_PATH} -type f -name '*{keyword}*'", shell=True, capture_output=True, text=True).stdout
        find_paths = [line for line in find_paths.splitlines() if line.strip()]
        notes_paths = grep_paths + find_paths
        notes_paths = list(set(notes_paths))
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