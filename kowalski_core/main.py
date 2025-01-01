import typer
import warnings

from typing_extensions import Annotated
from datetime import datetime

from kowalski_core.features.editor import Editor
from kowalski_core.features.database import Database
from kowalski_core.features.parser import Parser
from kowalski_core.features.book import Book
from kowalski_core.features.note import Note, NotePreview
from kowalski_core.features.download import Downloader
from kowalski_core.features.magic import Magician


warnings.filterwarnings('ignore')

app = typer.Typer()
editor = Editor()
db = Database()
parser = Parser()
downloader = Downloader()
magician = Magician()

@app.command()
def add(
    book: Annotated[str, typer.Argument()],
    note: Annotated[str, typer.Argument()] = None
) -> None:

    if note is None:
        editor.create_temp_file()
        media, source, content = editor.open()
        editor.delete_temp_file()
    else:
        media, source, content = parser.get_type_source_content(note)
    date = datetime.today().strftime('%Y-%m-%d %H:%M:%S')
    db.insert_note(book, date, media, source, content)

@app.command()
def list(
    book: Annotated[str, typer.Argument()] = None,
    limit: Annotated[int, typer.Argument()] = 10
) -> None:

    if book is None:
        [print(Book(x[0], x[1])) for x in db.list_books()]
    else:
        [print(NotePreview(x[0], x[1], x[2], x[3], x[4], x[5])) for x in db.list_notes(book, limit)]

@app.command()
def find(
    keywords: Annotated[str, typer.Argument()],
    book: Annotated[str, typer.Argument()] = None,
) -> None:

    [print(NotePreview(x[0], x[1], x[2], x[3], x[4], x[5])) for x in db.find_note(keywords, book)]

@app.command()
def view(
    id: Annotated[str, typer.Argument()],
) -> None:
    
    note_raw = db.view_note(id)
    note = Note(note_raw[0], note_raw[1], note_raw[2], note_raw[3], note_raw[4], note_raw[5])
    print(note)


@app.command()
def download(
    id: Annotated[str, typer.Argument()],
) -> None:
    
    note_raw = db.view_note(id)
    note = Note(note_raw[0], note_raw[1], note_raw[2], note_raw[3], note_raw[4], note_raw[5])
    downloader.download(note)

@app.command()
def magic(
    id: Annotated[str, typer.Argument()],
    spell: Annotated[str, typer.Argument()] = None
):
    
    note_raw = db.view_note(id)
    note = Note(note_raw[0], note_raw[1], note_raw[2], note_raw[3], note_raw[4], note_raw[5])
    media, source, content = magician.trick(note, spell)
    date = datetime.today().strftime('%Y-%m-%d %H:%M:%S')
    db.insert_note(note.book, date, media, source, content)

@app.command()
def edit(
    id: Annotated[str, typer.Argument()]
):
    note_raw = db.view_note(id)
    note = Note(note_raw[0], note_raw[1], note_raw[2], note_raw[3], note_raw[4], note_raw[5])

    editor.create_file()
    editor.load_file(note.content)
    _, _, content = editor.open()
    editor.delete_file()

    date = datetime.today().strftime('%Y-%m-%d %H:%M:%S')
    db.update_note(note.id, date, content)