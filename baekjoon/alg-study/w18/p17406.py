import sys
from copy import deepcopy

INF = 10**8


def h_shift(A, B, r, c, s, shift):
    for i in range(c, c + s):
        B[r][i+shift] = A[r][i]


def v_shift(A, B, r, c, s, shift):
    for i in range(r, r + s):
        B[i+shift][c] = A[i][c]


def rotate(A, rotation):
    # FIXME most of time is spent here.
    B = deepcopy(A)
    r, c, s = rotation
    for ss in range(1, s + 1):
        h_shift(A, B, r - ss,   c - ss,   ss * 2,  1)       # top
        v_shift(A, B, r - ss,   c + ss,   ss * 2,  1)       # right
        h_shift(A, B, r + ss,   c - ss+1, ss * 2, -1)       # bottom
        v_shift(A, B, r - ss+1, c - ss,   ss * 2, -1)       # left
    return B


def find_min(A, rotations):
    if not rotations:
        return min(sum(row) for row in A)

    min_value = INF
    for idx, rotation in enumerate(rotations):
        B = rotate(A, rotation)
        min_value = min(min_value, find_min(B, rotations[:idx] + rotations[idx+1:]))
    return min_value


# test_time : 3.25ms
def solve(A, raw_rotations):
    raw_rotations = [(r - 1, c - 1, s) for (r, c, s) in raw_rotations]      # convert to 0-start index
    return find_min(A, raw_rotations)


def main():
    stdin = sys.stdin
    N, M, K = [int(x) for x in stdin.readline().split()]
    A = [[int(x) for x in stdin.readline().split()] for _ in range(N)]
    rotations = [[int(x) for x in stdin.readline().split()] for _ in range(K)]
    print(solve(A, rotations))


if __name__ == "__main__":
    main()


from util import *
from random import randint
import pytest


def test_h_shift():
    A = [[1, 2, 3], [4, 5, 6]]
    B = [[1, 2, 3], [4, 5, 6]]
    h_shift(A, B, 0, 0, 2, 1)
    assert B == [[1, 1, 2], [4, 5, 6]]


def test_v_shift():
    A = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    B = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    v_shift(A, B, 0, 0, 2, 1)
    assert B == [[1, 2, 3], [1, 5, 6], [4, 8, 9]]


def test_main():
    in_str = """
5 6 2
1 2 3 2 5 6
3 8 7 2 1 3
8 2 3 1 4 5
3 4 5 1 1 1
9 3 2 1 4 3
3 4 2
4 2 1
    """.strip()
    out_str = """
12
    """.strip()
    assert mock_io(main)(in_str) == out_str


def test_generated1():
    in_str = """
4 4 2
8 7 2 3
1 5 8 6
6 7 6 9
1 3 8 1
2 2 1
3 2 1
    """.strip()
    out_str = """
10
    """.strip()
    assert mock_io(main)(in_str) == out_str


def test_generated2():
    in_str = """
3 4 2
3 6 7 4
1 9 2 8
5 6 8 1
2 3 1
2 2 1
    """.strip()
    out_str = """
17
    """.strip()
    assert mock_io(main)(in_str) == out_str


def test_generated3():
    in_str = """
3 14 3
9 1 8 6 8 5 3 6 6 8 8 8 5 6
5 9 4 2 2 9 5 8 9 8 9 9 5 2
7 8 7 8 1 7 2 8 9 9 9 8 7 8
2 9 1
2 13 1
2 9 1
    """.strip()
    out_str = """
88
    """.strip()
    assert mock_io(main)(in_str) == out_str


def make_prob(rN=50, rM=50, rK=6):
    N, M = randint(3, rN), randint(3, rM)
    K = randint(1, rK)
    # N, M, K = 3, 4, 3

    xs = [[randint(1, 9) for _ in range(M)] for _ in range(N)]
    ys = []
    for _ in range(K):
        s = randint(1, (min(N, M) - 1) // 2)
        r = randint(s, N - 1 - s) + 1
        c = randint(s, M - 1 - s) + 1
        ys.append((r, c, s))
    prob = merge_to_lines([
        list_to_string([N, M, K]),
        merge_to_lines(xs),
        merge_to_lines(ys),
    ])
    return prob


def test_time():
    generator = generate_probs(make_prob, count=5)
    timeits(mock_io(main), generator)


def test_profile():
    timeit_lp(mock_io(main), make_prob(), funcs=[solve, find_min, rotate], log=False)


@pytest.mark.skip
def test_compare():
    generator = generate_probs(make_prob, count=10)
    compare_func_results(ext_binary_to_func('p17406'), mock_io(main), generator)
