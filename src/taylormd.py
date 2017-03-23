"""TaylorMD."""
from distutils.dir_util import copy_tree
import os

import click

from mkdocs.commands.serve import serve
from parser import parse_file

exclude = ('venv')


@click.group()
def cli():
    """CLI Command Group."""
    pass


def populate_docs_with_index():
    """Populate docs/ with an index file."""
    index_path = os.path.join("docs/", "index.md")
    index_exists = os.path.exists(index_path)
    if not index_exists:
        copy_tree("default_docs/", "docs/")


@click.command()
@click.argument('folder')
def generate(folder):
    """Simple program that greets NAME for a total of COUNT times."""
    print("You want to search in folder: " + str(folder))
    populate_docs_with_index()
    for dirpath, dnames, fnames in os.walk(folder):
        [dnames.remove(d) for d in list(dnames) if d in exclude]
        for f in fnames:
            if f.endswith(".py"):
                file_base = folder
                file_path = dirpath[len(file_base):]
                parse_file(file_base, file_path, f)


@click.command()
def run():
    """Create a local server to view markdown files as website."""
    serve()


cli.add_command(generate)
cli.add_command(run)

if __name__ == '__main__':
    cli()

