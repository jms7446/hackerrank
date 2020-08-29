import sys


def solve(N, K, sensors):
    sensors = sorted(sensors)
    gaps = sorted([y - x for (x, y) in zip(sensors, sensors[1:])], reverse=True)
    return sensors[-1] - sensors[0] - sum(gaps[:K-1])


def main():
    stdin = sys.stdin
    N = int(stdin.readline())
    K = int(stdin.readline())
    sensors = [int(x) for x in stdin.readline().split()]
    print(solve(N, K, sensors))


if __name__ == "__main__":
    main()


from util.result_check import get_output_with_stdin


def test_main():
    in_str = """
6
2
1 6 9 3 6 7    
    """.strip()
    assert get_output_with_stdin(main, in_str) == "5"
