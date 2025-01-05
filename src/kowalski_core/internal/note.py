from datetime import datetime
from json     import dumps


TEMPLATE = """---
id: {}
created: {}
updated: {}
---

{}"""

class Note():

    def __init__(self, id: str, created: datetime, updated: datetime, content: str):
        self.id      = id
        self.created = created
        self.updated = updated
        self.content = content

    def refresh_updated(self):
        self.updated = datetime.now()

    def write(self, path: str):
        f = open(path, 'w')
        f.write(TEMPLATE.format(self.id, self.created, self.updated, self.content))

    def description(self, mode: str):
        match mode:
            case 'short':
                content = self.content
                content = content if len(content) < 50 else f"{content[:50]}[...]"
                content = content.replace("\n", " ")
                return f"[{self.id}] {content}"
            case 'long':
                return TEMPLATE.format(self.id, self.created, self.updated, self.content)
            case 'json':
                return dumps(self.__dict__, indent=4, default=str)