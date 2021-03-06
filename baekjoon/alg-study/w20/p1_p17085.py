
################################################################################
# from util
################################################################################

from typing import Sequence, Callable, TypeVar, Iterator, Tuple

U = TypeVar('U')


def combination2_with_pruning(items: Sequence[U], condition: Callable[[U, U], bool]) -> Iterator[Tuple[U, U]]:
    """generate combination(items) with pruning

    note.
      1. items must be sorted by caller appropriately.
      2. condition(item1, item1) must have valid meaning.
    """
    for i in range(len(items) - 1):
        item1 = items[i]
        if not condition(item1, item1):
            break
        for j in range(i + 1, len(items)):
            item2 = items[j]
            if not condition(item1, item2):
                break
            yield item1, item2


################################################################################


import sys
from operator import itemgetter, attrgetter
from dataclasses import dataclass


# Right, Left, Bottom, Top
R, L, B, T = range(4)


@dataclass(frozen=True)
class Center:
    row: int
    col: int
    size: int


def get_cross_size_grid(n, m, grid):
    """calculate maximum size of cross for each element in the grid. time & space complexity is O(nm)

    first, calculate continuous '#' count for each 4-direction respectively.
    Then, take min for each grid element.
    Verbose, but straight forward.
    """
    grid = [[int(c == '#') for c in row] for row in grid]
    acc = [[[0] * 4 for _ in range(m)] for _ in range(n)]
    for i in range(n):
        acc[i][0][L] = grid[i][0]
        acc[i][-1][R] = grid[i][-1]
        for j in range(1, m):
            val = grid[i][j]
            acc[i][j][L] = acc[i][j-1][L] + val if val else 0
            val = grid[i][-j-1]
            acc[i][-j-1][R] = acc[i][-j][R] + val if val else 0
    for j in range(m):
        acc[0][j][T] = grid[0][j]
        acc[-1][j][B] = grid[-1][j]
        for i in range(1, n):
            val = grid[i][j]
            acc[i][j][T] = acc[i-1][j][T] + val if val else 0
            val = grid[-i-1][j]
            acc[-i-1][j][B] = acc[-i][j][B] + val if val else 0

    for i in range(n):
        for j in range(m):
            grid[i][j] = min(acc[i][j])
    return grid


def calc_score_with_adjusting_size(center1: Center, center2: Center):
    def normalize_pair(center1, center2):
        """normalize pair to the form (r, c, ss1, ss2)
        (r1, c1, s1), (r2, c2, s2)
          --> (0, 0, ss1), (r, c, ss2)  (where r <= c and ss1 >= ss2)
          pairs that have the same normalized value will make the same result by symmetry.
        """
        row = abs(center2.row - center1.row)
        col = abs(center2.col - center1.col)
        if row > col:
            row, col = col, row
        return row, col, center1.size, center2.size

    def iter_sizes(s1, s2):
        while s1 > 1 or s2 > 1:
            yield s1, s2
            if s1 == s2:
                s2 -= 1
            else:
                s1 -= 1

    def is_interfered(r, c, s1, s2):
        """
           #                 #   #
           #     #           #  #O#
        ###O### #O#       ###O######
           #     #           #
           #
        """
        return r == 0 and c < s1 + s2 or r < s2 and c < s1

    row, col, size1, size2 = normalize_pair(center1, center2)
    for s1, s2 in iter_sizes(size1, size2):
        if not is_interfered(row, col, s1, s2):
            return calc_score(s1, s2)
    return 0


def calc_score(s1, s2):
    return (4 * (s1 - 1) + 1) * (4 * (s2 - 1) + 1)


def solve(n, m, grid):
    grid = get_cross_size_grid(n, m, grid)
    eprint(merge_to_lines(grid), '')

    max_score = 1
    centers = [Center(r, c, grid[r][c]) for r, row in enumerate(grid) for c, val in enumerate(row) if grid[r][c] > 0]
    centers = sorted(centers, key=attrgetter('size'), reverse=True)
    for center1, center2 in combination2_with_pruning(centers, lambda c1, c2: calc_score(c1.size, c2.size) > max_score):
        score = calc_score_with_adjusting_size(center1, center2)
        max_score = max(max_score, score)
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
    timeit_lp(solve, (n, m, grid), time_limit=1, funcs=[])  # , log=True, omit_func_args=True)


# @pytest.mark.skip
def test_compare():
    def gen_prob():
        ratio = 0.6
        n, m = 15, 15
        grid = [['#' if random.random() < ratio else '.' for _ in range(m)] for _ in range(n)]
        return merge_to_lines([
            list_to_string([n, m]),
            '\n'.join(''.join(row) for row in grid),
        ])
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
