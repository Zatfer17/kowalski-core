import click

from kowalski_core.internal.database import Database


greeter = """
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
             *+*#+#  +*+=+*                       
"""

@click.command(help="Initialize the database")
@click.option("-f", "--force", is_flag=True, required=False,  help="Force reinitialization")
def init(force: bool):

    click.echo(greeter)
    click.echo("Welcome to Kowalski!")

    db = Database()

    if force:
        db.delete()
        
    db.initialize()