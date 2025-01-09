import os

from kowalski.internal.config import load_config


def remove_cmd(name: str):

    PATH, _ = load_config()

    note_path = os.path.join(PATH, name)
    os.remove(note_path)