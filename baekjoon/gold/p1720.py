import sys
from functools import reduce
from operator import mul


def factorial(n):
    ret = 1
    for i in range(2, n + 1):
        ret *= i
    return ret


def solve(N):
    def b(state):
        if state == (0, 0, 1) or state == (0, 0, 0):
            return 1
        if state in bmemory:
            return bmemory[state]

        numer = factorial(sum(state))
        denom = reduce(mul, (factorial(i) for i in state if i >= 2), 1)
        all_cases = numer // denom
        bmemory[state] = all_cases
        return all_cases

    def f(state):
        all_cases = b(state)
        odds_indices = [i for i, d in enumerate(state) if d % 2 == 1]
        if len(odds_indices) == 0:
            new_state = tuple(x // 2 for x in state)
            symmetric_cases = b(new_state)
        elif len(odds_indices) == 1:
            new_state = list(state)
            new_state[odds_indices[0]] -= 1
            new_state = tuple(x // 2 for x in new_state)
            symmetric_cases = b(new_state)
        else:
            symmetric_cases = 0

        memory[state] = (all_cases + symmetric_cases) // 2
        return memory[state]

    bmemory = {}
    memory = {}
    stack = []
    remain = N
    total_count = 0
    for tt in range(remain // 2 + 1):
        stack.append(tt)
        remain -= 2 * tt
        for ss in range(remain // 2 + 1):
            stack.append(ss)
            remain -= 2 * ss

            s = remain
            stack.append(s)

            state = tuple(sorted(stack))
            total_count += f(state)
            stack.pop()

            stack.pop()
            remain += 2 * ss

        remain += 2 * tt
        stack.pop()

    return total_count


def main():
    stdin = sys.stdin
    N = int(stdin.readline())
    print(solve(N))


if __name__ == "__main__":
    main()

from util.result_check import get_output_with_stdin, eprint
import pytest


@pytest.mark.parametrize(['n', 'e'], [
    (1, 1),
    (2, 3),
    (3, 3),
    (4, 8),
    (5, 12),
    (6, 27),
    (7, 45),
    (8, 96),
    (30, 357935787),
])
def test_main(n, e):
    assert get_output_with_stdin(main, str(n)) == str(e)


def test_time():
    assert get_output_with_stdin(main, str(30), ) == str(357935787)

