import ast
from typing import TextIO


def entry(input_stream: TextIO, output_stream: TextIO) -> None:
    """Processes input data and writes to output stream.

    Args:
        input_stream: A readable stream for input python code.
        output_stream: A writable stream for output python code.

    Returns:
        None
    """
    output_stream.write(input_stream.read())
