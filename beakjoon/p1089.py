import sys


INVALIDS = {4, 10}

cache = {}
number_map = None


def replace_str_by_index(s, pos, r):
    return "".join([s[:pos] + r + s[pos + 1:]])


def parse_numbers(displayed, N):
    display_numbers = ["".join([row[4 * n: 4 * (n + 1) - 1] for row in displayed]) for n in range(N)]
    return display_numbers


def make_possible_numbers(shape):
    if shape in cache:
        return cache[shape]
    if number_map.get(shape, None) == 8:
        return {8}

    possible_numbers = {number_map[shape]} if shape in number_map else set()
    for i, c in enumerate(shape):
        if i not in INVALIDS and c == ".":
            new_shape = replace_str_by_index(shape, i, "#")
            possible_numbers = possible_numbers.union(make_possible_numbers(new_shape))

    cache[shape] = possible_numbers
    return possible_numbers


def make_number_map():
    org_number_str = """
###...#.###.###.#.#.###.###.###.###.###
#.#...#...#...#.#.#.#...#.....#.#.#.#.#
#.#...#.###.###.###.###.###...#.###.###
#.#...#.#.....#...#...#.#.#...#.#.#...#
###...#.###.###...#.###.###...#.###.###
    """.strip()
    number_map = {shape: num for num, shape in enumerate(parse_numbers(org_number_str.split("\n"), 10))}
    return number_map


def make_number(digits):
    N = len(digits)
    return sum(d * 10 ** (N - i - 1) for i, d in enumerate(digits))


def solve(displayed, N):
    # from itertools import product
    global number_map
    number_map = make_number_map()
    displayed_numbers = parse_numbers(displayed, N)
    possible_numbers_list = [make_possible_numbers(displayed_number) for displayed_number in displayed_numbers]
    if any(len(numbers) == 0 for numbers in possible_numbers_list):
        return -1
    return sum(sum(numbers) * 10 ** (N - i - 1) / len(numbers) for i, numbers in enumerate(possible_numbers_list))


def main():
    stdin = sys.stdin
    N = int(stdin.readline())
    displayed = [line.strip() for line in stdin.readlines()]
    print(solve(displayed, N))


if __name__ == "__main__":
    main()


import pytest

from util.result_check import get_output_with_stdin


def test_make_number_map():
    number_map = make_number_map()
    assert len(number_map) == 10
    assert number_map["####.##.##.####"] == 0


def test_main():
    in_str = """
2
###.###
#.#.#.#
#.#.###
#.#...#
###.###    
""".strip()
    res = float(get_output_with_stdin(main, in_str))
    print(res, file=sys.stderr)
    assert res == pytest.approx(48.5)


def test_possible_numbers():
    global number_map
    number_map = make_number_map()

    in_str = "".join("""
..#
...
...
...
..#    
""".split())

    print(make_possible_numbers(in_str), file=sys.stderr)


def test_make_number():
    assert make_number([0, 0, 1, 2, 3]) == 123
