import operator as op
from functools import reduce


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


def ncr(n, r):
    r = min(r, n-r)
    numer = reduce(op.mul, range(n, n-r, -1), 1)
    denom = reduce(op.mul, range(1, r+1), 1)
    return numer // denom


def iter_primes(max_value, begin=None):
    is_primes = [True] * (max_value + 1)
    is_primes[0] = is_primes[1] = False
    for i in range(2, (max_value + 1) // 2):
        if is_primes[i]:
            j = 2 * i
            while j <= max_value:
                is_primes[j] = False
                j += i
    if begin is None:
        return (i for i, is_prime in enumerate(is_primes) if is_prime)
    else:
        return (i for i, is_prime in enumerate(is_primes) if is_prime and i >= begin)
