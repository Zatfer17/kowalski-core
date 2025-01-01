import os

from kowalski_core.features.note import Note


class Downloader():

    def __init__(self, path: str = '.kowalski/export'):
        self.path = path
        if not os.path.exists(path):
            os.makedirs(path)

    def download(self, note: Note):
        note_dir = os.path.join(self.path, note.book)
        if not os.path.exists(note_dir):
            os.makedirs(note_dir)
        note_name = f'{note.book}-{note.id}-{note.date}.md'
        note_path = os.path.join(note_dir, note_name)
        with open(note_path, 'w') as f:
            f.write(note.__str__())