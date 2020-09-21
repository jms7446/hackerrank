# 광고

import sys


def solve(L, txt):
    table = [0] * L
    j = 0
    for i in range(1, L):
        while txt[j] != txt[i] and j > 0:
            j = table[j - 1]
        if txt[j] == txt[i]:
            j += 1
            table[i] = j
            if j * 2 - 1 == i and txt.startswith(txt[i:]):
                return i
    return L - j


def main():
    stdin = sys.stdin
    L = int(stdin.readline())
    s = stdin.readline().strip()
    print(solve(L, s))


if __name__ == "__main__":
    main()

from util import *
import pytest


@pytest.mark.parametrize(('in_str', 'out_str'), [
    ('''
5
aaaaa
        '''.strip(), '1'),
    ('''
6
aabaaa
        '''.strip(), '4'),
    ('''
4
abca
    '''.strip(), '3'),
])
def test_main(in_str, out_str):
    assert mock_io(main)(in_str) == out_str

