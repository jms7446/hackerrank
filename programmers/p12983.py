import sys
from collections import defaultdict

sys.setrecursionlimit(1000000)


def str_findall(ptn, s):
    idx = s.find(ptn)
    while idx != -1:
        yield idx
        idx = s.find(ptn, idx + 1)


def solution(strs, t):
    match_map = defaultdict(list)
    for s in strs:
        for start in str_findall(s, t):
            match_map[start].append(start + len(s))

    memory = [None] * len(t)

    def loop(idx):
        if idx == len(t):
            return 0
        if memory[idx] is not None:
            return memory[idx]

        res = -1
        if idx in match_map:
            counts = [loop(end) for end in match_map[idx]]
            valid_counts = [c for c in counts if c >= 0]
            if valid_counts:
                res = 1 + min(valid_counts)
            else:
                res = -1
        else:
            res = -1

        memory[idx] = res
        return res
    return loop(0)


def test1():
    assert solution(["ab", "na", "n", "a", "bn"], "nabnabn") == 4
    assert solution(["ba", "na", "n", "a"], "banana") == 3
    assert solution(["app", "ap", "p", "l", "e", "ple", "pp"], "apple") == 2
    assert solution(["ba", "an", "nan", "ban", "n"], "banana") == -1
