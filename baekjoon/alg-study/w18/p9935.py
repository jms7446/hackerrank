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


def test_main():
    in_str = """
mirkovC4nizCC44
C4
    """.strip()
    out_str = """
mirkovniz
    """.strip()
    assert evaluate_via_io(main, in_str) == out_str


def test_main2():
    in_str = """
12ab112ab2ab
12ab
    """.strip()
    out_str = """
FRULA
    """.strip()
    assert evaluate_via_io(main, in_str) == out_str


def test_main3():
    in_str = """
1
1
    """.strip()
    out_str = """
FRULA
    """.strip()
    assert evaluate_via_io(main, in_str) == out_str


def test_main4():
    in_str = """
1
2
    """.strip()
    out_str = """
1
    """.strip()
    assert evaluate_via_io(main, in_str) == out_str


def test_time():
    timeit(solve, ('12345' * 1000, '123'), num_iter=100)
