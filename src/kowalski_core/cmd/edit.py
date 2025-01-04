import click

from datetime                        import datetime
from kowalski_core.internal.database import Database
from kowalski_core.internal.note     import Note


@click.command(help="Edit a note")
@click.argument("slug", required=True)
def edit(slug: str):

    db = Database()
    old_id, book, old_content = db.get_note(slug)

    updated_at = datetime.today()
    media   = "note"
    source  = None
    content = click.edit(old_content)

    note = Note(book, updated_at, media, source, content)

    db = Database()
    db.insert(note)
    db.remove(old_id)

    click.echo(note)