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

        output_folder = "docs/"
        file_name = "output.md"

        with open(output_folder + file_name, "w") as output_file:

            class FuncLister(ast.NodeVisitor):
                def visit_FunctionDef(self, node):
                    output_file.write("#### Function: " + node.name)
                    output_file.write('\n')
                    output_file.write("`" + ast.get_docstring(node) + "`")
                    output_file.write('\n')
                    output_file.write('\n')
                    self.generic_visit(node)

                def visit_ClassDef(self, node):
                    output_file.write("#### Class: " + node.name)
                    output_file.write('\n')
                    output_file.write("`" + ast.get_docstring(node) + "`")
                    output_file.write('\n')
                    output_file.write('\n')
                    self.generic_visit(node)

            FuncLister().visit(tree)



if __name__ == '__main__':
    # Parse a single file?
    pass
