import click


@click.command()
@click.argument('folder')
def generate(folder):
    """Simple program that greets NAME for a total of COUNT times."""
    print("You want to search in folder: " + str(folder))


if __name__ == '__main__':
    generate()
