import click
from commands import decode, shell


@click.group(help="CLI tool for methane-sensor")
def cli():
    pass


cli.add_command(decode.decode)
cli.add_command(shell.shell)


if __name__ == '__main__':
    cli()
