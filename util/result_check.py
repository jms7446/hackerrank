from unittest.mock import patch
from io import StringIO
import time
import sys

MAX_LOOP = 10 ** 8


def to_time_str(sec):
    if sec >= 60:
        return '{:.2f}m'.format(sec / 60)
    elif sec >= 1:
        return '{:.2f}s'.format(sec)
    elif sec >= 1e-3:
        return '{:.2f}ms'.format(sec * 1e3)
    elif sec >= 1e-6:
        return '{:.2f}µs'.format(sec * 1e6)
    else:
        return '{:.2f}ns'.format(sec * 1e9)


def _print_avg_time(elapse_time, num_iter):
    avg_time = elapse_time / num_iter
    print('\n==> avg time: {} in {} iterations'.format(to_time_str(avg_time), num_iter), file=sys.stderr, end='')


def check_elapse_time(func, args, expected=None, num_iter=1):
    st = time.time()
    if expected:
        for _ in range(num_iter):
            assert func(*args) == expected
    else:
        for _ in range(num_iter):
            func(*args)
    elapse_time = time.time() - st
    _print_avg_time(elapse_time, num_iter)


def get_output_with_stdin(func, inputs, num_iter=1, check_time=False):
    st = time.time()
    for _ in range(num_iter):
        with patch("sys.stdin", StringIO(inputs)), patch("sys.stdout", new_callable=StringIO) as mocked_out:
            func()
    elapse_time = time.time() - st
    if check_time:
        _print_avg_time(elapse_time, num_iter)
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
    elapse_time = time.time() - st
    print(f"elapse time: {elapse_time}", file=sys.stderr)
