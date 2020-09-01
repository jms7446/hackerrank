from unittest.mock import patch
from io import StringIO
import time
import sys
import os

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


def batch(func, arg_list, expected=None):
    if expected:
        for arg in arg_list:
            assert func(*arg) == expected
    else:
        for arg in arg_list:
            func(*arg)


def check_elapse_time(func, args=None, args_list=None, expected=None, num_iter=1):
    if args_list is None:
        args_list = [args]
    st = time.time()
    for _ in range(num_iter):
        batch(func, args_list, expected)
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


def find_edge_case_by_external_program(binary_path, func, in_strs, binary_dir=None):
    import subprocess
    binary_dir = binary_dir or os.path.join(os.path.dirname(os.path.abspath(__file__)), '../ext_code')
    binary_path = os.path.join(binary_dir, binary_path)
    for in_str in in_strs:
        try:
            expected = subprocess.check_output(binary_path, input=in_str.encode()).decode().strip()
        except Exception as ex:
            expected = '<<<<<<<<<<< Error({}) >>>>>>>>>>>>>>>'.format(ex)
        try:
            actual = get_output_with_stdin(func, in_str).strip()
        except Exception as ex:
            actual = '<<<<<<<<<<< Error({}) >>>>>>>>>>>>>>>'.format(ex)

        if expected != actual:
            print('', file=sys.stderr)
            print('=================== in_str   ==================', file=sys.stderr)
            print(in_str, file=sys.stderr)
            print('=================== expected ==================', file=sys.stderr)
            print(expected, file=sys.stderr)
            print('=================== actual   ==================', file=sys.stderr)
            print(actual, file=sys.stderr)
            print('===============================================', file=sys.stderr)
            raise Exception("Match Failed")


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


def eprint(*args, **kwargs):
    print(file=sys.stderr)
    print(*args, **kwargs, end='', file=sys.stderr)
