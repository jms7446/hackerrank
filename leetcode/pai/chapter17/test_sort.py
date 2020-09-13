import random
import pytest
from util import *

from .sort import *


@pytest.mark.parametrize(['sort_alg'], [
    (quick_sorted, ),
])
def test_random(sort_alg):
    num_cases = 100
    for _ in range(num_cases):
        xs = [random.randint(-9, 9) for _ in range(10)]
        try:
            assert sort_alg(xs) == sorted(xs)
        except Exception as e:
            eprint(xs, '\nfailed with\n', e)
            assert False


@pytest.mark.parametrize(['in_'], [
    ([5, 1, 3, 4, 2], ),
    ([-2, 1, 2, 0, -2], ),
])
def test_found(in_):
    assert quick_sorted(in_) == sorted(in_)
