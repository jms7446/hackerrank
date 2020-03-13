from beakjoon.p14890_decline import main, is_valid_road
from util.result_check import get_output_with_stdin

import pytest


@pytest.mark.parametrize(("in_str", "L", "expected"), [
    ("3 3 4 4 5 5", 2, True),
    ("3 4 5 4 3", 1, True),
    ("4 3 3 3 3 3 3 4 4 4 5", 3, True),
])
def test_is_valid_road(in_str, L, expected):
    road = [int(x) for x in in_str.split()]
    assert(is_valid_road(road, L) == expected)


@pytest.mark.parametrize(("inputs", "outputs"), [
    ("""
6 2
3 3 3 3 3 3
2 3 3 3 3 3
2 2 2 3 2 3
1 1 1 2 2 2
1 1 1 3 3 1
1 1 2 3 3 2
""",
     "3"),

    ("""
6 2
3 2 1 1 2 3
3 2 2 1 2 3
3 2 2 2 3 3
3 3 3 3 3 3
3 3 3 3 2 2
3 3 3 3 2 2
""",
     "7"),
    ("""
6 3
3 2 1 1 2 3
3 2 2 1 2 3
3 2 2 2 3 3
3 3 3 3 3 3
3 3 3 3 2 2
3 3 3 3 2 2
""",
     "3"),
    ("""
6 1
3 2 1 1 2 3
3 2 2 1 2 3
3 2 2 2 3 3
3 3 3 3 3 3
3 3 3 3 2 2
3 3 3 3 2 2
""",
     "11"),
    ("""
1 1
1
""",
     "2"),
])
def test_main(inputs, outputs):
    inputs = inputs.strip()
    assert get_output_with_stdin(main, inputs) == outputs
