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


def solve(txt, ptn):
    return list(KMP(ptn).search(txt))


def main():
    stdin = sys.stdin
    T = stdin.readline().rstrip('\n')
    P = stdin.readline().rstrip('\n')
    result = solve(T, P)
    print(len(result))
    print(' '.join(str(idx + 1) for idx in result))    # convert to 1-base index


if __name__ == "__main__":
    main()


from util import *


def test_main():
    in_str = """
ABC ABCDAB ABCDABCDABDE
ABCDABD
    """.strip()
    out_str = """
1
16
    """.strip()
    assert mock_io(main)(in_str) == out_str


def test_add():
    in_str = """
ABC ABCDAB ABCDABCDABDE
ABC
    """.strip()
    out_str = """
4
1 5 12 16
    """.strip()
    assert mock_io(main)(in_str) == out_str


def test_add2():
    in_str = """
ABC ABCDAB ABCDABCDABDE
ABCX
    """.strip()
    out_str = """
0

    """.strip()
    assert mock_io(main)(in_str) == out_str


def test_add3():
    in_str = """
ABC 
ABC  
    """.strip()
    out_str = """
1
1
    """.strip()
    assert mock_io(main)(in_str) == out_str


from util.cc_tools import str_findall
import random


def naive_search(txt, ptn):
    return list(str_findall(ptn, txt))


def test_compare():

    def prob_gen(L):
        N = random.randint(1, L)
        M = random.randint(1, L)
        txt = ''.join(random.choice(alphabet) for _ in range(N))
        ptn = ''.join(random.choice(alphabet) for _ in range(M))
        return txt, ptn

    alphabet = 'ABC '
    compare_func_results(solve, naive_search, generate_probs(prob_gen, (5, ), count=10))
