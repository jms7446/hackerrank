import sys
from _collections import namedtuple


'''
Hold
'''


def solve(X, N):
    hs = [[0] * N for _ in range(N)]
    vs = [[0] * N for _ in range(N)]
    ds = [[0] * N for _ in range(N)]

    for c in range(N):
        if X[0][c] == 1:
            break
        hs[0][c] = 1

    for r in range(1, N):
        for c in range(2, N):
            if X[r][c]:
                continue
            hs[r][c] = hs[r][c-1]

    return 0


def main():
    stdin = sys.stdin
    N = int(stdin.readline())
    X = [[int(x) for x in stdin.readline().split()] for _ in range(N)]
    print(solve(X, N))


if __name__ == '__main__':
    main()


from util.result_check import get_output_with_stdin
import pytest


@pytest.mark.parametrize(('in_str', 'out_str'), [
    ('''
3
0 0 0
0 0 0
0 0 0
    '''.strip(),
     '1'),
    ('''
4
0 0 0 0
0 0 0 0
0 0 0 0
0 0 0 0
    '''.strip(),
     '3'),
    ('''
5
0 0 1 0 0
0 0 0 0 0
0 0 0 0 0
0 0 0 0 0
0 0 0 0 0
    '''.strip(),
     '0'),
    ('''
6
0 0 0 0 0 0
0 1 0 0 0 0
0 0 0 0 0 0
0 0 0 0 0 0
0 0 0 0 0 0
0 0 0 0 0 0
    '''.strip(),
     '13'),
])
def test_main(in_str, out_str):
    assert get_output_with_stdin(main, in_str) == out_str
