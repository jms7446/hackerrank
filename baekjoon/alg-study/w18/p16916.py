import sys


class KMP:
    def __init__(self, ptn):
        self.ptn = ptn
        self.table = self.make_partial_match_table(ptn)

    @staticmethod
    def make_partial_match_table(ptn):
        table = [0] * len(ptn)
        cnd = 0
        for pos in range(1, len(ptn)):
            while cnd > 0 and ptn[pos] != ptn[cnd]:
                cnd = table[cnd - 1]
            if ptn[pos] == ptn[cnd]:
                cnd += 1
                table[pos] = cnd
        return table

    def search(self, in_str):
        ptn = self.ptn
        table = self.table
        len_ptn_minus1 = len(ptn) - 1
        j = 0
        for i, c in enumerate(in_str):
            while j > 0 and c != ptn[j]:
                j = table[j-1]
            if c == ptn[j]:
                if j == len_ptn_minus1:
                    yield i - len(ptn) + 1
                    j = table[j]
                else:
                    j += 1


# elapse time - test_big: 123ms, test_small: 119ms
def solve(S, P):
    if len(S) < len(P):
        return 0

    kmp = KMP(P)
    for _ in kmp.search(S):
        return 1
    return 0


def main():
    stdin = sys.stdin
    S = stdin.readline().strip()
    P = stdin.readline().strip()
    print(solve(S, P))


if __name__ == "__main__":
    main()


from util import *
import pytest


def test_time1():
    import random
    import string

    N = 100000
    P = 1000
    random.seed(2)
    in_str = ''.join(random.choice(string.ascii_lowercase) for _ in range(N))
    ptn = ''.join(random.choice(string.ascii_lowercase) for _ in range(P))
    timeit_lp(solve, (in_str, ptn), num_iter=2, funcs=[KMP.make_partial_match_table, KMP.search], log=False)


def test_time2():
    import random
    import string

    N = 100000
    P = 100
    random.seed(2)
    in_str = ''.join(random.choice(string.ascii_lowercase) for _ in range(N))
    ptn = ''.join(random.choice(string.ascii_lowercase) for _ in range(P))
    timeit_lp(solve, (in_str, ptn), num_iter=2, funcs=[KMP.make_partial_match_table, KMP.search], log=False)


def test_kmp_table():
    kmp = KMP('abababac')
    assert kmp.table == [0, 0, 1, 2, 3, 4, 5, 0]
    assert list(kmp.search('xababababababac')) == [7]


@pytest.mark.parametrize(('in_str', 'out_str'), [
    ('''
baekjoon
aek
    '''.strip(),
     '''
1
     '''.strip()),
    ('''
baekjoon
bak
    '''.strip(),
     '''
0
     '''.strip()),
    ('''
baekjoon
joo
    '''.strip(),
     '''
1
     '''.strip()),
    ('''
baekjoon
oone
    '''.strip(),
     '''
0
     '''.strip()),
    ('''
baekjoon
online
    '''.strip(),
     '''
0
     '''.strip()),
    ('''
baekjoon
baekjoon
    '''.strip(),
     '''
1
     '''.strip()),
])
def test_main(in_str, out_str):
    assert mock_io(main)(in_str) == out_str


################################################################################
# old tries (for comparision)
################################################################################

# elapse time - test_big: 3.06ms, test_small: 0.675ms
def solve_naive(S, P):
    return 1 if S.find(P) >= 0 else 0


# from http://code.activestate.com/recipes/117214/
def KnuthMorrisPratt(text, pattern):
    # allow indexing into pattern and protect against change during yield
    pattern = list(pattern)

    # build table of shift amounts
    shifts = [1] * (len(pattern) + 1)
    shift = 1
    for pos in range(len(pattern)):
        while shift <= pos and pattern[pos] != pattern[pos-shift]:
            shift += shifts[pos-shift]
        shifts[pos+1] = shift

    # do the actual search
    startPos = 0
    matchLen = 0
    for c in text:
        while matchLen == len(pattern) or \
                matchLen >= 0 and pattern[matchLen] != c:
            startPos += shifts[matchLen]
            matchLen -= shifts[matchLen]
        matchLen += 1
        if matchLen == len(pattern):
            yield startPos


# elapse time - test_big: 473ms, test_small: 416ms
def solve_KnuthMorrisPratt(S, P):
    for _ in KnuthMorrisPratt(S, P):
        return 1
    return 0
