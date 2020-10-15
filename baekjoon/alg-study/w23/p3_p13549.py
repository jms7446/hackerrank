# 숨바꼭질3
import sys
from heapq import heappush, heappop

M = 100001


def solve(n, k):
    min_count = M
    heap = [(0, n)]
    visited = [False] * M
    while heap:
        count, cur = heappop(heap)
        if count >= min_count:
            break
        if cur < 0 or visited[cur]:
            continue
        visited[cur] = True

        while cur < k:
            heappush(heap, (count + 1, cur - 1))
            heappush(heap, (count + 1, cur + 1))
            if cur == 0:
                break
            else:
                cur *= 2
        if cur == k:
            min_count = count
            break
        elif cur > k:
            min_count = min(min_count, count + (cur - k))

    return min_count


def main():
    stdin = sys.stdin
    N, K = [int(x) for x in stdin.readline().split()]
    print(solve(N, K))


if __name__ == "__main__":
    main()

from util import *
import pytest


def test_time():
    timeit(solve, (1, 99999), time_limit=1)


@pytest.mark.parametrize(('in_str', 'out_str'), [
    # ('5 17', '2'),
    ('0 1', '1'),
    # ('1 1', '0'),
    # ('0 0', '0'),
    # ('1 99999', '0'),
])
def test_main(in_str, out_str):
    assert mock_io(main)(in_str) == out_str
