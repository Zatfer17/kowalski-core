from kowalski_core.features.ui import *


class Note():
    
    def __init__(self, id: str, book: str, date: str, media: str, source: str, content: str):
        self.id = id
        self.book = book
        self.date = date
        self.media = media
        self.source = source
        self.content = content

    def __str__(self):
        return f'''---
id: {self.id}
book: {self.book}
date: {self.date}
media: {self.media}
source: {self.source}
---

{self.content}
'''

class NotePreview(Note):

    def __str__(self):
        text = self.content if len(self.content) < 50 else f'{self.content[:50]}[...]'
        return f'• [{in_yellow(self.book)}:{in_yellow(self.id)}] [{in_green(self.date)}] [{in_green(self.media.ljust(4))}] {text}'
    

