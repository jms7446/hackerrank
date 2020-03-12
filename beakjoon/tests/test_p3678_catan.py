from beakjoon.p3678_catan import katan, main, init_katan_table, calc_num_layers
from util import result_check


def test_katan():
    pos_list = [1, 4, 10, 100, 1]
    assert katan(pos_list) == [1, 4, 5, 5, 1]


def test_katan_tmp():
    pos_list = [1, 4, 10, 100, 9998, 9999, 10000]
    print(katan(pos_list))


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


def test_init_katan_table_1():
    init_katan_table(4)

