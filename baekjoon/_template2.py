import sys


def main():
    stdin = sys.stdin
    N = int(stdin.readline())


if __name__ == '__main__':
    main()


from util.result_check import get_output_with_stdin
import pytest


@pytest.mark.parametrize(('in_str', 'out_str'), [
    ('''
    '''.strip(),
     '1'),
])
def test_main(in_str, out_str):
    assert get_output_with_stdin(main, in_str) == out_str
