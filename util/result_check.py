from unittest.mock import patch
from io import StringIO
import time

MAX_LOOP = 10 ** 8


def get_output_with_stdin(func, inputs):
    with patch("sys.stdin", StringIO(inputs)), patch("sys.stdout", new_callable=StringIO) as mocked_out:
        func()
    return mocked_out.getvalue().strip()


def iter_run(func, loop=1, time_limit=None, gen=None):
    if time_limit is not None:
        loop = MAX_LOOP

    st = time.time()
    for _ in range(loop):
        if time_limit and time.time() - st >= time_limit:
            break
        if gen is not None:
            func(*gen())
        else:
            func()
