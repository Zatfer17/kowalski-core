import typer
import sys

from kowalski_core.features.intent import Intent
from kowalski_core.features.note   import Note
from kowalski_core.features.analysis     import Analysis
from typing_extensions import Annotated


app = typer.Typer()


@app.command()
def collect(
    source: Annotated[str, typer.Argument(help="The piece of information you want to collect (note, url, youtube link)")] = "",
    intent: Annotated[Intent, typer.Option(help="What Kowalski should do with that piece of information")] = Intent.SUMMARIZE
) -> None:

    if not sys.stdin.isatty():
        source = sys.stdin.read().strip()

    note = Note(source, intent)
    note.write_note()
    print(note.get_note_path())

@app.command()
def transform(
    source: Annotated[str, typer.Argument(help="The note you want to transform (path)")] = ""
) -> None:
    
    if not sys.stdin.isatty():
        source = sys.stdin.read().strip()

    analysis = Analysis(source=source)
    analysis.run()