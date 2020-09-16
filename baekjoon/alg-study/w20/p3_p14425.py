import sys


def solve(ptns, texts):
    ptns = set(ptns)
    return sum(text in ptns for text in texts)


def main():
    stdin = sys.stdin
    n, m = [int(x) for x in stdin.readline().split()]
    ptns = [stdin.readline().strip() for _ in range(n)]
    texts = [stdin.readline().strip() for _ in range(m)]
    print(solve(ptns, texts))


if __name__ == "__main__":
    main()

from util import *
import pytest


def test_main():
    in_str = """

    """.strip()
    out_str = """

    """.strip()
    assert mock_io(main)(in_str) == out_str


@pytest.mark.parametrize(('in_str', 'out_str'), [
    ('''
5 11
baekjoononlinejudge
startlink
codeplus
sundaycoding
codingsh
baekjoon
codeplus
codeminus
startlink
starlink
sundaycoding
codingsh
codinghs
sondaycoding
startrink
icerink
    '''.strip(), '4'.strip()),
])
def test_main(in_str, out_str):
    assert mock_io(main)(in_str) == out_str
