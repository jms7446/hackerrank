import sys


def solve():
    return -1


def main():
    stdin = sys.stdin
    PN = int(stdin.readline())
    for _ in range(PN):
        N, M = [int(x) for x in stdin.readline().split()]
        _ = [[int(x) - 1 for x in stdin.readline().split()] for _ in range(M)]
        print(solve())


if __name__ == "__main__":
    main()


from util.result_check import get_output_with_stdin


def test_main():
    in_str = """
""".strip()
    assert get_output_with_stdin(main, in_str) == ""
