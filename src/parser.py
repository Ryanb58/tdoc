"""Parse a python file's docstrings to markdown."""

import ast

NODE_TYPES = {
    ast.ClassDef: 'Class',
    ast.FunctionDef: 'Function/Method',
    ast.Module: 'Module'
}

classes = []

functions_by_class = {}


if __name__ == '__main__':
    # Parse a single file?
    pass
