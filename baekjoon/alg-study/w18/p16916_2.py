import sys


# 40.55ms
def solve_rabin_karp2(txt, ptn):
    N = len(txt)
    M = len(ptn)
    d = 256
    q = 101
    if N < M:
        return 0

    p = t = 0
    for i in range(len(ptn)):
        p = (d * p + ord(ptn[i])) % q
        t = (d * t + ord(txt[i])) % q

    h = 1
    for i in range(len(ptn) - 1):
        h = (h * d) % q

    if p == t and txt[:M] == ptn:
        return 1
    for i in range(N - M):
        t = (d * (t - ord(txt[i]) * h) + ord(txt[i+M])) % q
        if p == t and txt[i+1:i+M+1] == ptn:
            return 1
    return 0


def main():
    stdin = sys.stdin
    S = stdin.readline().strip()
    P = stdin.readline().strip()
    print(solve_rabin_karp2(S, P))


if __name__ == "__main__":
    main()


from util import *
import pytest


import random, string


def find_sub(txt, ptn):
    return int(ptn in txt)


def test_compare():
    def gen_prob():
        N = 100
        P = random.randint(1, 1000)
        in_str = ''.join(random.choice(string.ascii_lowercase) for _ in range(N))
        ptn = ''.join(random.choice(string.ascii_lowercase) for _ in range(P))
        return in_str, ptn

    compare_func_results(find_sub, solve_rabin_karp2, generate_probs(gen_prob, count=10000))


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
    ('''
kfeqyxskhnjkwvvxokzgpbpblauylmkajbiajxknkeflwjihynthwdbskpawyeriaeibnlzputkfyiestsncuutjjcuarynbtpal
qroyarrvwragtrelyrjxgxjmyoaqypdjncqxahaxzajfqjpjipribvdfcghlgkkjbrvtjxaiepbrxphpyprlqtfuinumwqxupsvpgqowqbvmhynrpaxxsgsmhyywwuxtrpgoinhppvgrtpzbwvncpewkhoqktomxjwgxkeibydxpdvxzcxpbtkdzgksedqyyayzjhhuwcpshqvvqlcrgtcescfzduwtiiqwrhxpzgzrmchpmueupjdfmdqeqgribopnvfchjrsuizrxfqbqyqwaxryslkycmtrbuaoxnjwmycdymyotnxxssgiivkjwfdjndihaayafqopaqrvmtufkcoieuckpwbfbfnybnzxxfqutwxxuarxdhmfrodrpeuhagejwczmdzjkkyeohauewxxcovolxelteoivhkojwscphokesjrbyloedydhobkzekffkonoyttirnhzmhy
    '''.strip(),
     '''
0
     '''.strip()),
])
def test_main(in_str, out_str):
    assert mock_io(main)(in_str) == out_str
