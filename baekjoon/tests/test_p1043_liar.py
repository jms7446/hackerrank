from baekjoon.p1043_liar import main
from util.result_check import get_output_with_stdin


def test_main():
    inputs = """
4 3
0
2 1 2
1 3
3 2 3 4
    """.strip()
    outputs = "3"
    assert get_output_with_stdin(main, inputs) == outputs


def test_main2():
    inputs = """
4 3
1 1
2 1 2
1 3
3 2 3 4
    """.strip()
    outputs = "0"
    assert get_output_with_stdin(main, inputs) == outputs
