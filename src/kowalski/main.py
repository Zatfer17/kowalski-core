from argparse import ArgumentParser
from warnings import filterwarnings

filterwarnings("ignore")


WELCOME_IMAGE = """
                           %%%                   
                         =:-%#%#                 
                        .....--..                
                        ...:==-=:                
                       .....-+-..%               
                       =.........*               
                       +.........#               
                      #*.........#%              
                      #=.........-%              
                      %...........+#             
                     %=...........:%             
                     #:............=             
                     %.............-#            
                     %.............:%            
                     %............::%            
                     %...........::-@%           
                     @.........:::-=@@           
                      .......:::---=             
                       :::::::---==              
                        :-----==++               
                      +=+*#  *##**              
                      *+*#+#  +*+=+*"""

WELCOME_TEXT = """
██╗  ██╗ ██████╗ ██╗    ██╗ █████╗ ██╗     ███████╗██╗  ██╗██╗
██║ ██╔╝██╔═══██╗██║    ██║██╔══██╗██║     ██╔════╝██║ ██╔╝██║
█████╔╝ ██║   ██║██║ █╗ ██║███████║██║     ███████╗█████╔╝ ██║
██╔═██╗ ██║   ██║██║███╗██║██╔══██║██║     ╚════██║██╔═██╗ ██║
██║  ██╗╚██████╔╝╚███╔███╔╝██║  ██║███████╗███████║██║  ██╗██║
╚═╝  ╚═╝ ╚═════╝  ╚══╝╚══╝ ╚═╝  ╚═╝╚══════╝╚══════╝╚═╝  ╚═╝╚═╝"""


def kowalscii():
    print(WELCOME_IMAGE)
    print(WELCOME_TEXT)

def cli():
    parser = ArgumentParser(prog="kv", description="")
    subparsers = parser.add_subparsers(dest="command", required=False)
    
    add_parser = subparsers.add_parser("add", help="Add a new note")
    add_parser.add_argument("note", type=str, nargs="?", default=None, help="The note to add (optional)")

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
    kaboom_parser.add_argument("--prompt", type=str, nargs="?", default="Please summarize this note", help="The prompt to kaboom with")

    remove_parser = subparsers.add_parser("remove", help="Remove a note")
    remove_parser.add_argument("note", type=str, help="The note to remove")
    
    sync_parser = subparsers.add_parser("sync", help="Sync notes")

    args = parser.parse_args()
    
    if args.command is None:
        kowalscii()
    else:
        match args.command:
            # Not PEP8 compliant, but speed is meh otherwise
            case "add":
                from kowalski.cmd.add import addCmd
                addCmd(args.note)
            case "save":
                from kowalski.cmd.save import saveCmd
                saveCmd(args.link)
            case "list":
                from kowalski.cmd.list import listCmd
                listCmd(args.limit)
            case "edit":
                from kowalski.cmd.edit import editCmd
                editCmd(args.note)
            case "show":
                from kowalski.cmd.show import showCmd
                showCmd(args.note)
            case "kaboom":
                from kowalski.cmd.kaboom import kaboomCmd
                kaboomCmd(args.note, args.prompt)
            case "remove":
                from kowalski.cmd.remove import removeCmd
                removeCmd(args.note)
            case "sync":
                from kowalski.cmd.sync import syncCmd
                syncCmd()