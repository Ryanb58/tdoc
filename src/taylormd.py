import os

import click


@click.command()
@click.argument('folder')
def generate(folder):
    """Simple program that greets NAME for a total of COUNT times."""
    print("You want to search in folder: " + str(folder))
    for dirpath, dnames, fnames in os.walk(folder):
        for f in fnames:
            if f.endswith(".py"):
                print(os.path.join(dirpath, f))


if __name__ == '__main__':
    generate()
