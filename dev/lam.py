import ast
from ast import AST
from sys import stderr
from typing import TextIO


def prerr(msg) -> None:
    print(msg, file=stderr, end='')


def ast_hammer(node: AST) -> None:
    if isinstance(node, AST):
        cls = type(node)
        prerr(f'({cls.__name__}[{node.__str__()}]')
        for name in node._fields:
            try:
                value = getattr(node, name)
            except AttributeError:
                continue
            ast_hammer(value)
        if node._attributes:
            for name in node._attributes:
                try:
                    value = getattr(node, name)
                except AttributeError:
                    continue
                if value is None and getattr(cls, name, ...) is None:
                    continue
                ast_hammer(value)
        prerr(')')
    elif isinstance(node, list):
        if not node:
            prerr('()')
            return
        for node in node:
            ast_hammer(node)


def entry(input_stream: TextIO, output_stream: TextIO) -> None:
    """Processes input data and writes to output stream.

    Args:
        input_stream: A readable stream for input python code.
        output_stream: A writable stream for output python code.

    Returns:
        None
    """
    raw_text = input_stream.read()
    try:
        orig_ast = ast.parse(raw_text)
        print(ast.dump(orig_ast, indent=4))
        # ast_hammer(orig_ast)
    except Exception as e:
        print(f'Got following error when processing input:\n'
              f'{e}\noutput will be unchanged as input.',
              file=stderr)
        output_stream.write(raw_text)
    output_stream.write(ast.unparse(orig_ast))
    output_stream.write('\n')
