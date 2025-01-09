import sys
import os

from datetime    import datetime
from frontmatter import load

from kowalski.internal.config import load_config
from kowalski.internal.run    import execute
from kowalski.internal.note   import Note


def add_cmd(content: str):

    PATH, EDITOR = load_config()

    if not sys.stdin.isatty():
        piped_content = sys.stdin.read().strip()
        content = piped_content if piped_content else content

    timestamp = datetime.now()

    name = f"{timestamp.strftime("%H%M%S-%y%m%d")}.md"
    created = timestamp.strftime("%Y%m%d%H%M%S")
    tags = []

    if content is None:

        note = Note(name, created, tags, "")
        note.write(PATH)

        note_path = os.path.join(PATH, name)
        execute(f"{EDITOR} {note_path}")

        md = load(note_path)
        tags = md["tags"]
        content = md.content

    note = Note(name, created, tags, content)
    note.write(PATH)

    print(note)
