from frontmatter import load

from kowalski.internal.config import load_config
from kowalski.internal.run    import execute
from kowalski.internal.note   import Note


def find_cmd(content: str):
    
    PATH, _ = load_config()

    files = execute(f"grep -ril '{content}' --include='*.md' {PATH}", split=False, shell=True, output=True)
    files = [file for file in files.splitlines() if file.strip()]
    files = sorted(files, reverse=True)

    notes = []
    for f in files:
        md = load(f)
        notes.append(Note(md["name"], md["created"], md["tags"], md.content))

    print(*notes, sep=f"\n")

    return notes