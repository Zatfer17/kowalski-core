from argparse               import ArgumentParser
from kowalski_core.cmd.add  import addCmd
from kowalski_core.cmd.list import listCmd
from kowalski_core.cmd.edit import editCmd
from kowalski_core.cmd.show import showCmd
from kowalski_core.cmd.sync import syncCmd


def cli():
    parser = ArgumentParser(prog="kv", description="")
    subparsers = parser.add_subparsers(dest="command", required=True)
    
    add_parser = subparsers.add_parser("add", help="Add a new note")
    add_parser.add_argument("content", nargs="?", default=None, help="The note to add (optional)")
    
    list_parser = subparsers.add_parser("list", help="List all notes")
    list_parser.add_argument("--limit", type=int, nargs="?", default=50, help="The number of notes to display (optional)")
    
    edit_parser = subparsers.add_parser("edit", help="Edit a note")
    edit_parser.add_argument("note", type=int, help="The note to edit")
    
    open_parser = subparsers.add_parser("show", help="Show a note")
    open_parser.add_argument("note", type=int, help="The note to show")
    
    sync_parser = subparsers.add_parser("sync", help="Sync notes")

    args = parser.parse_args()

    match args.command:
        case "add":
            addCmd(args.content)
        case "list":
            listCmd(args.limit)
        case "edit":
            editCmd(args.note)
        case "show":
            showCmd(args.note)
        case "sync":
            syncCmd()