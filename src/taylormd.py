import os

import click

from parser import parse_file

exclude = ('venv')


@click.command()
@click.argument('folder')
def generate(folder):
    """Simple program that greets NAME for a total of COUNT times."""
    print("You want to search in folder: " + str(folder))
    for dirpath, dnames, fnames in os.walk(folder):
        [dnames.remove(d) for d in list(dnames) if d in exclude]
        for f in fnames:
            if f.endswith(".py"):
                file_path = os.path.join(dirpath, f)
                parse_file(file_path)


if __name__ == '__main__':
    generate()
