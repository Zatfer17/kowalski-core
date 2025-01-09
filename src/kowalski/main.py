# PYTHON_ARGCOMPLETE_OK
import argparse
import argcomplete


def note_completer(prefix, parsed_args, **kwargs):
    from kowalski.cmd.list import list_cmd
    return [note.name for note in list_cmd(None) if note.name.startswith(prefix)]

def cli():
    
    parser = argparse.ArgumentParser(prog="ko", description="")
    subparsers = parser.add_subparsers(dest="command", required=False)

    add_parser = subparsers.add_parser("add", help="Add a new note")
    add_parser.add_argument("--content", type=str, nargs="?", default=None, help="The content to add (optional). Omitting this argument will open the default editor")

    save_parser = subparsers.add_parser("save", help="Save a url")
    save_parser.add_argument("url", type=str, help="The url to save. Youtube videos will be transcribed, normal URLs will be retrieved")
    
    list_parser = subparsers.add_parser("list", help="List all notes")
    list_parser.add_argument("--limit", type=int, nargs="?", default=None, help="The number of notes to display (optional)")

    find_parser = subparsers.add_parser("find", help="Find a note")
    find_parser.add_argument("content", type=str, help="The content to search for")

    show_parser = subparsers.add_parser("show", help="Show a note")
    show_parser.add_argument("name", type=str, help="The name of the note to show").completer = note_completer

    edit_parser = subparsers.add_parser("edit", help="Edit a note")
    edit_parser.add_argument("name", type=str, help="The name of the note to edit").completer = note_completer
    edit_parser.add_argument("--content", type=str, nargs="?", default=None, help="The content to replace (optional). Omitting this argument will open the default editor")

    remove_parser = subparsers.add_parser("remove", help="Remove a note")
    remove_parser.add_argument("name", type=str, help="The name of the note to remove").completer = note_completer

    argcomplete.autocomplete(parser)
    args = parser.parse_args()

    match args.command:
        case "add":
            from kowalski.cmd.add  import add_cmd
            add_cmd(args.content)
        case "save":
            from kowalski.cmd.save import save_cmd
            save_cmd(args.url)
        case "list":
            from kowalski.cmd.list import list_cmd
            list_cmd(args.limit)
        case "find":
            from kowalski.cmd.find import find_cmd
            find_cmd(args.content)
        case "show":
            from kowalski.cmd.show import show_cmd
            show_cmd(args.name)
        case "edit":
            from kowalski.cmd.edit import edit_cmd
            edit_cmd(args.name, args.content)
        case "remove":
            from kowalski.cmd.remove import remove_cmd
            remove_cmd(args.name)