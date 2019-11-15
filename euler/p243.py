"""
제대로 된 해를 찾지 못함.
휴리스틱한 가정을 세우고 풀었으나, 그 가정이 맞지 않은 듯.
"""

import sys
from functools import reduce


def main():
    num_lines = int(sys.stdin.readline())
    for _ in range(num_lines):
        line = sys.stdin.readline()
        a, b = [int(x) for x in line.split()]
        print(calc_resilience(a, b))


################################################################################
# logic
################################################################################

PRIMES = [2, 3, 5, 7, 11, 13]


def calc_resilience(a, b):
    q = a / b
    combinations = make_combinations(100000)
    combinations.sort(key=product_prime)

    for combination in combinations:
        value = product_prime(combination)
        co_div_numbers = get_co_div_numbers(value, combination)
        r = (value - 1 - len(co_div_numbers)) / (value - 1)
        if r < q:
            return value


def get_co_div_numbers(value, comb):
    def loop(nc, idx, cur_prod):
        num = cur_prod * PRIMES[idx]
        if num >= value:
            return
        if num in numbers:
            return
        numbers.add(num)
        nc[idx] += 1
        for i in range(len(PRIMES)):
            loop(nc.copy(), i, num)

    numbers = set()
    for idx, c in enumerate(comb):
        if c > 0:
            num_comb = [0] * len(PRIMES)
            loop(num_comb, idx, 1)
    return numbers


def make_combinations(upper_bound):
    def _make_combinations(cur_comb, idx):
        if idx >= len(PRIMES):
            return
        if idx > 0 and cur_comb[idx] >= cur_comb[idx - 1]:
            return
        cur_comb = cur_comb.copy()
        cur_comb[idx] += 1
        if product_prime(cur_comb) > upper_bound:
            return
        acc.add(tuple(cur_comb))

        _make_combinations(cur_comb, idx)
        _make_combinations(cur_comb, idx + 1)

    acc = set()
    _make_combinations([0, 0, 0, 0, 0, 0], 0)
    return list(acc)


def product_prime(comb):
    numbers = [p ** c for c, p in zip(comb, PRIMES)]
    return reduce(lambda x, y: x * y, numbers)


################################################################################
# tests
################################################################################

def test_calc_resilience():
    assert calc_resilience(1, 1) == 4
    assert calc_resilience(4, 10) == 12


def test_product_prime():
    assert product_prime([1, 0, 1]) == 10


def test_get_co_div_numbers():
    assert get_co_div_numbers(6, [1, 1, 0, 0, 0, 0]) == {2, 3, 4}
    assert get_co_div_numbers(12, [2, 1, 0, 0, 0, 0]) == {2, 3, 4, 6, 8, 9, 10}


def test_make_combinations():
    assert make_combinations(2) == {(1, 0, 0, 0, 0, 0)}
    assert make_combinations(3) == {(1, 0, 0, 0, 0, 0)}
    assert make_combinations(4) == {(1, 0, 0, 0, 0, 0), (2, 0, 0, 0, 0, 0)}
    assert make_combinations(10) == {(1, 0, 0, 0, 0, 0), (2, 0, 0, 0, 0, 0), (3, 0, 0, 0, 0, 0), (1, 1, 0, 0, 0, 0)}
    print(len(make_combinations(100000)))


if __name__ == '__main__':
    main()
