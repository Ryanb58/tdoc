# TDoc
A python documentation generator.


### Installation

```
pip install tdoc
```
[pypi](https://pypi.python.org/pypi/tdoc)



### Generate the markdown documentation.

```
tdoc generate --folder ./testfiles
```

### Run a local webserver to view your documentation.

```
tdoc serve
```

### Non Auto Generated Docs:

To include custom markdown files simply create a folder called
`default_docs` and place any and all markdown files inside of it. This
directory will be copied over into the `docs` folder before any auto
generation.

### Screenshot of Results using the Material Theme:

![Screen Shot](imgs/screenshot.png?raw=true "Screen Shot")


### Installing As Editable:

```
pip install --editable .
```