"""TDoc."""
from distutils.dir_util import copy_tree
import os

import click

from mkdocs.commands.serve import serve
from .parser import parse_file

exclude = ('venv')

MKDOCS_YML = 'mkdocs.yml'
DOCS_FOLDER = "docs/"
DEFAULT_DOCS_FOLDER = "default_docs/"


@click.group()
def cli():
    """CLI Command Group."""
    pass


def copy_default_docs():
    """Populate docs/ with an index file."""
    # Create `docs/` folder if does not exist.
    docs_exist = os.path.exists(DOCS_FOLDER)
    if not docs_exist:
        os.makedirs(DOCS_FOLDER)

    default_docs_exists = os.path.exists(DEFAULT_DOCS_FOLDER)
    # If `default_docs` directory exists, go ahead and copy it into `docs/`.
    if default_docs_exists:
        copy_tree(DEFAULT_DOCS_FOLDER, DOCS_FOLDER)

    # Check if index exists in docs.
    index_path = os.path.join(DOCS_FOLDER, "index.md")
    index_exists = os.path.exists(index_path)

    # If no index exists, then create one in the `docs/` directory.
    if not index_exists:
        with open(index_path, 'w') as out:
            out.write('### Welcome To Your Documentation\n')
            out.write('\n')
            out.write('Welcome to your documentation.\n')
            out.write('\n')
            out.write('To replace this page, simply replace your index.md')
            out.write(' file inside of your `default_docs` folder.')


@click.command()
@click.option(
    '--folder',
    prompt="Project path",
    type=click.Path(exists=True),
    help="The source path for API documentation generation."
)
def generate(folder):
    """Simple program that greets NAME for a total of COUNT times."""
    print("You want to search in folder: " + str(folder))
    copy_default_docs()
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
    mkdocs_yml_exists = os.path.exists(MKDOCS_YML)
    if not mkdocs_yml_exists:
        with open(MKDOCS_YML, 'w') as out:
            out.write("site_name: My Docs\n")
            out.write("theme: 'mkdocs'\n")
    serve()


cli.add_command(generate)
cli.add_command(run)

if __name__ == '__main__':
    cli()

