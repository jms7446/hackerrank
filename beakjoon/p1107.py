
import sys


INIT_CHANNEL = 100


def digits_to_number(digits):
    number = 0
    for d in digits:
        number = number * 10 + d
    return number


def calc_button_count_by_number(target, number):
    return len(str(number)) + abs(target - number)


def get_closest_number(target, valid_buttons, is_upper):
    exact_flag = True
    suffix = min(valid_buttons) if is_upper else max(valid_buttons)
    digits = []
    for s in str(target):
        if exact_flag:
            d = int(s)
            if d in valid_buttons:
                digits.append(d)
            else:
                if is_upper:
                    closest = min(x for x in valid_buttons if x > d)
                else:
                    closest = max(x for x in valid_buttons if x < d)
                digits.append(closest)
                exact_flag = False
        else:
            digits.append(suffix)
    return digits_to_number(digits)


def calc_count_with_same_order(target, valid_buttons):
    candidates = [
        get_closest_number(target, valid_buttons, is_upper=True),
        get_closest_number(target, valid_buttons, is_upper=False),
    ]
    print(target, candidates, valid_buttons, file=sys.stderr)
    return min(calc_button_count_by_number(target, number) for number in candidates)


def calc_count_with_high_order(target, valid_buttons):
    head = min(i for i in valid_buttons if i > 0)
    tail = min(valid_buttons)
    closest_digits = [head] + [tail] * len(str(target))
    closest_number = digits_to_number(closest_digits)
    return calc_button_count_by_number(target, closest_number)


def calc_count_with_low_order(target, valid_buttons):
    closest_digits = [max(valid_buttons)] * len(str(target))
    closest_number = digits_to_number(closest_digits)
    return calc_button_count_by_number(target, closest_number)


def calc_count_with_up_down(target):
    return abs(target - INIT_CHANNEL)


def solve(target, broken_buttons):
    valid_buttons = [i for i in range(10) if i not in broken_buttons]
    results = [
        calc_count_with_same_order(target, valid_buttons),
        calc_count_with_high_order(target, valid_buttons),
        calc_count_with_low_order(target, valid_buttons),
        calc_count_with_up_down(target),
    ]
    return min(results)


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
])
def test_main(in_str, expected):
    assert get_output_with_stdin(main, in_str.strip()) == expected
