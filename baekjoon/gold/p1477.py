import sys
from itertools import chain, takewhile
import math


def solve(N, M, L, xs):
    def is_possible(guess):
        need_to_cut = takewhile(lambda dist: dist > guess, dists)
        cuts = sum(math.ceil(dist / guess) - 1 for dist in need_to_cut)
        if cuts > M:
            return False
        return True

    locations = sorted(chain([0], xs, [L]))
    dists = sorted([l2 - l1 for l1, l2 in zip(locations, locations[1:])], reverse=True)

    left = L // (N + M + 1)
    right = dists[0]
    solution = None
    while left <= right:
        mid = (right + left) // 2
        if is_possible(mid):
            solution = mid
            right = mid - 1
        else:
            left = mid + 1
    return solution


def main():
    stdin = sys.stdin
    N, M, L = [int(x) for x in stdin.readline().split()]
    xs = [int(x) for x in stdin.readline().split()]
    print(solve(N, M, L, xs))


if __name__ == "__main__":
    main()


from util import *


def test_main():
    in_str = """
6 7 800
622 411 201 555 755 82
""".strip()
    assert evaluate_via_io(main, in_str) == "70"


def test_main2():
    in_str = """
0 1 800
""".strip()
    assert evaluate_via_io(main, in_str) == "400"


def test_main3():
    in_str = """
0 0 800
""".strip()
    assert evaluate_via_io(main, in_str) == "800"
