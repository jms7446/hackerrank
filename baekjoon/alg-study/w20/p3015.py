import sys


# timeout
# 520.13ms
def solve_org(n, xs):
    count = 0
    stack = []
    for x in xs:
        for i in reversed(range(len(stack))):
            count += 1
            if stack[i] > x:
                break
            elif stack[i] < x:
                stack.pop()
        stack.append(x)
    return count


# 486.21ms
def solve(n, xs):
    count = 0
    stack = []
    for x in xs:
        for i in reversed(range(len(stack))):
            if stack[i][0] > x:
                count += 1
                break
            elif stack[i][0] == x:
                count += stack[i][1]
            else:
                count += stack[i][1]
                stack.pop()
        if stack and stack[-1][0] == x:
            stack[-1][1] += 1
        else:
            stack.append([x, 1])
    return count


def main():
    stdin = sys.stdin
    n = int(stdin.readline())
    xs = [int(stdin.readline().strip()) for _ in range(n)]
    print(solve(n, xs))


if __name__ == "__main__":
    main()

from util import *
import random


def test_time():
    func = solve_org
    N = 10000
    xs = [random.randint(1, 5) for _ in range(N)]
    timeit(func, (N, xs), num_iter=100)


def test_main():
    in_str = """
7
2
4
1
2
2
5
1
    """.strip()
    out_str = """
10
    """.strip()
    assert mock_io(main)(in_str) == out_str


def test_main2():
    in_str = """
1
1
    """.strip()
    out_str = """
0
    """.strip()
    assert mock_io(main)(in_str) == out_str
