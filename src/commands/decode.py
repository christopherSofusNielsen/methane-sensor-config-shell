import click


@click.command(help="Decode lora-wan packages")
@click.argument("path", type=click.Path(exists=True, ))
def decode(path):
    print(f"decode {path}")
