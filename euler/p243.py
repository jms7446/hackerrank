
import pytest

FACTOR = 3
INIT_SIZE = 1000


class NotFoundException(Exception):
    """Can not find number"""


def calc_resilience(a: int, b: int) -> int:
    q = a / b
    limit = INIT_SIZE
    while True:
        try:
            solution = calc_resilience_until(q, limit)
        except NotFoundException:
            continue
        else:
            return solution


def calc_resilience_until(q: float, limit: int) -> int:
    """raise NotFoundException when cannot find solution"""
    num_divisors = [0] * limit
    for i in range(2, limit):
        num_proper_factions = (i - 1)
        resilience = (num_proper_factions - num_divisors[i]) / num_proper_factions
        if resilience < q:
            return i
        else:
            update_num_divisors(num_divisors, i)
    raise NotFoundException


def update_num_divisors(num_divisors, x):
    i = x + x
    while i < len(num_divisors):
        num_divisors[i] += 1
        i += x


def calc_resilience_naive(a, b):
    q = a / b
    for d in range(2, 100000):
        num_proper_fractions = d - 1
        resilience = (num_proper_fractions - find_has_gcd_num_count(d)) / num_proper_fractions
        if resilience < q:
            return d
    raise NotFoundException()


def find_has_gcd_num_count(d):
    return len([n for n in range(2, d) if gcd(d, n) > 1])


def gcd(a, b):
    if a < b:
        b, a = (a, b)
    if b == 0:
        return a
    else:
        return gcd(b, a % b)


################################################################################
# tests
################################################################################

def test_calc_resilience():
    assert calc_resilience(4, 10) == 12
    assert calc_resilience(1, 1) == 4


@pytest.mark.parametrize(('before', 'x', 'after'), [
    ([0, 0, 0, 0, 0], 2, [0, 0, 0, 0, 1]),
    ([0, 0, 0, 0, 0, 0, 0], 2, [0, 0, 0, 0, 1, 0, 1]),
    ([0, 0, 1, 1, 1, 1, 1, 1], 3, [0, 0, 1, 1, 1, 1, 2, 1]),
])
def test_update_num_divisors(before, x, after):
    update_num_divisors(before, x)
    assert before == after


def test_gcd():
    assert gcd(6, 4) == 2
    assert gcd(4, 6) == 2
    assert gcd(1, 2) == 1
    assert gcd(5, 12) == 1


def test_find_has_gcd_num_count():
    assert find_has_gcd_num_count(2) == 0
    assert find_has_gcd_num_count(3) == 0
    assert find_has_gcd_num_count(4) == 1
    assert find_has_gcd_num_count(6) == 3
    assert find_has_gcd_num_count(12) == 7


def test_calc_resilience_naive():
    assert calc_resilience_naive(1, 1) == 4
    assert calc_resilience_naive(4, 10) == 12
