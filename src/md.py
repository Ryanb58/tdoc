import ast


def get_function_markdown(node):
    """Parse a function node."""
    output = ""
    output += "#### " + node.name + "("
    if len(node.args.args) > 0:
        output += ", ".join(
            str(x.arg) for x in node.args.args)
    output += ')'
    output += '\n'
    output += '\n'

    doc_string = ast.get_docstring(node)
    if doc_string:
        output += "> " + doc_string + ""
    else:
        output += "> No docstring found."
    output += '\n'
    output += '\n'

    return output


def get_class_markdown(node):
    """Parse a class node."""
    output = ""
    if node.name.lower().strip() != "meta":
        output += '--------------------'
        output += '\n'
    output += "## " + node.name
    output += '\n'
    doc_string = ast.get_docstring(node)
    if doc_string:
        output += "" + doc_string + ""
    output += '\n'
    output += '\n'

    return output
