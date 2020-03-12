from beakjoon.p3678_catan import katan, main
from util import result_check


def test_katan():
    pos_list = [1, 4, 10, 100, 1]
    assert katan(pos_list) == [1, 4, 5, 5, 1]


def test_main():
    inputs = """
4
1
4
10
100
    """.strip()
    outputs = """
1
4
5
5
    """.strip()
    assert result_check.get_output_with_stdin(main, inputs).strip() == outputs
