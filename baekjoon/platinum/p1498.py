import sys


def solve(ptn):
    table = [0] * len(ptn)
    j = 0
    res = []
    base = 0
    for i in range(1, len(ptn)):
        while ptn[j] != ptn[i] and j > 0:
            j = table[j - 1]
            base = 0
        if ptn[j] == ptn[i]:
            j += 1
            table[i] = j
            if i + 1 == j * 2:
                base = j
            if base > 0 and (i + 1) % base == 0:
                res.append((i + 1, (i + 1) // base))
    return res


def main():
    stdin = sys.stdin
    txt = stdin.readline().strip()
    for i, n in solve(txt):
        print(i, n)


if __name__ == "__main__":
    main()

from util import *
import pytest
import random


def solve_naive(ptn):
    res = []
    for i in range(2, len(ptn) + 1):
        for j in range(1, i // 2 + 1):
            if ptn[:i].startswith(ptn[j:i]) and i % j == 0:
                res.append((i, i // j))
                break
    return res


def test_compare():
    def gen_prob():
        N = 6
        ptn = ''.join(random.choice('ab') for _ in range(N))
        return ptn

    compare_func_results(solve, solve_naive, generate_probs(gen_prob, count=100))


@pytest.mark.parametrize(('in_str', 'out_str'), [
    ('''
aabaab
    '''.strip(),
     '''
2 2
6 2
     '''.strip()),
    ('''
aabaabaabaab
    '''.strip(),
     '''
2 2
6 2
9 3
12 4
     '''.strip()),
    ('''
aaa
    '''.strip(),
     '''
2 2
3 3
     '''.strip()),
    ('''
aa
    '''.strip(),
     '''
2 2
     '''.strip()),
])
def test_main(in_str, out_str):
    assert mock_io(main)(in_str) == out_str


@pytest.mark.parametrize(('in_str', 'out_str'), [
    ('''
bababb
    '''.strip(),
     '''
4 2
     '''.strip()),
])
def test_found(in_str, out_str):
    assert mock_io(main)(in_str) == out_str

