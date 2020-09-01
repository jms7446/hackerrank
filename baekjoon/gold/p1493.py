import sys


# compare other's solution but I can find no edge cases, but fail to be accepted.
def solve(L, W, H, _, X):
    sizes = sorted([L, W, H])
    base_size = sizes[0]
    base_type = int.bit_length(base_size) - 1
    base_count = (sizes[1] // sizes[0]) * (sizes[2] // sizes[0])

    used_count = 0
    remain = base_count
    cubes = dict(X)
    for cur_type in range(base_type, -1, -1):
        count = cubes.get(cur_type, 0)
        if count > 0:
            if remain <= count:
                return used_count + remain
            else:
                remain -= count
                used_count += count
        remain *= 8
    return -1


def main():
    stdin = sys.stdin
    L, W, H = [int(x) for x in stdin.readline().split()]
    N = int(stdin.readline())
    X = [[int(x) for x in stdin.readline().split()] for _ in range(N)]
    print(solve(L, W, H, N, X))


if __name__ == "__main__":
    main()


import pytest
from random import randint
from util import *


@pytest.mark.parametrize(('in_str', 'out_str'), [
    ('''
4 4 8
3
0 10
1 10
2 1
        '''.strip(), '9'),
    ('''
2 4 8
3
0 10
1 10
2 1
            '''.strip(), '8'),
    ('''
2 4 8
2
0 10
1 5
                '''.strip(), '-1'),
    ('''
8 4 8
3
0 10
1 10
2 1
            '''.strip(), '-1'),
    ('''
1 1 1
0
            '''.strip(), '-1'),
    ('''
32 64 128
6
0 10
1 10
2 1
3 500
5 1
6 1
    '''.strip(), '449'),
])
def test_main(in_str, out_str):
    assert evaluate_via_io(main, in_str) == out_str


def test_found_edge_case():
    in_str = '''
2 16 16
2
0 54
1 15
    '''.strip()
    out_str = '-1'
    assert evaluate_via_io(main, in_str) == out_str


def gen_probs(LR=20, NR=20, XR=6, K=20):
    L, W, H = [2 ** randint(0, LR) for _ in range(3)]
    N = randint(1, NR)
    X = random_choices([(i, randint(0, 10**XR)) for i in range(K)], k=N)
    return merge_to_lines([
        [L, W, H],
        N,
        merge_to_lines(X),
    ])


@pytest.mark.skip
def test_compare():
    input_generator = generate_probs(gen_probs, count=10000)
    find_edge_case_by_external_program('p1493', main, input_generator)
