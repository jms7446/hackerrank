import sys
from collections import Counter


def get_not_divided_numbers(n):
    numbers = []
    for i in range(1, n + 1):
        if all(j % i != 0 for j in range(i + 1, n + 1)):
            numbers.append(i)
    return numbers


def solve(M, s):
    def calc_remain_count(start, step):
        return Counter(s[start::step]).most_common(n=1)[0][1]

    remain_counts = []
    for m in get_not_divided_numbers(M):
        remain_count = sum(calc_remain_count(k, m) for k in range(m))
        remain_counts.append(remain_count)
    return len(s) - max(remain_counts)


def main():
    stdin = sys.stdin
    M = int(stdin.readline())
    s = stdin.readline().strip()
    print(solve(M, s))


if __name__ == "__main__":
    main()


from util.result_check import get_output_with_stdin


def test_main():
    in_str = """
2
ACGTGCA
""".strip()
    assert get_output_with_stdin(main, in_str) == "3"


def test_get_not_divided_numbers():
    assert get_not_divided_numbers(10) == [6, 7, 8, 9, 10]
