import typer
import os
import time

from typing_extensions import Annotated
from kowalski_core.features.utils.utils import run


HOME = os.getenv('HOME')
NOTES_PATH = os.path.join(HOME, '.kowalski')
EDITOR = os.getenv('EDITOR')

app = typer.Typer()

@app.command()
def add(
    book: Annotated[str, typer.Argument(help="The book you want to add the note to")],
    note: Annotated[str, typer.Argument(help="The note/url/youtube link you want to add")] = None
) -> None:

    book_path = os.path.join(NOTES_PATH, book)
    run(f'mkdir -p {book_path}')

    note_name = f'{int(time.time())}.md'
    note_path = os.path.join(book_path, note_name)
    
    if note is None:
        run(f'touch {note_path}')
        run(f'{EDITOR} {note_path}')
    else:
        run(f'echo {note} > {note_path}')


@app.command()
def transform() -> None:
    return