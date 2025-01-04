import click

from kowalski_core.internal.database import Database
from kowalski_core.internal.book     import Book
from kowalski_core.internal.note     import Note


@click.command(help="List books or notes")
@click.option("-b", "--book", required=False, help="The book to list notes from")
def list(book: str):
    
    db = Database()

    if book:
        results = [Note(x[0], x[1], x[2], x[3], x[4]) for x in db.list_notes(book)]
    else:
        results = [Book(x[0], x[1]) for x in db.list_books()]

    [click.echo(x) for x in results]

    return results