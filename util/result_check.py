from unittest.mock import patch
from io import StringIO
import time
import datetime
import os
import subprocess
from typing import List, Callable, Iterable

from deprecation import deprecated
from line_profiler import LineProfiler

from util.tools import eprint, get_caller_filename
from util.prob_generate import list_to_string, merge_to_lines

MAX_LOOP = 10 ** 8
BINARY_DIR_BASE = os.path.join(os.path.dirname(os.path.abspath(__file__)), '../ext_code')


def logging_profile_info(msg_list, log_file_name):
    out_lines = '\n' + '#' * 120 + '\n'
    in_lines = '\n' + '-' * 120 + '\n'

    cur_time_str = str(datetime.datetime.now())
    core_msg = in_lines.join([f'{name}: \n{msg}' for name, msg in msg_list])
    total_msg = out_lines.join(['', cur_time_str, core_msg, ''])
    with open(log_file_name, 'a') as f:
        f.write(total_msg)
        eprint(f'Profile is saved in {log_file_name} (appended)')


def timeit_lp(func, func_args, funcs=None, num_iter=100, time_limit=0.1, log=False,
              silence=False, log_file_name=None, changed='', omit_func_args=False):
    """execute timeit and line profiling

    :param func:
    :param func_args:
    :param funcs:
    :param num_iter:
    :param time_limit:
    :param silence: Dot not display stats by stderr
    :param log: additionally logging stats into log_file
    :param log_file_name: if log_file_name is not given, default value is caller's `filename.lprof`
    :param changed:
    :param omit_func_args:
    """
    timeit_msg = timeit(func, func_args, num_iter=num_iter, time_limit=time_limit, return_msg=True, silence=silence)
    lp_msg = lprun(func, func_args, funcs=funcs, return_msg=True, silence=silence)
    if log:
        log_file_name = log_file_name or get_caller_filename() + '.lprof'
        logging_profile_info([
            ('changed', changed),
            ('args', repr(func_args) if not omit_func_args else ''),
            ('timeit', timeit_msg),
            ('line_profiler', lp_msg),
        ], log_file_name)


def lprun(func, args, funcs=None, silence=False, return_msg=False):
    funcs = funcs or []
    if isinstance(args, str) or not isinstance(args, Iterable):
        args = (args, )

    lp = LineProfiler()
    for f in funcs:
        lp.add_function(f)
    lp_wrapper = lp(func)
    lp_wrapper(*args)

    output = StringIO()
    lp.print_stats(stream=output)
    msg = output.getvalue()
    if not silence:
        eprint(msg)
    if return_msg:
        return msg


def timeit(func, func_args, num_iter=100, time_limit=0.1, silence=False, return_msg=False):
    elapse_times = _calc_elapse_times(func, func_args, num_iter=num_iter, time_limit=time_limit)
    msg = make_elapse_time_msg(elapse_times)
    if not silence:
        eprint(msg)
    if return_msg:
        return msg


def timeits(func, func_args_list, num_iter=100, time_limit_per_args=0.1, silence=False, return_msg=False):
    elapse_times = []
    for func_args in func_args_list:
        e_times = _calc_elapse_times(func, func_args, num_iter=num_iter, time_limit=time_limit_per_args)
        elapse_times.extend(e_times)
    msg = make_elapse_time_msg(elapse_times)
    if not silence:
        eprint(msg)
    if return_msg:
        return msg


def time_complexity(func: Callable, args_func: Callable, scales: Iterable, num_iter=10, time_limit=1):
    elapse_times = []
    for scale in scales:
        args = args_func(scale)
        cur_elapse_times = _calc_elapse_times(func, args, num_iter=num_iter, time_limit=time_limit)
        avg_time = sum(cur_elapse_times) / len(cur_elapse_times)
        elapse_times.append(avg_time)
    return {'scale': scales, 'elapse_time': elapse_times}


def compare_func_result(func1, func2, args, silence=False):
    try:
        res1 = func1(*args)
    except Exception as ex:
        res1 = '<<<<<<<<<<< Error1({}) >>>>>>>>>>>>>>>'.format(ex)
    try:
        res2 = func2(*args)
    except Exception as ex:
        res2 = '<<<<<<<<<<< Error2({}) >>>>>>>>>>>>>>>'.format(ex)

    if res1 != res2:
        if not silence:
            lines = [
                '=================== in_str   ==================',
                list_to_string(args),
                '=================== func1 ==================',
                res1,
                '=================== func2   ==================',
                res2,
                '===============================================',
            ]
            eprint(merge_to_lines(lines))
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


def mock_io(func):
    def mocked_func(stdin_str):
        with patch("sys.stdin", StringIO(stdin_str)), patch("sys.stdout", new_callable=StringIO) as mocked_out:
            func()
        return mocked_out.getvalue().strip()
    return mocked_func


@deprecated(details='use mock_io')
def io_mock(func):
    return mock_io(func)


@deprecated('Use io_mock instead')
def evaluate_via_io(func, in_str):
    return _evaluate(func, in_str, io_mock=True)


################################################################################
################################################################################


@deprecated(details='Use io_mock instead')
def _evaluate(func, func_args, io_mock=False):
    """evaluate func with func_args, to use io_mock easily"""
    if io_mock:
        in_str = func_args if isinstance(func_args, str) else func_args[0]
        with patch("sys.stdin", StringIO(in_str)), patch("sys.stdout", new_callable=StringIO) as mocked_out:
            func()
        return mocked_out.getvalue().strip()
    else:
        return func(*func_args)


def _calc_elapse_times(func, func_args, num_iter=1, time_limit=None) -> List[float]:
    """execute func and return elapse times (and print out to stderr)"""
    elapse_times = []
    if isinstance(func_args, str) or not isinstance(func_args, Iterable):
        func_args = (func_args, )
    total_time = 0
    for _ in range(num_iter):
        st = time.time()
        func(*func_args)
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


def make_elapse_time_msg(elapse_times):
    avg_time = sum(elapse_times) / len(elapse_times)
    msg = '==> avg_time: {} in {} iterations'.format(_to_time_str(avg_time), len(elapse_times))
    return msg
