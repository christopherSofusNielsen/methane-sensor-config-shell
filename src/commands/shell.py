import click
from shell_menu_api import shell as term


@click.command(help="Open shell to configure sensor")
def shell():
    while(True):
        options = ["Option 1", "Option 2", "Option 3"]
        selected = term.show_menu(options)
        if(selected == None):
            return
        print(selected)
