import click

from datetime                        import datetime
from kowalski_core.internal.database import Database
from kowalski_core.internal.llm      import OpenAI
from kowalski_core.internal.note     import Note


@click.command(help="Kaboom a note with AI")
@click.argument("slug", required=True)
@click.option("-p", "--prompt", required=False, default = 'Summarize this:', help="The prompt to run the completion with")
@click.option("-m", "--model", required=False, default = 'gpt-4o-mini', help="The model to run the completion with")

def kaboom(slug: str, prompt: str, model: str):

    db = Database()
    _, book, content = db.get_note(slug)

    client = OpenAI()

    updated_at = datetime.today()
    media   = "ai"
    source  = slug
    content = client.completion(prompt, content, model)

    note = Note(book, updated_at, media, source, content)

    db = Database()
    db.insert(note)

    click.echo(note)