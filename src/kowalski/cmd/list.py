from glob        import glob
from frontmatter import load

from kowalski.internal.config import load_config
from kowalski.internal.note   import Note


def list_cmd(limit: int):

    PATH, _ = load_config()

    files = glob(f"{PATH}/*.md")
    files = sorted(files, reverse=False)
    files = files if limit is None else files[-limit:]

    notes = []
    for f in files:
        md = load(f)

        # Ensure compatibility with gitJournal
        created = md["created"]
        name = f"{created}.md"
        tags = md["tags"] if "tags" in md else []

        notes.append(Note(name, created, tags, md.content))

    print(*notes, sep=f"\n")

    return notes