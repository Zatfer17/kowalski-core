import click

from datetime                        import datetime
from kowalski_core.internal.parse    import get_url_content, get_yt_content
from kowalski_core.internal.note     import Note
from kowalski_core.internal.database import Database


@click.command(help="Add a note")
@click.option("-b", "--book", required=True,  help="The book to add the note to")
@click.option("-n", "--note", required=False, help="The note to add")
@click.option("-u", "--url", required=False, help="The url to add")
@click.option("-y", "--youtube", required=False, help="The youtube video to add")
def add(book: str, note: str, url: str, youtube: str):

    provided_options = [opt for opt in (note, url, youtube) if opt is not None]

    match len(provided_options):
        case 0:
            media   = "note"
            source  = None
            content = click.edit()
        case 1:
            if note:
                media   = "note"
                source  = None
                content = note
            elif url:
                media   = "url"
                source  = url
                content = get_url_content(url)
            else:
                media   = "youtube"
                source  = youtube
                content = get_yt_content(youtube)
        case 2 | 3:
            raise click.UsageError("Wrong parameters...")
        
    updated_at = datetime.today()

    note = Note(book, updated_at, media, source, content)

    db = Database()
    db.insert(note)

    click.echo(note)