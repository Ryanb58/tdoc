"""Parse a python file's docstrings to markdown."""

import ast
import os

NODE_TYPES = {
    ast.ClassDef: 'Class',
    ast.FunctionDef: 'Function/Method',
    ast.Module: 'Module'
}


def parse_file(file_base, file_path, file_name):
    """Parse a python's files contents to extract API documentation."""
    src_path = os.path.join(file_base, file_path, file_name)

    print(src_path)

    with open(src_path) as fp:
        source = fp.read()
        tree = ast.parse(source)

        output_folder = "./docs/"
        dst_path = os.path.join(output_folder, file_path, file_name + ".md")

        os.makedirs(os.path.join(output_folder, file_path), exist_ok=True)

        with open(dst_path, "w") as output_file:

            class FuncLister(ast.NodeVisitor):
                def visit_FunctionDef(self, node):
                    """Function Visitor"""
                    output_file.write("#### " + node.name + "()")
                    output_file.write('\n')
                    doc_string = ast.get_docstring(node)
                    if doc_string:
                        output_file.write("`" + doc_string + "`")
                    else:
                        output_file.write("`No docstring found.`")
                    output_file.write('\n')
                    output_file.write('\n')
                    self.generic_visit(node)

                def visit_ClassDef(self, node):
                    """Class Visitor"""
                    if node.name.lower().strip() != "meta":
                        output_file.write('--------------------')
                        output_file.write('\n')
                    output_file.write("### " + node.name)
                    output_file.write('\n')
                    doc_string = ast.get_docstring(node)
                    if doc_string:
                        output_file.write("`" + doc_string + "`")
                    else:
                        output_file.write("`No docstring found.`")
                    output_file.write('\n')
                    output_file.write('\n')
                    self.generic_visit(node)

            FuncLister().visit(tree)


if __name__ == '__main__':
    # Parse a single file?
    pass
