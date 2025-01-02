from kowalski_core.features.ui import *

class Book():

    def __init__(self, name: str, notes_count: str):
        self.name = name
        self.notes_count = notes_count

    def __str__(self):
        return f'• {self.name} [{in_yellow(self.notes_count)}]'