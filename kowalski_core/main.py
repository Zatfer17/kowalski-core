import typer

from typing_extensions import Annotated
from kowalski_core.features.database import Database
from kowalski_core.features.parser import Parser


app = typer.Typer()
db = Database()
parser = Parser()

@app.command()
def add(
    book: Annotated[str, typer.Argument()],
    note: Annotated[str, typer.Argument()]
) -> None:

    media, source, content = parser.get_type_source_content(note)
    db.insert_note(book, media, source, content)

@app.command()
def list(
    book: Annotated[str, typer.Argument()] = None,
    limit: Annotated[int, typer.Argument()] = 10
) -> None:

    if book is None:
        print(*db.list_books(), sep='\n')
    else:
        print(*db.list_notes(book, limit), sep='\n')

@app.command()
def find(
    keywords: Annotated[str, typer.Argument()],
    book: Annotated[str, typer.Argument()] = None,
) -> None:

    if len(keywords.split(' ')) > 1:
        print(*db.query_notes(keywords, book, exact=False), sep='\n')
    else:
        print(*db.query_notes(keywords, book, exact=True), sep='\n')

@app.command()
def view(
    id: Annotated[str, typer.Argument()],
) -> None:
    
    print(*db.get_note(id), sep='\n')