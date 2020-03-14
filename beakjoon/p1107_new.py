
import sys
from bisect import bisect_left

INIT_CHANNEL = 100


def number_to_digits(num, base=10, length=None):
    digits = []
    while num > 0:
        digits.append(num % base)
        num //= base
    if length is not None:
        padding = [0] * (length - len(digits))
        digits += padding

    return list(reversed(digits))


def digits_to_number(digits, base=10):
    num = 0
    for digit in digits:
        num = num * base + digit
    return num


class PossibleNumbers:
    def __init__(self, digits, n):
        assert digits
        self.digits = sorted(digits)
        self.n = n
        self._base = len(digits)

    def __len__(self):
        return self._base ** self.n

    def __getitem__(self, idx):
        idx_of_digits = number_to_digits(idx, base=self._base, length=self.n)
        return digits_to_number([self.digits[d] for d in idx_of_digits])

    def upper(self):
        if self.digits[0] == 0:
            if len(self.digits) == 1:
                return 0
            else:
                return digits_to_number([self.digits[1]] + [self.digits[0]] * self.n)
        else:
            return digits_to_number([self.digits[0]] * (self.n + 1))

    def lower(self):
        if self.n == 1:
            return self.digits[0]
        else:
            return digits_to_number([self.digits[-1]] * (self.n - 1))


def calc_count_without_digits(target):
    return abs(target - INIT_CHANNEL)


def calc_count_with_digits(target, valid_digits):
    def calc_button_count_by_number(number):
        return len(str(number)) + abs(target - number)

    possible_numbers = PossibleNumbers(valid_digits, len(str(target)))
    idx = bisect_left(possible_numbers, target)
    if idx == len(possible_numbers):
        candidates = [possible_numbers.upper(), possible_numbers[idx-1]]
    elif idx == 0:
        candidates = [possible_numbers[idx], possible_numbers.lower()]
    else:
        candidates = [possible_numbers[idx], possible_numbers[idx-1]]
    return min(calc_button_count_by_number(number) for number in candidates)


def solve(target, broken_buttons):
    valid_digits = sorted([i for i in range(10) if i not in broken_buttons])
    if valid_digits:
        return min(calc_count_without_digits(target), calc_count_with_digits(target, valid_digits))
    else:
        return calc_count_without_digits(target)


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


def test_PossibleNumbers():
    pn = PossibleNumbers([1, 3, 4], 2)
    assert len(pn) == 9
    assert pn[0] == 11
    assert pn.lower() == 4
    assert pn.upper() == 111


def test_PossibleNumbers_lower_upper():
    pn = PossibleNumbers([8, 9], 4)
    assert pn.lower() == 999
    assert pn.upper() == 88888


def test_PossibleNumbers_upper_with_zero():
    assert PossibleNumbers([0, 8, 9], 4).upper() == 80000
    assert PossibleNumbers([0], 4).upper() == 0


def test_solve():
    target = 1000
    valid_digits = [0, 1, 2, 3, 4, 5, 6, 7]
    assert solve(target, valid_digits) == 4


def test_find_for_bug():
    from beakjoon.p1107 import solve as comp_solve
    import random
    for _ in range(1000):
        target = random.randint(0, 1000)
        valid_digits = [d for d in range(10) if random.random() < 0.5]
        my = solve(target, valid_digits)
        comp = comp_solve(target, valid_digits)
        if my != comp:
            print(f"my: {my}, comp: {comp}, target: {target}, valid_digits: {valid_digits}", file=sys.stderr)
            assert False
