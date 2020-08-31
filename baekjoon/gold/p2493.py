import sys

INF = 110000000


def solve(N, xs):
    stack = [(0, INF)]
    res = []
    for idx, x in enumerate(xs, start=1):
        while stack[-1][1] < x:
            stack.pop()
        res.append(str(stack[-1][0]))
        stack.append((idx, x))
    return ' '.join(res)


def main():
    stdin = sys.stdin
    N = int(stdin.readline())
    xs = [int(x) for x in stdin.readline().split()]
    print(solve(N, xs))


if __name__ == "__main__":
    main()

from util.result_check import get_output_with_stdin


def test_main():
    in_str = """
5
6 9 5 7 4
    """.strip()
    out_str = """
0 0 2 2 4
    """.strip()
    assert get_output_with_stdin(main, in_str) == out_str


def test_add1():
    in_str = """
1
2
    """.strip()
    out_str = """
0
    """.strip()
    assert get_output_with_stdin(main, in_str) == out_str

