from ast import *

# this file is only for development conveniences.
# its useless for the main program.

Module(
    body=[
        Import(
            names=[
                alias(name='ast')]),
        ImportFrom(
            module='ast',
            names=[
                alias(name='AST')],
            level=0),
        ImportFrom(
            module='sys',
            names=[
                alias(name='stderr')],
            level=0),
        ImportFrom(
            module='typing',
            names=[
                alias(name='TextIO')],
            level=0),
        FunctionDef(
            name='prerr',
            args=arguments(
                posonlyargs=[],
                args=[
                    arg(arg='msg')],
                kwonlyargs=[],
                kw_defaults=[],
                defaults=[]),
            body=[
                Expr(
                    value=Call(
                        func=Name(id='print', ctx=Load()),
                        args=[
                            Name(id='msg', ctx=Load())],
                        keywords=[
                            keyword(
                                arg='file',
                                value=Name(id='stderr', ctx=Load())),
                            keyword(
                                arg='end',
                                value=Constant(value=''))]))],
            decorator_list=[],
            returns=Constant(value=None),
            type_params=[]),
        FunctionDef(
            name='ast_hammer',
            args=arguments(
                posonlyargs=[],
                args=[
                    arg(
                        arg='node',
                        annotation=Name(id='AST', ctx=Load()))],
                kwonlyargs=[],
                kw_defaults=[],
                defaults=[]),
            body=[
                If(
                    test=Call(
                        func=Name(id='isinstance', ctx=Load()),
                        args=[
                            Name(id='node', ctx=Load()),
                            Name(id='AST', ctx=Load())],
                        keywords=[]),
                    body=[
                        Assign(
                            targets=[
                                Name(id='cls', ctx=Store())],
                            value=Call(
                                func=Name(id='type', ctx=Load()),
                                args=[
                                    Name(id='node', ctx=Load())],
                                keywords=[])),
                        Expr(
                            value=Call(
                                func=Name(id='prerr', ctx=Load()),
                                args=[
                                    JoinedStr(
                                        values=[
                                            Constant(value='('),
                                            FormattedValue(
                                                value=Attribute(
                                                    value=Name(id='cls', ctx=Load()),
                                                    attr='__name__',
                                                    ctx=Load()),
                                                conversion=-1),
                                            Constant(value='['),
                                            FormattedValue(
                                                value=Call(
                                                    func=Attribute(
                                                        value=Name(id='node', ctx=Load()),
                                                        attr='__str__',
                                                        ctx=Load()),
                                                    args=[],
                                                    keywords=[]),
                                                conversion=-1),
                                            Constant(value=']')])],
                                keywords=[])),
                        For(
                            target=Name(id='name', ctx=Store()),
                            iter=Attribute(
                                value=Name(id='node', ctx=Load()),
                                attr='_fields',
                                ctx=Load()),
                            body=[
                                Try(
                                    body=[
                                        Assign(
                                            targets=[
                                                Name(id='value', ctx=Store())],
                                            value=Call(
                                                func=Name(id='getattr', ctx=Load()),
                                                args=[
                                                    Name(id='node', ctx=Load()),
                                                    Name(id='name', ctx=Load())],
                                                keywords=[]))],
                                    handlers=[
                                        ExceptHandler(
                                            type=Name(id='AttributeError', ctx=Load()),
                                            body=[
                                                Continue()])],
                                    orelse=[],
                                    finalbody=[]),
                                Expr(
                                    value=Call(
                                        func=Name(id='ast_hammer', ctx=Load()),
                                        args=[
                                            Name(id='value', ctx=Load())],
                                        keywords=[]))],
                            orelse=[]),
                        If(
                            test=Attribute(
                                value=Name(id='node', ctx=Load()),
                                attr='_attributes',
                                ctx=Load()),
                            body=[
                                For(
                                    target=Name(id='name', ctx=Store()),
                                    iter=Attribute(
                                        value=Name(id='node', ctx=Load()),
                                        attr='_attributes',
                                        ctx=Load()),
                                    body=[
                                        Try(
                                            body=[
                                                Assign(
                                                    targets=[
                                                        Name(id='value', ctx=Store())],
                                                    value=Call(
                                                        func=Name(id='getattr', ctx=Load()),
                                                        args=[
                                                            Name(id='node', ctx=Load()),
                                                            Name(id='name', ctx=Load())],
                                                        keywords=[]))],
                                            handlers=[
                                                ExceptHandler(
                                                    type=Name(id='AttributeError', ctx=Load()),
                                                    body=[
                                                        Continue()])],
                                            orelse=[],
                                            finalbody=[]),
                                        If(
                                            test=BoolOp(
                                                op=And(),
                                                values=[
                                                    Compare(
                                                        left=Name(id='value', ctx=Load()),
                                                        ops=[
                                                            Is()],
                                                        comparators=[
                                                            Constant(value=None)]),
                                                    Compare(
                                                        left=Call(
                                                            func=Name(id='getattr', ctx=Load()),
                                                            args=[
                                                                Name(id='cls', ctx=Load()),
                                                                Name(id='name', ctx=Load()),
                                                                Constant(value=Ellipsis)],
                                                            keywords=[]),
                                                        ops=[
                                                            Is()],
                                                        comparators=[
                                                            Constant(value=None)])]),
                                            body=[
                                                Continue()],
                                            orelse=[]),
                                        Expr(
                                            value=Call(
                                                func=Name(id='ast_hammer', ctx=Load()),
                                                args=[
                                                    Name(id='value', ctx=Load())],
                                                keywords=[]))],
                                    orelse=[])],
                            orelse=[]),
                        Expr(
                            value=Call(
                                func=Name(id='prerr', ctx=Load()),
                                args=[
                                    Constant(value=')')],
                                keywords=[]))],
                    orelse=[
                        If(
                            test=Call(
                                func=Name(id='isinstance', ctx=Load()),
                                args=[
                                    Name(id='node', ctx=Load()),
                                    Name(id='list', ctx=Load())],
                                keywords=[]),
                            body=[
                                If(
                                    test=UnaryOp(
                                        op=Not(),
                                        operand=Name(id='node', ctx=Load())),
                                    body=[
                                        Expr(
                                            value=Call(
                                                func=Name(id='prerr', ctx=Load()),
                                                args=[
                                                    Constant(value='()')],
                                                keywords=[])),
                                        Return()],
                                    orelse=[]),
                                For(
                                    target=Name(id='node', ctx=Store()),
                                    iter=Name(id='node', ctx=Load()),
                                    body=[
                                        Expr(
                                            value=Call(
                                                func=Name(id='ast_hammer', ctx=Load()),
                                                args=[
                                                    Name(id='node', ctx=Load())],
                                                keywords=[]))],
                                    orelse=[])],
                            orelse=[])])],
            decorator_list=[],
            returns=Constant(value=None),
            type_params=[]),
        FunctionDef(
            name='entry',
            args=arguments(
                posonlyargs=[],
                args=[
                    arg(
                        arg='input_stream',
                        annotation=Name(id='TextIO', ctx=Load())),
                    arg(
                        arg='output_stream',
                        annotation=Name(id='TextIO', ctx=Load()))],
                kwonlyargs=[],
                kw_defaults=[],
                defaults=[]),
            body=[
                Expr(
                    value=Constant(value='Processes input data and writes to output stream.\n\n    Args:\n        input_stream: A readable stream for input python code.\n        output_stream: A writable stream for output python code.\n\n    Returns:\n        None\n    ')),
                Assign(
                    targets=[
                        Name(id='raw_text', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='input_stream', ctx=Load()),
                            attr='read',
                            ctx=Load()),
                        args=[],
                        keywords=[])),
                Try(
                    body=[
                        Assign(
                            targets=[
                                Name(id='orig_ast', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='ast', ctx=Load()),
                                    attr='parse',
                                    ctx=Load()),
                                args=[
                                    Name(id='raw_text', ctx=Load())],
                                keywords=[])),
                        Expr(
                            value=Call(
                                func=Name(id='print', ctx=Load()),
                                args=[
                                    Call(
                                        func=Attribute(
                                            value=Name(id='ast', ctx=Load()),
                                            attr='dump',
                                            ctx=Load()),
                                        args=[
                                            Name(id='orig_ast', ctx=Load())],
                                        keywords=[
                                            keyword(
                                                arg='indent',
                                                value=Constant(value=4))])],
                                keywords=[]))],
                    handlers=[
                        ExceptHandler(
                            type=Name(id='Exception', ctx=Load()),
                            name='e',
                            body=[
                                Expr(
                                    value=Call(
                                        func=Name(id='print', ctx=Load()),
                                        args=[
                                            JoinedStr(
                                                values=[
                                                    Constant(value='Got following error when processing input:\n'),
                                                    FormattedValue(
                                                        value=Name(id='e', ctx=Load()),
                                                        conversion=-1),
                                                    Constant(value='\noutput will be unchanged as input.')])],
                                        keywords=[
                                            keyword(
                                                arg='file',
                                                value=Name(id='stderr', ctx=Load()))])),
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='output_stream', ctx=Load()),
                                            attr='write',
                                            ctx=Load()),
                                        args=[
                                            Name(id='raw_text', ctx=Load())],
                                        keywords=[]))])],
                    orelse=[],
                    finalbody=[]),
                Expr(
                    value=Call(
                        func=Attribute(
                            value=Name(id='output_stream', ctx=Load()),
                            attr='write',
                            ctx=Load()),
                        args=[
                            Call(
                                func=Attribute(
                                    value=Name(id='ast', ctx=Load()),
                                    attr='unparse',
                                    ctx=Load()),
                                args=[
                                    Name(id='orig_ast', ctx=Load())],
                                keywords=[])],
                        keywords=[])),
                Expr(
                    value=Call(
                        func=Attribute(
                            value=Name(id='output_stream', ctx=Load()),
                            attr='write',
                            ctx=Load()),
                        args=[
                            Constant(value='\n')],
                        keywords=[]))],
            decorator_list=[],
            returns=Constant(value=None),
            type_params=[])],
    type_ignores=[])
