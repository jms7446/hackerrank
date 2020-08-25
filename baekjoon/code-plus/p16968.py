import sys
from functools import reduce
from operator import mul


cnt_map = {
    'c': 26,
    'd': 10,
}


def solve(ptn):
    if not ptn:
        return 1
    cases = (cnt_map[cur] if pre != cur else cnt_map[cur] - 1
             for pre, cur in zip('.' + ptn, ptn))
    return reduce(mul, cases)


def main():
    stdin = sys.stdin
    ptn = stdin.readline().strip()
    print(solve(ptn))


if __name__ == '__main__':
    main()


from util.result_check import get_output_with_stdin
import pytest


@pytest.mark.parametrize(('in_str', 'out_str'), [
    ('dd', '90'),
    ('cc', '650'),
    ('dcdd', '23400'),
    ('', '1')
])
def test_main(in_str, out_str):
    assert get_output_with_stdin(main, in_str) == out_str
