from setuptools import setup, find_packages

setup(
    name='tdoc',
    version='0.2',
    description='Python To Markdown Documentation Tool',
    author='Taylor Brazelton',
    author_email='ryanb58@live.com',
    url='https://github.com/Ryanb58/tdoc',
    keywords=['doc', 'gen', 'api', 'ast', 'auto'],
    packages=find_packages(),
    install_requires=[
        'Click',
        'mkdocs',
    ],
    entry_points='''
        [console_scripts]
        tdoc=src.tdoc:cli
    ''',
)
