import sys
from itertools import combinations

# Right, Left, Bottom, Top ward
R, L, B, T = range(4)


def get_cross_size_grid(n, m, grid):
    """calculate maximum size of cross for each element in the grid"""
    grid = [[int(c == '#') for c in row] for row in grid]
    acc = [[[0] * 4 for _ in range(m)] for _ in range(n)]
    for i in range(n):
        acc[i][0][R] = grid[i][0]
        acc[i][-1][L] = grid[i][-1]
        for j in range(1, m):
            val = grid[i][j]
            acc[i][j][R] = acc[i][j-1][R] + val if val else 0
            val = grid[i][-j-1]
            acc[i][-j-1][L] = acc[i][-j][L] + val if val else 0
    for j in range(m):
        acc[0][j][B] = grid[0][j]
        acc[-1][j][T] = grid[-1][j]
        for i in range(1, n):
            val = grid[i][j]
            acc[i][j][B] = acc[i-1][j][B] + val if val else 0
            val = grid[-i-1][j]
            acc[-i-1][j][T] = acc[-i][j][T] + val if val else 0

    for i in range(n):
        for j in range(m):
            grid[i][j] = min(acc[i][j][R], acc[i][j][L], acc[i][j][B], acc[i][j][T])
    return grid


def normalize_pair(center1, center2):
    """normalize pair to the form (r, c, ss1, ss2)
    (r1, c1, s1), (r2, c2, s2)
      --> (0, 0, ss1), (r, c, ss2)  (where r <= c and ss1 >= ss2)
      pairs that have the same normalized value will make the same result by symmetry.
    """
    if center1[2] == 1 and center2[2] == 1:
        return 1, 1, 1, 1

    r1, c1, s1 = center1
    r2, c2, s2 = center2
    r = abs(r2 - r1)
    c = abs(c2 - c1)
    return min(r, c), max(r, c), max(s1, s2), min(s1, s2)


def iter_sizes(s1, s2):
    while s1 > 1 or s2 > 1:
        yield s1, s2
        if s1 == s2:
            s2 -= 1
        else:
            s1 -= 1


def calc_score(s1, s2):
    return (4 * (s1 - 1) + 1) * (4 * (s2 - 1) + 1)


def is_interfered(s1, s2, r, c):
    return r == 0 and c < s1 + s2 or r < s2 and c < s1


def solve(n, m, grid):
    grid = get_cross_size_grid(n, m, grid)
    centers = [(r, c, grid[r][c]) for r, row in enumerate(grid) for c, val in enumerate(row) if grid[r][c] > 0]

    # this line is hot-spot, it takes 93% of time.
    # can we improve this lines?
    pairs = {normalize_pair(center1, center2) for center1, center2 in combinations(centers, 2)}

    pairs = sorted([(calc_score(s1, s2), r, c, s1, s2) for r, c, s1, s2 in pairs], reverse=True)
    max_score = 1
    for score_limit, r, c, s1, s2 in pairs:
        if score_limit < max_score:
            break
        for ss1, ss2 in iter_sizes(s1, s2):
            score = calc_score(ss1, ss2)
            if score < max_score:
                break
            if not is_interfered(ss1, ss2, r, c):
                max_score = max(max_score, score)
                break
    return max_score


def main():
    stdin = sys.stdin
    n, m = [int(x) for x in stdin.readline().split()]
    grid = [stdin.readline().strip() for _ in range(n)]
    print(solve(n, m, grid))


if __name__ == "__main__":
    main()


import random
import pytest
from util import *


def test_time():
    ratio = 0.9
    n, m = 15, 15
    random.seed(2)
    grid = [['#' if random.random() < ratio else '.' for _ in range(m)] for _ in range(n)]
    timeit_lp(solve, (n, m, grid), time_limit=1)  # , log=True, omit_func_args=True)


# @pytest.mark.skip
def test_compare():
    def gen_prob():
        ratio = 0.6
        n, m = 10, 10
        grid = [['#' if random.random() < ratio else '.' for _ in range(m)] for _ in range(n)]
        return merge_to_lines([
            list_to_string([n, m]),
            '\n'.join(''.join(row) for row in grid),
        ])
    # eprint(gen_prob())
    compare_func_results(mock_io(main), ext_binary_to_func('p17085'), generate_probs(gen_prob, count=100))


def test_main():
    in_str = """
5 6
######
#...#.
######
##..#.
######
    """.strip()
    out_str = '5'
    assert mock_io(main)(in_str) == out_str


def test_main2():
    in_str = """
6 6
.#..#.
######
.#..#.
######
.#..#.
.#..#.
    """.strip()
    out_str = '25'
    assert mock_io(main)(in_str) == out_str


def test_found():
    in_str = """
5 5
.##.#
..###
#####
#.###
##.##
    """.strip()
    out_str = '5'
    assert mock_io(main)(in_str) == out_str
