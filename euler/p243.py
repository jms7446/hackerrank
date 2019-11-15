import sys


def main():
    num_lines = int(sys.stdin.readline())
    for _ in range(num_lines):
        line = sys.stdin.readline()
        a, b = [int(x) for x in line.split()]
        print(calc_resilience(a, b))


################################################################################
# logic
################################################################################

class NotFoundException(Exception):
    """Can not find number"""


def calc_resilience(a, b):
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
    assert calc_resilience(1, 1) == 4
    assert calc_resilience(4, 10) == 12


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


if __name__ == '__main__':
    main()
