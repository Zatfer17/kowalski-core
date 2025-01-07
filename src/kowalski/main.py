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
    #print(WELCOME_IMAGE)
    print(WELCOME_TEXT)

def cli():
    parser = ArgumentParser(prog="kv", description="")
    subparsers = parser.add_subparsers(dest="command", required=False)
    
    add_parser = subparsers.add_parser("add", help="Add a new note")
    add_parser.add_argument("note", type=str, nargs="?", default=None, help="The note to add (optional). Omitting this argument will open the default editor")

    save_parser = subparsers.add_parser("save", help="Save a link")
    save_parser.add_argument("link", type=str, help="The link to save. Youtube videos will be transcribed, normal URLs will be retrieved")

    open_parser = subparsers.add_parser("open", help="Open a note")
    open_parser.add_argument("note", type=str, help="The note to open")

    remove_parser = subparsers.add_parser("remove", help="Remove a note")
    remove_parser.add_argument("note", type=str, help="The note to remove")

    list_parser = subparsers.add_parser("list", help="List all notes")
    list_parser.add_argument("--keyword", type=str, nargs="?", help="The keyword to filter notes with (optional)")
    list_parser.add_argument("--limit", type=int, nargs="?", default=100, help="The number of notes to display (optional)")
    
    kaboom_parser = subparsers.add_parser("kaboom", help="Transform a note with AI")
    kaboom_parser.add_argument("note", type=str, help="The note to transform with AI")
    kaboom_parser.add_argument("--prompt", type=str, nargs="?", default="Please summarize this note", help="The prompt to trasnform the note with")
    
    sync_parser = subparsers.add_parser("sync", help="Sync notes with remote")

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
            case "open":
                from kowalski.cmd.open import openCmd
                openCmd(args.note)
            case "remove":
                from kowalski.cmd.remove import removeCmd
                removeCmd(args.note)
            case "list":
                from kowalski.cmd.list import listCmd
                listCmd(args.keyword, args.limit)
            case "kaboom":
                from kowalski.cmd.kaboom import kaboomCmd
                kaboomCmd(args.note, args.prompt)
            case "sync":
                from kowalski.cmd.sync import syncCmd
                syncCmd()