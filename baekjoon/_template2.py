import sys


def main():
    stdin = sys.stdin
    N = int(stdin.readline())


if __name__ == '__main__':
    main()


from util import *
import pytest


@pytest.mark.parametrize(('in_str', 'out_str'), [
    ('''
    '''.strip(),
     '1'),
])
def test_main(in_str, out_str):
    assert evaluate_via_io(main, in_str) == out_str
