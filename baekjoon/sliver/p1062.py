import sys
from collections import defaultdict

A = 26


def solve(N, K, words):
    pass

    return -1


def main():
    stdin = sys.stdin
    N, K = [int(x) for x in stdin.readline().split()]
    words = [stdin.readline().strip() for _ in range(N)]
    print(solve(N, K, words))


if __name__ == "__main__":
    main()


from util.result_check import get_output_with_stdin


def test_main():
    in_str = """
3 6
antarctica
antahellotica
antacartica
""".strip()
    assert get_output_with_stdin(main, in_str) == "2"
