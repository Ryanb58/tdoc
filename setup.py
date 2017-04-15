from setuptools import setup, find_packages

setup(
    name='tdoc',
    version='0.1',
    description='Python To Markdown Documentation Tool',
    author='Taylor Brazelton',
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
