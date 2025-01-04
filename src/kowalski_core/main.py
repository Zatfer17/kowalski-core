import click

from kowalski_core.cmd.init   import init 
from kowalski_core.cmd.add    import add 
from kowalski_core.cmd.list   import list
from kowalski_core.cmd.edit   import edit
from kowalski_core.cmd.open   import open
from kowalski_core.cmd.kaboom import kaboom


@click.group()
def cli():
    pass

cli.add_command(init)
cli.add_command(add)
cli.add_command(list)
cli.add_command(edit)
cli.add_command(open)
cli.add_command(kaboom)