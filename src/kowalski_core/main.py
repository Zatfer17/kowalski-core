from argparse               import ArgumentParser
from kowalski_core.cmd.add  import addCmd
from kowalski_core.cmd.list import listCmd
from kowalski_core.cmd.edit import editCmd
from kowalski_core.cmd.show import showCmd


def cli():
    parser = ArgumentParser(prog="kv", description="")
    subparsers = parser.add_subparsers(dest="command", required=True)
    
    add_parser = subparsers.add_parser("add", help="Add a new note")
    add_parser.add_argument("content", help="Content of the note")
    
    subparsers.add_parser("list", help="List all notes")
    
    edit_parser = subparsers.add_parser("edit", help="Edit a note")
    edit_parser.add_argument("note_id", type=int, help="The ID of the note to edit")
    
    open_parser = subparsers.add_parser("show", help="Show a note")
    open_parser.add_argument("note_id", type=int, help="The ID of the note to show")
    
    search_parser = subparsers.add_parser("search", help="Search notes by keywords")
    search_parser.add_argument("keywords", help="The keywords to search for")

    args = parser.parse_args()
    print("--------------------------")
    print(f"Command  : {args.command}")
    print(f"Arguments: {vars(args)}")
    print("--------------------------")

    match args.command:
        case "add":
            addCmd(args.content)
        case "list":
            listCmd()
        case "edit":
            editCmd(args.note_id)
        case "show":
            showCmd(args.note_id)