import sys
from itertools import count, chain


def solve(xs, start, end):
    if start == end:
        return 0
    N = len(xs)
    visited = [False] * N
    stack = [start]
    for step in count(1):
        if not stack:
            return -1
        new_stack = []
        for idx in stack:
            gap = xs[idx]
            right_moves = range(idx + gap, N, gap)
            left_moves = range(idx - gap, -1, -gap)
            for next_idx in chain(right_moves, left_moves):
                if next_idx == end:
                    return step
                if not visited[next_idx]:
                    visited[next_idx] = True
                    new_stack.append(next_idx)
        stack = new_stack


def main():
    stdin = sys.stdin
    _ = stdin.readline()
    xs = [int(x) for x in stdin.readline().split()]
    start, end = [int(x) - 1 for x in stdin.readline().split()]
    print(solve(xs, start, end))


if __name__ == '__main__':
    main()


from util.result_check import get_output_with_stdin


def test_main():
    in_str = '''
5
1 2 2 1 2
1 5
    '''.strip()

    out_str = '''
1
'''.strip()
    assert get_output_with_stdin(main, in_str) == out_str
