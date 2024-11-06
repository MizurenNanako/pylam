import ast
from ast import AST
from sys import stderr
from typing import TextIO


def prerr(msg) -> None:
    print(msg, file=stderr, end='')


def hammer_statement(stmt: AST) -> None:
    match stmt:
        case ast.FunctionDef(name=fname, args=ast.arguments(
                posonlyargs=[],
                args=args,
                kwonlyargs=[],
                kw_defaults=[],
                defaults=[])
        ):
            args = [arg.arg for arg in args]
            print(f'[FunctionDef recognized] {fname}({', '.join(args)})')
        case _:
            print(f'[{type(stmt).__name__}] leave unchanged.')


def ast_hammer(node: AST) -> None:
    match node:
        case ast.Module(body=body, type_ignores=_):
            # print('module')
            for stmt in body:
                hammer_statement(stmt)
        case _:
            print(f'[unknown node:] {node}')


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
        # print(ast.dump(orig_ast, indent=4))
        ast_hammer(orig_ast)
    except Exception as e:
        print(f'Got following error when processing input:\n'
              f'{e}\noutput will be unchanged as input.',
              file=stderr)
        output_stream.write(raw_text)
    output_stream.write(ast.unparse(orig_ast))
    output_stream.write('\n')
