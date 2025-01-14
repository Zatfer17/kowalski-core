import os

from datetime import datetime

from kowalski.internal.utils import colored, bold


TEMPLATE = """---
name: {}
created: {}
tags: {}
---

{}"""

class Note():

    def __init__(self, name: str, created: datetime, tags: list[str], content: str):

        self.name    = name
        self.created = created
        self.tags    = tags
        self.content = content

    def format(self):

        return TEMPLATE.format(self.name, self.created, self.tags, self.content)

    def write(self, path):

        f = open(os.path.join(path, self.name), "w")
        f.write(self.format())

    def __str__(self):

        name = self.name
        name = colored(235, 171, 52, name)
        name = bold(name)

        tags = str(self.tags)
        tags = tags.replace("[", "").replace("]", "")
        tags = tags.replace("'", "")
        tags = tags[:17]
        tags = tags.ljust(20, ".")
        tags = colored(0, 168, 138, tags)

        content = self.content
        content = content.replace("\n", " ")
        content = content[:27]
        content = content.ljust(30, ".")
        content = bold(content)

        return f"({name}): [🗞  {content}] [🏷️  {tags}]"