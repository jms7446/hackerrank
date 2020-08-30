import sys


def solve(S, P):
    def remove_matched_and_get_next_index():
        for _ in range(L):
            stack.pop()
        if stack:
            return stack[-1][1]
        else:
            return 0

    stack = []
    L = len(P)
    idx = 0
    for c in S:
        if c == P[idx]:
            idx += 1
            stack.append((c, idx))
            if idx == L:
                idx = remove_matched_and_get_next_index()
        else:
            if c == P[0]:
                idx = 1
            else:
                idx = 0
            stack.append((c, idx))

    if stack:
        return ''.join(x[0] for x in stack)
    else:
        return 'FRULA'


def main():
    stdin = sys.stdin
    S = stdin.readline().strip()
    P = stdin.readline().strip()
    print(solve(S, P))


if __name__ == "__main__":
    main()



from util.result_check import get_output_with_stdin
import pytest


def test_main():
    in_str = """
mirkovC4nizCC44
C4
    """.strip()
    out_str = """
mirkovniz
    """.strip()
    assert get_output_with_stdin(main, in_str) == out_str


def test_main2():
    in_str = """
12ab112ab2ab
12ab
    """.strip()
    out_str = """
FRULA
    """.strip()
    assert get_output_with_stdin(main, in_str) == out_str


def test_main3():
    in_str = """
1
1
    """.strip()
    out_str = """
FRULA
    """.strip()
    assert get_output_with_stdin(main, in_str) == out_str


def test_main4():
    in_str = """
1
2
    """.strip()
    out_str = """
1
    """.strip()
    assert get_output_with_stdin(main, in_str) == out_str


# @pytest.mark.skip
def test_time():
    import time
    s = '12345' * 1000
    ptn = '123'
    st = time.time()
    for _ in range(1000):
        solve(s, ptn)
    print('elapse time: ', time.time() - st, file=sys.stderr)
