import sys
import os

import pytest

from util.result_check import *


def main_correct():
    stdin = sys.stdin
    return stdin.readline().strip() + ' processed'


def main_incorrect():
    stdin = sys.stdin
    return stdin.readline() + ' what?'


def test_evaluate_via_stdin():
    in_str = 'a'
    assert evaluate_via_io(main_correct, in_str) == 'a processed'


def test_compare_func_result():
    def func1(s):
        return s + '1'

    def func2(s):
        return s + '2'

    compare_func_result(func1, func1, 'a')
    with pytest.raises(Exception):
        compare_func_result(func1, func2, 'a')


def test_ext_binary_to_func():
    binary_dir = os.path.abspath(os.path.dirname(__file__))
    binary_path = 'ext_sample.py'
    func = ext_binary_to_func(binary_path, binary_dir)
    assert func('hi') == 'hi processed'
