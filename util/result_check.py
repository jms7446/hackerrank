from unittest.mock import patch
from io import StringIO
import time
import os
import subprocess
from typing import List, Callable, Iterable

from util.tools import eprint

MAX_LOOP = 10 ** 8
BINARY_DIR_BASE = os.path.join(os.path.dirname(os.path.abspath(__file__)), '../ext_code')


def evaluate_via_io(func, in_str):
    return _evaluate(func, in_str, io_mock=True)


def timeit(func, func_args, num_iter=100, time_limit=0.1, io_mock=False):
    """execute func num_iter times and print elapse time info to stderr"""
    elapse_times = _calc_elapse_times(func, func_args, num_iter=num_iter, time_limit=time_limit, io_mock=io_mock)
    _print_elapse_time(elapse_times)


def timeits(func, func_args_list, num_iter=100, time_limit_per_args=0.1, io_mock=False):
    """execute func for func_args_list and print elapse time info to stderr"""
    elapse_times = []
    for func_args in func_args_list:
        e_times = _calc_elapse_times(func, func_args, num_iter=num_iter, time_limit=time_limit_per_args,
                                     io_mock=io_mock)
        elapse_times.extend(e_times)
    _print_elapse_time(elapse_times)


def time_complexity(func: Callable, args_func: Callable, scales: Iterable, num_iter=10, time_limit=1, io_mock=False):
    elapse_times = []
    for scale in scales:
        args = args_func(scale)
        cur_elapse_times = _calc_elapse_times(func, args, num_iter=num_iter, time_limit=time_limit, io_mock=io_mock)
        avg_time = sum(cur_elapse_times) / len(cur_elapse_times)
        elapse_times.append(avg_time)
    return {'scale': scales, 'elapse_time': elapse_times}


def compare_func_result(func1, func2, args, silence=False):
    try:
        res1 = _evaluate(func1, args)
    except Exception as ex:
        res1 = '<<<<<<<<<<< Error1({}) >>>>>>>>>>>>>>>'.format(ex)
    try:
        res2 = _evaluate(func2, args)
    except Exception as ex:
        res2 = '<<<<<<<<<<< Error2({}) >>>>>>>>>>>>>>>'.format(ex)

    if res1 != res2:
        if not silence:
            lines = [
                '=================== in_str   ==================',
                args,
                '=================== expected ==================',
                res1,
                '=================== actual   ==================',
                res2,
                '===============================================',
            ]
            eprint('\n'.join(lines))
        raise Exception("Match Failed")


def compare_func_results(func1, func2, args_iter, silence=False):
    for args in args_iter:
        compare_func_result(func1, func2, args, silence=silence)


def ext_binary_to_func(binary_path, binary_dir=BINARY_DIR_BASE) -> Callable:
    def func(in_str):
        res = subprocess.check_output(binary_path, input=in_str.encode())
        return res.decode().strip()

    binary_path = os.path.join(binary_dir, binary_path)
    return func


################################################################################
################################################################################

def _evaluate(func, func_args, io_mock=False):
    """evaluate func with func_args, to use io_mock easily"""
    if io_mock:
        in_str = func_args if isinstance(func_args, str) else func_args[0]
        with patch("sys.stdin", StringIO(in_str)), patch("sys.stdout", new_callable=StringIO) as mocked_out:
            func()
        return mocked_out.getvalue().strip()
    else:
        return func(*func_args)


def _calc_elapse_times(func, func_args, num_iter=1, time_limit=None, io_mock=False) -> List[float]:
    """execute func and return elapse times (and print out to stderr)"""
    elapse_times = []
    total_time = 0
    for _ in range(num_iter):
        st = time.time()
        _evaluate(func, func_args, io_mock=io_mock)
        elapse_time = time.time() - st
        elapse_times.append(elapse_time)
        total_time += elapse_time
        if time_limit and total_time > time_limit:
            break
    return elapse_times


def _to_time_str(sec):
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


def _print_elapse_time(elapse_times):
    avg_time = sum(elapse_times) / len(elapse_times)
    eprint('\n==> avg time: {} in {} iterations'.format(_to_time_str(avg_time), len(elapse_times)))
