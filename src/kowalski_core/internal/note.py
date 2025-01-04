import hashlib
import os
import click

from datetime import datetime


TEMPLATE = """---
id: {}
updated_at: {}
source: {}
media: {}
---
{}"""

class Note():

    def __init__(self, book: str, updated_at: datetime | str, media: str, source: str, content: str):

        if type(updated_at) == str:
            updated_at = datetime.strptime(updated_at, "%Y-%m-%d %H:%M:%S.%f")

        self.id         = hashlib.sha1(f"{book}.{content}".encode()).hexdigest()
        self.slug       = f"{updated_at.strftime("%y%m%d")}:{self.id[:4]}"
        self.book       = book
        self.updated_at = updated_at
        self.media      = media
        self.source     = source
        self.content    = content

    def __str__(self):
        return "{} {} -> {}".format(
            click.style(f"[{self.slug}]", fg="yellow", bold=True),
            click.style(f"[{self.media.ljust(4)}]", fg="green", bold=False),
            f"{self.content[:50].replace("\n", " ")}[...]"
        )