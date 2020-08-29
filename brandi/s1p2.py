import sys
from itertools import count
import copy

directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]


def make_water_time_table(N, M):
    W = [[None] * N for _ in range(N)]
    stack = [(0, 0)]
    W[0][0] = 0
    for step in count(1):
        new_stack = []
        if not stack:
            return W
        for r, c in stack:
            for dr, dc in directions:
                nr = r + dr
                nc = r + dc
                if M[nr][nc] != '0':
                    continue
                if W[nr][nc] is not None:
                    W[nr][nc] = step
                new_stack.append((nr, nc))
        stack = new_stack


def h_move(N, M, W, start):
    stack = [start]


def naive_solution(N, M):
    S = [[0] * N for _ in range(N)]

    stack = [(0, 0), (N-1, N-1), S]
    for step in count(0):
        new_stack = []
        # for w, p, s in stack:

    stack = new_stack


def solve(N, M):
    return -1
    W = make_water_time_table(N, M)
    solutions = h_move(N, M, W, (N-1, N-1))




def main():
    stdin = sys.stdin
    N = int(stdin.readline().strip())
    M = [stdin.readline().strip() for _ in range(N)]
    print(solve(N, M))


if __name__ == '__main__':
    main()


from util.result_check import get_output_with_stdin
import pytest


def test_main():
    in_str = '''
3
0 1 0
0 0 1
1 0 0
    '''.strip()
    out_str = '''
2
    '''.strip()
    assert get_output_with_stdin(main, in_str) == out_str


def test_main2():
    in_str = '''
4
0 0 0 0 
1 0 1 0 
0 0 0 0 
0 0 1 0 
    '''.strip()
    out_str = '''
1
    '''.strip()
    assert get_output_with_stdin(main, in_str) == out_str


def test_main3():
    in_str = '''
5
0 1 0 0 0 
0 0 1 1 0 
0 0 0 0 0 
0 0 0 0 0 
0 0 0 0 0 
    '''.strip()
    out_str = '''
4
    '''.strip()
    assert get_output_with_stdin(main, in_str) == out_str
