from glob        import glob
from frontmatter import load

from kowalski.internal.config import load_config
from kowalski.internal.note   import Note


def list_cmd(limit: int):

    PATH, _ = load_config()

    files = glob(f"{PATH}/*.md")
    files = sorted(files, key=lambda x: (x.split('-')[1], x.split('-')[0]), reverse=True)
    files = files[:limit]

    notes = []
    for f in files:
        md = load(f)
        notes.append(Note(md["name"], md["created"], md["tags"], md.content))

    print(*notes, sep=f"\n")

    return notes