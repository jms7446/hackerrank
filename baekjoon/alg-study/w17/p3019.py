import sys


shape_map = {
    1: [[0], [0, 0, 0, 0]],
    2: [[0, 0]],
    3: [[0, 0, 1], [1, 0]],
    4: [[1, 0, 0], [0, 1]],
    5: [[0, 0, 0], [1, 0, 1], [0, 1], [1, 0]],
    6: [[0, 0, 0], [0, 1, 1], [0, 0], [2, 0]],
    7: [[0, 0, 0], [1, 1, 0], [0, 0], [0, 2]],
}


def match_height(xs, ys):
    diffs = {x - y for x, y in zip(xs, ys)}
    return len(diffs) == 1


def solve(C, P, heights):
    count = 0
    for shape in shape_map[P]:
        size = len(shape)
        for i in range(C - size + 1):
            if match_height(shape, heights[i:i+size]):
                count += 1
    return count


def main():
    stdin = sys.stdin
    C, P = [int(x) for x in stdin.readline().split()]
    heights = [int(x) for x in stdin.readline().split()]
    print(solve(C, P, heights))


if __name__ == '__main__':
    main()


from util.result_check import get_output_with_stdin
import pytest


@pytest.mark.parametrize(('in_str', 'out_str'), [
    ('''
    6 5
    2 1 1 1 0 1
        '''.strip(),
     '5'),
    ('''
1 2
2
    '''.strip(),
     '0'),
])
def test_main(in_str, out_str):
    assert get_output_with_stdin(main, in_str) == out_str
