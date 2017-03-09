"""Parse a python file's docstrings to markdown."""

import ast

NODE_TYPES = {
    ast.ClassDef: 'Class',
    ast.FunctionDef: 'Function/Method',
    ast.Module: 'Module'
}

classes = []

functions_by_class = {}


def parse_file(file_path):
    print(file_path)

    with open(file_path) as fp:
        source = fp.read()
        tree = ast.parse(source)

        from pdb import set_trace;set_trace()

        """
        class FuncLister(ast.NodeVisitor):
            def visit_FunctionDef(self, node):
                print(node.name)
                from pdb import set_trace;set_trace()
                self.generic_visit(node)

            def visit_ClassDef(self, node):
                print(node.name)
                self.generic_visit(node)

        FuncLister().visit(tree)
        """
        """
        # Walk the tree and build data structure.
        for node in ast.walk(tree):
            if isinstance(node, tuple(NODE_TYPES)):
                docstring = ast.get_docstring(node)
                print(docstring)
                from pdb import set_trace;set_trace()
        """


if __name__ == '__main__':
    # Parse a single file?
    pass
