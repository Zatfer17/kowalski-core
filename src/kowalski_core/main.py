from argparse               import ArgumentParser
from kowalski_core.cmd.add  import addCmd
from kowalski_core.cmd.save  import saveCmd
from kowalski_core.cmd.list import listCmd
from kowalski_core.cmd.edit import editCmd
from kowalski_core.cmd.show import showCmd
from kowalski_core.cmd.kaboom import kaboomCmd
from kowalski_core.cmd.sync import syncCmd


def cli():
    parser = ArgumentParser(prog="kv", description="")
    subparsers = parser.add_subparsers(dest="command", required=True)
    
    add_parser = subparsers.add_parser("add", help="Add a new note")
    add_parser.add_argument("content", type=str, nargs="?", default=None, help="The note to add (optional)")

    save_parser = subparsers.add_parser("save", help="Save a link")
    save_parser.add_argument("link", type=str, help="The link to save")
    
    list_parser = subparsers.add_parser("list", help="List all notes")
    list_parser.add_argument("--limit", type=int, nargs="?", default=50, help="The number of notes to display (optional)")
    
    edit_parser = subparsers.add_parser("edit", help="Edit a note")
    edit_parser.add_argument("note", type=str, help="The note to edit")
    
    open_parser = subparsers.add_parser("show", help="Show a note")
    open_parser.add_argument("note", type=str, help="The note to show")

    kaboom_parser = subparsers.add_parser("kaboom", help="Kaboom a note")
    kaboom_parser.add_argument("note", type=str, help="The note to kaboom")
    kaboom_parser.add_argument("prompt", type=str, nargs="Please summarize this note", default=50, help="The prompt to kaboom with")
    
    sync_parser = subparsers.add_parser("sync", help="Sync notes")

    args = parser.parse_args()

    match args.command:
        case "add":
            addCmd(args.content)
        case "save":
            saveCmd(args.link)
        case "list":
            listCmd(args.limit)
        case "edit":
            editCmd(args.note)
        case "show":
            showCmd(args.note)
        case "kaboom":
            kaboomCmd(args.note, args.prompt)
        case "sync":
            syncCmd()