import typer
import sys

from kowalski_core.features.collect.note       import Note
from kowalski_core.features.transform.intent   import Intent
from kowalski_core.features.transform.analysis import Analysis

from typing_extensions import Annotated


app = typer.Typer()


@app.command()
def collect(
    source: Annotated[str, typer.Argument(help="The piece of information you want to collect (note, url, youtube link)")] = ""
) -> None:

    if not sys.stdin.isatty():
        source = sys.stdin.read().strip()

    note = Note(source=source)
    note.write_note()
    print(note.path)

@app.command()
def transform(
    source: Annotated[str, typer.Argument(help="The note you want to transform (path)")] = "",
    intent: Annotated[Intent, typer.Option(help="What Kowalski should do with that piece of information")] = Intent.SUMMARIZE
) -> None:
    
    if not sys.stdin.isatty():
        source = sys.stdin.read().strip()

    note = Note(source=source, is_path=True)
    analysis = Analysis(note=note)
    analysis.run(intent=intent)