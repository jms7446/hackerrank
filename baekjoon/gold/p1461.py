import sys


def calc_steps(xs, M):
    if not xs:
        return 0
    xs = sorted(xs, reverse=True)
    steps = sum(xs[::M])
    return steps * 2


def solve(M, xs):
    pos_sides = sorted([x for x in xs if x > 0])
    neg_sides = sorted([-x for x in xs if x < 0])
    pos_sides_max = pos_sides[-1] if len(pos_sides) else 0
    neg_sides_max = neg_sides[-1] if len(neg_sides) else 0
    final_skip_steps = max(pos_sides_max, neg_sides_max)
    return calc_steps(pos_sides, M) + calc_steps(neg_sides, M) - final_skip_steps


def main():
    stdin = sys.stdin
    N, M = [int(x) for x in stdin.readline().split()]
    xs = [int(x) for x in stdin.readline().split()]
    print(solve(M, xs))


if __name__ == "__main__":
    main()


from util.result_check import get_output_with_stdin


def test_main():
    in_str = """
7 2
-37 2 -6 -39 -29 11 -28
    """.strip()
    assert get_output_with_stdin(main, in_str) == "131"


def test_main2():
    in_str = """
3 2
1 5 4
    """.strip()
    assert get_output_with_stdin(main, in_str) == "7"


def test_main3():
    in_str = """
0 3
    """.strip()
    assert get_output_with_stdin(main, in_str) == "0"


def test_main4():
    in_str = """
4 3
1 5 4 7
    """.strip()
    assert get_output_with_stdin(main, in_str) == "9"

