import sys
from itertools import count


def solve(N, xs):
    if N == 1:
        return 0

    visited = [False] * N
    stack = [0]
    visited[0] = True
    for step in count(1):
        if not stack:
            return -1
        new_stack = []
        for idx in stack:
            jump = xs[idx]
            for s in range(-jump, jump + 1):
                next_idx = idx + s
                if next_idx == N - 1:
                    return step
                if not (0 <= next_idx < N) or visited[next_idx]:
                    continue
                visited[next_idx] = True
                new_stack.append(next_idx)
        stack = new_stack


def main():
    stdin = sys.stdin
    N = int(stdin.readline())
    G = [int(x) for x in stdin.readline().split()]
    print(solve(N, G))


if __name__ == "__main__":
    main()

from util import *
import pytest


@pytest.mark.parametrize(('in_str', 'out_str'), [
    ('''
10
1 2 0 1 3 2 1 5 4 2
        '''.strip(),
     '''
5
     '''.strip()),
    ('''
1
1
    '''.strip(),
     '''
0
     '''.strip()),
])
def test_main(in_str, out_str):
    assert mock_io(main)(in_str) == out_str
