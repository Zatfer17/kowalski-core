import click

from kowalski_core.internal.database import Database


@click.command(help="Initialize the database")
@click.option("-f", "--force", is_flag=True, required=False,  help="Force reinitialization")
def init(force: bool):

    db = Database()

    if force:
        db.delete()
        
    db.initialize()