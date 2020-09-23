# 축사 배정, 이분 매칭

import sys


def solve(N, M, prefers):
    def allocate(person, visited):
        for room in prefers[person]:
            if visited[room]:
                continue
            visited[room] = True
            if rooms[room] == -1 or allocate(rooms[room], visited):
                rooms[room] = person
                return True
        return False

    rooms = [-1] * M
    res = 0
    for person in range(N):
        visited = [False] * M
        if allocate(person, visited):
            res += 1
    return res


def main():
    stdin = sys.stdin
    N, M = [int(x) for x in stdin.readline().split()]
    xs_list = [[int(x) - 1 for x in stdin.readline().split()[1:]] for _ in range(N)]
    print(solve(N, M, xs_list))


if __name__ == "__main__":
    main()

from util import *
import pytest


@pytest.mark.parametrize(('in_str', 'out_str'), [
    ('''
5 5
2 2 5
3 2 3 4
2 1 5
3 1 2 5
1 2
    '''.strip(),
     '''
4
     '''.strip()),
])
def test_main(in_str, out_str):
    assert mock_io(main)(in_str) == out_str
