################################################################################
# profiling
################################################################################
# base_version : 3.30ms
# 모두 스택에 먼저 넣는 버전 : 8.15ms
# ptn을 list로 번경 : 5.50ms
# add_last_c : 4.28ms
# len(stack) < L 제거 : 3.41
################################################################################


import sys


def solve(in_str, ptn):
    stack = []
    ptn = list(ptn)
    ptn_len = len(ptn)
    last_char = ptn[-1]
    for c in in_str:
        stack.append(c)
        if c == last_char and stack[-ptn_len:] == ptn:
            del stack[-ptn_len:]

    return ''.join(x[0] for x in stack) if stack else 'FRULA'


def main():
    stdin = sys.stdin
    S = stdin.readline().strip()
    P = stdin.readline().strip()
    print(solve(S, P))


if __name__ == "__main__":
    main()


from util import *


def test_time():
    prob = ('1234567' * 1000) + ('abc' * 1000)
    ptn = '123456'
    timeit_lp(solve, (prob, ptn), num_iter=100, time_limit=0.5, omit_func_args=True, log=True, changed='remove: len(stack) < L')


def test_main():
    in_str = """
mirkovC4nizCC44
C4
    """.strip()
    out_str = """
mirkovniz
    """.strip()
    assert mock_io(main)(in_str) == out_str


def test_main2():
    in_str = """
12ab112ab2ab
12ab
    """.strip()
    out_str = """
FRULA
    """.strip()
    assert mock_io(main)(in_str) == out_str


def test_main3():
    in_str = """
1
1
    """.strip()
    out_str = """
FRULA
    """.strip()
    assert mock_io(main)(in_str) == out_str


def test_main4():
    in_str = """
1
2
    """.strip()
    out_str = """
1
    """.strip()
    assert mock_io(main)(in_str) == out_str


################################################################################
# old version
################################################################################

def solve_old(in_str, ptn):
    def remove_matched_and_get_next_index():
        for _ in range(L):
            stack.pop()
        if stack:
            return stack[-1][1]
        else:
            return 0

    stack = []
    L = len(ptn)
    idx = 0
    for c in in_str:
        if c == ptn[idx]:
            idx += 1
            stack.append((c, idx))
            if idx == L:
                idx = remove_matched_and_get_next_index()
        else:
            if c == ptn[0]:
                idx = 1
            else:
                idx = 0
            stack.append((c, idx))

    if stack:
        return ''.join(x[0] for x in stack)
    else:
        return 'FRULA'


def solve_old2(in_str, ptn):
    stack = []
    L = len(ptn)
    for c in in_str:
        stack.append(c)
        if len(stack) < L:
            continue
        for i in range(1, L + 1):
            if stack[-i] != ptn[-i]:
                break
        else:
            stack = stack[:-L]

    return ''.join(x[0] for x in stack) if stack else 'FRULA'
