import sys
from itertools import count

N = 100001


def solve(start, end):
    if start >= end:
        return start - end
    visited = [False] * N
    stack = [start]
    for step in count(1):
        new_stack = []
        for pos in stack:
            for next_pos in [pos - 1, pos + 1, pos * 2]:
                if 0 <= next_pos < N and not visited[next_pos]:
                    if next_pos == end:
                        return step
                    visited[next_pos] = True
                    new_stack.append(next_pos)
        stack = new_stack


def main():
    stdin = sys.stdin
    x, y = [int(i) for i in stdin.readline().split()]
    print(solve(x, y))


if __name__ == '__main__':
    main()


from util.result_check import get_output_with_stdin


def test_main():
    in_str = '''
5 17
    '''.strip()

    out_str = '''
4
'''.strip()
    assert get_output_with_stdin(main, in_str) == out_str


def test_main():
    in_str = '''
10000 100000
    '''.strip()

    out_str = '''
2503
'''.strip()
    assert get_output_with_stdin(main, in_str) == out_str
