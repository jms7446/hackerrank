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


from util.result_check import get_output_with_stdin, check_elapse_time
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
    assert get_output_with_stdin(main, in_str, check_time=True) == out_str


def test_time():
    in_str = '12345' * 1000
    ptn = '123'
    check_elapse_time(solve, (in_str, ptn), num_iter=1000)