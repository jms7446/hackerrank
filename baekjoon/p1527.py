import sys
from itertools import product


def solve(A, B):
    A = tuple(str(A))
    B = tuple(str(B))
    count = sum(2 ** d for d in range(len(A), len(B)))
    for ss in product("47", repeat=len(A)):
        if ss < A:
            count -= 1
        else:
            break
    for ss in product("47", repeat=len(B)):
        if ss <= B:
            count += 1
        else:
            break
    return count


def main():
    stdin = sys.stdin
    A, B = [int(x) for x in stdin.readline().split()]
    print(solve(A, B))


if __name__ == "__main__":
    main()


from util.result_check import get_output_with_stdin


def test_main():
    in_str = """
1 10
""".strip()
    assert get_output_with_stdin(main, in_str) == "2"


def test_solve():
    assert solve(10, 77) == 4


def test_Numbers():
    numbers = Numbers(4)
    print(numbers[-1], file=sys.stderr)
