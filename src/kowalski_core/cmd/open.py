import click

from kowalski_core.internal.database import Database


@click.command(help="Open a note")
@click.argument("slug", required=True)
def open(slug: str):
   
    db = Database()
    _, _, content = db.get_note(slug)

    click.edit(content)