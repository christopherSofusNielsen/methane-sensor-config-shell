import click
from commands import decode


@click.group(help="CLI tool for methane-sensor")
def cli():
    pass


cli.add_command(decode.decode)


if __name__ == '__main__':
    cli()
