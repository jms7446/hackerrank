
from collections.abc import Iterable
import random


def list_to_string(ints):
    return ' '.join(str(i) for i in ints)


def merge_to_lines(args):
    def to_string(x):
        if isinstance(x, str):
            line = x
        elif isinstance(x, Iterable):
            line = list_to_string(x)
        else:
            line = str(x)
        return line

    return '\n'.join([to_string(arg) for arg in args])


def random_choices(xs, k=None):
    k = k or len(xs)
    xs = list(xs)
    random.shuffle(xs)
    return xs[:k]


def generate_probs(func, args=None, count=1, random_state=None):
    """generate input strings by func

    example of func:
    def make_probs(LR=19, NR=20, XR=6):
        L, W, H = [2 ** randint(1, LR) for _ in range(3)]
        N = randint(1, NR)
        X = [(randint(0, 19), randint(0, 10**XR)) for _ in range(N)]
        return merge_to_lines([
            [L, W, H],
            N,
            merge_to_lines(X),
        ])
    """
    args = args or []

    if random_state:
        random.seed(random_state)

    for _ in range(count):
        yield func(*args)

