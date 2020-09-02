import sys
from itertools import chain


def solve(N, K, s):
    left = K
    stack = []
    i = 0
    for i, c in enumerate(s):
        while left > 0 and stack and stack[-1] < c:
            stack.pop()
            left -= 1
        if left == 0:
            break
        stack.append(c)
    return ''.join(chain(stack, s[i:]))[:N-K]


def main():
    stdin = sys.stdin
    N, K = [int(x) for x in stdin.readline().split()]
    s = stdin.readline().strip()
    print(solve(N, K, s))


if __name__ == "__main__":
    main()

from util import *


def test_main():
    in_str = """
4 2
1924
    """.strip()
    assert evaluate_via_io(main, in_str) == '94'


def test_add():
    in_str = """
10 5
1348182933
    """.strip()
    assert evaluate_via_io(main, in_str) == '88933'


def test_add2():
    in_str = """
6 3
999999
    """.strip()
    assert evaluate_via_io(main, in_str) == '999'


def test_error():
    in_str = """
2 1
12
    """.strip()
    assert evaluate_via_io(main, in_str) == '2'
