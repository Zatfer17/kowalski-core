from kowalski.internal.config import MODEL
from kowalski.internal.ai     import Client
from kowalski.internal.config import KOWALSKI_PATH
from os                       import path
from frontmatter              import load
from kowalski.cmd.add         import addCmd


def kaboomCmd(note_name: str, prompt: str):
    note_path = path.join(KOWALSKI_PATH, f"{note_name}.md")
    note_md = load(note_path)
    client = Client(MODEL)
    content = client.completion(note_md.content, prompt)
    addCmd(content)