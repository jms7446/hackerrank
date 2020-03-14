
import sys


INIT_CHANNEL = 100


def digits_to_number(digits):
    number = 0
    for d in digits:
        number = number * 10 + d
    return number


def make_min_large_order_number(valid_digits, n):
    if valid_digits == [0]:
        return None
    min_digit = min(valid_digits)
    min_digit_except_zero = min(d for d in valid_digits if d > 0)
    return digits_to_number([min_digit_except_zero] + [min_digit] * (n - 1))


def make_max_lower_order_number(valid_digits, n):
    if n == 0:
        return None
    return digits_to_number([max(valid_digits)] * n)


def get_closest_number(target, valid_digits, is_upper):

    N = len(str(target))
    sign = 1 if is_upper else -1
    target = sign * target
    signed_valid_digits = {sign * d for d in valid_digits}

    max_digit = max(signed_valid_digits)
    cur_number = digits_to_number([max_digit] * N)
    if cur_number < target:
        if is_upper:
            return make_min_large_order_number(valid_digits, N + 1)
        else:
            return make_max_lower_order_number(valid_digits, N - 1)

    sorted_valid_buttons = sorted(signed_valid_digits)
    for b in reversed(range(N)):
        base = 10 ** b
        for d in sorted_valid_buttons:
            candidate = cur_number - (max_digit - d) * base
            if candidate >= target:
                cur_number = candidate
                break
    return sign * cur_number


def calc_button_count_by_number(target, number):
    return len(str(number)) + abs(target - number)


def calc_count_with_digits(target, valid_digits):
    candidate_numbers = [
        get_closest_number(target, valid_digits, is_upper=True),
        get_closest_number(target, valid_digits, is_upper=False),
    ]
    # 두 값이 동시에 None 이 되는 경우는 존재하지 않는다.
    return min(calc_button_count_by_number(target, number) for number in candidate_numbers if number is not None)


def calc_count_without_digits(target):
    return abs(target - INIT_CHANNEL)


def solve(target, broken_buttons):
    valid_digits = [i for i in range(10) if i not in broken_buttons]
    press_count = calc_count_without_digits(target)
    if valid_digits:
        press_count = min(press_count, calc_count_with_digits(target, valid_digits))
    return press_count


def main():
    stdin = sys.stdin
    target = int(stdin.readline())
    _ = stdin.readline()
    broken_buttons = {int(x) for x in stdin.readline().split()}
    print(solve(target, broken_buttons))


if __name__ == "__main__":
    main()


from util.result_check import get_output_with_stdin
import pytest


import random


@pytest.mark.parametrize(("in_str", "expected"), [
    ("""
5457
3
6 7 8
    """, "6"),
    ("""
100
5
0 1 2 3 4
    """, "0"),
    ("""
500000
8
0 2 3 4 6 7 8 9
    """, "11117"),
    ("""
0
10
0 1 2 3 4 5 6 7 8 9
    """, "100"),
    ("""
90
0
    """, "2"),
    ("""
101
0
    """, "1"),
    ("""
30
9
1 2 3 4 5 6 7 8 9
    """, "31"),
    ("""
10
3
0 2 3 8
    """, "2"),
    ("""
80879
5
4 6 7 8 9
    """, "19127"),
    ("""
1
8
0 1 2 3 4 5 8 9
    """, "6"),
])
def test_main(in_str, expected):
    assert get_output_with_stdin(main, in_str.strip()) == expected


def test_get_closest_number_with_upper():
    assert get_closest_number(3792, [1, 3, 5, 8], is_upper=True) == 3811
    assert get_closest_number(9111, [1, 3, 5, 8], is_upper=True) == 11111
    assert get_closest_number(1358, [1, 3, 5, 8], is_upper=True) == 1358
    assert get_closest_number(2358, [1, 4, 5, 8], is_upper=True) == 4111
    assert get_closest_number(2358, [0], is_upper=True) is None
    assert get_closest_number(80879, [0, 1, 2, 3, 5], is_upper=True) == 100000
    assert get_closest_number(1, [6, 7], is_upper=True) == 6


def test_get_closest_number_with_lower():
    assert get_closest_number(3792, [1, 3, 5, 8], is_upper=False) == 3588
    assert get_closest_number(3792, [4, 5, 6, 8], is_upper=False) == 888
    assert get_closest_number(1358, [1, 3, 5, 8], is_upper=False) == 1358
    assert get_closest_number(1356, [1, 3, 5, 8], is_upper=False) == 1355
    assert get_closest_number(2358, [0], is_upper=False) == 0
    assert get_closest_number(1, [6, 7], is_upper=False) is None
