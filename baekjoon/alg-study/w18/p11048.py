import sys


def solve(N, M, G):
    # why M + 1 : trick to avoid i >= 0 condition, keep pre_scores[-1] = 0
    pre_scores = [0] * (M + 1)
    cur_scores = [0] * (M + 1)
    for r in range(N):
        for c in range(M):
            score = max(pre_scores[c], pre_scores[c-1], cur_scores[c-1])
            cur_scores[c] = score + G[r][c]
        cur_scores, pre_scores = pre_scores, cur_scores
    return pre_scores[M-1]


def main():
    stdin = sys.stdin
    N, M = [int(x) for x in stdin.readline().split()]
    G = [[int(x) for x in stdin.readline().split()] for _ in range(N)]
    print(solve(N, M, G))


if __name__ == "__main__":
    main()

from util import *
import pytest


@pytest.mark.parametrize(('in_str', 'out_str'), [
    ('''
3 4
1 2 3 4
0 0 0 5
9 8 7 6
    '''.strip(),
     '''
31
     '''.strip()),
    ('''
3 3
1 0 0
0 1 0
0 0 1
    '''.strip(),
     '''
3
     '''.strip()),
    ('''
4 3
1 2 3
6 5 4
7 8 9
12 11 10
    '''.strip(),
     '''
47
     '''.strip()),
])
def test_main(in_str, out_str):
    assert mock_io(main)(in_str) == out_str
