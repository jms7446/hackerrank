# 접두사 찾기
import sys
from bisect import bisect_left


def solve_naive(corpus, texts):
    prefix_set = set()
    for ptn in corpus:
        for i in range(len(ptn)):
            prefix_set.add(ptn[:i+1])
    return sum(text in prefix_set for text in texts)


def solve_bisect(corpus, texts):
    corpus = sorted(corpus)
    count = 0
    for text in texts:
        idx = bisect_left(corpus, text)
        if idx < len(corpus) and corpus[idx].startswith(text):
            count += 1
    return count


def solve(corpus, texts):
    all_texts = sorted(corpus + texts)
    texts = set(texts)
    count = 0
    for i in range(len(all_texts)-1):
        text = all_texts[i]
        ptn = all_texts[i+1]
        if ptn.startswith(text) and text in texts:
            count += 1
    return count


def main():
    stdin = sys.stdin
    N, M = [int(x) for x in stdin.readline().split()]
    corpus = [stdin.readline().strip() for _ in range(N)]
    texts = [stdin.readline().strip() for _ in range(M)]
    print(solve(corpus, texts))


if __name__ == "__main__":
    main()

from util import *
import pytest


@pytest.mark.parametrize(('in_str', 'out_str'), [
    ('''
5 10
baekjoononlinejudge
startlink
codeplus
sundaycoding
codingsh
baekjoon
star
start
code
sunday
coding
cod
online
judge
plus
    '''.strip(),
     '''
7
     '''.strip()),
])
def test_main(in_str, out_str):
    assert mock_io(main)(in_str) == out_str
