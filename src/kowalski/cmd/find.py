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

        # Ensure compatibility with gitJournal
        created = md["created"]
        name = f"{created}.md"
        tags = md["tags"] if "tags" in md else []

        notes.append(Note(name, created, tags, md.content))

    print(*notes, sep=f"\n")