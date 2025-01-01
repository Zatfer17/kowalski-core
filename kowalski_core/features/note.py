from kowalski_core.features.ui import in_yellow, in_green


class Note():

    def __init__(self, book: str, id: str, date: str, media: str, source: str, content: str, distance: float = None, full: bool = False):
        self.book = book
        self.id = id
        self.date = date
        self.media = media
        self.source = source
        self.content = content
        self.distance = distance
        self.full = full

    def __str__(self):
        if self.full:
            return f'''
---
book: {self.book}
id: {self.id}
date: {self.date}
media: {self.media}
source: {self.source}
---

{self.content}
'''
        else:
            text = self.content if len(self.content) < 50 else f'{self.content[:50]}[...]'
            return f'• [{in_green(self.book)}] [{in_yellow(self.id)}] [{in_green(self.date)}] [{in_green(self.media.ljust(4))}] {text}'