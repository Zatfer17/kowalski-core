import os
import subprocess


def run(command: str):
    return subprocess.run(command.split(' '))


class Editor():

    def __init__(self, default: str = os.getenv('EDITOR')):
        self.default = default

    def create_file(self, path: str = '.temp'):
        run(f'touch {path}')

    def delete_file(self, path: str = '.temp'):
        run(f'rm {path}')

    def load_file(self, content: str, path: str = '.temp'):
        with open(path, 'w') as f:
            f.write(content)

    def open(self, path: str = '.temp'):
        run(f'{self.default} {path}')
        media  = 'note'
        source = None
        with open(path) as f:
            return media, source, f.read()