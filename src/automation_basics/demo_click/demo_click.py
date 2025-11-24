import click


@click.command()
def main():
    click.echo("This cli is built with click. ")


@click.command()
@click.argument("name")
def greeting(name):
    click.echo(f"Hello, {name}")


if __name__ == "__main__":
    greeting()
