from unittest.mock import patch
from io import StringIO


def get_output_with_stdin(func, inputs):

    with patch("sys.stdin", StringIO(inputs)), patch("sys.stdout", new_callable=StringIO) as mocked_out:
        func()
    return mocked_out.getvalue()
