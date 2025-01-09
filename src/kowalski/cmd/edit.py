import sys
import os

from frontmatter import load

from kowalski.internal.config import load_config
from kowalski.internal.run    import execute
from kowalski.internal.note   import Note


def edit_cmd(name: str, content: str):

    if not sys.stdin.isatty():
        piped_content = sys.stdin.read().strip()
        content = piped_content if piped_content else content

    PATH, EDITOR = load_config()

    note_path = os.path.join(PATH, name)

    if content is None:

        execute(f"{EDITOR} {note_path}")

    else:

        md = load(note_path)
        note = Note(md["name"], md["created"], md["tags"], content)

        note.write(PATH)

        print(note)