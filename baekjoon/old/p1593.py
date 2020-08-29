import sys
from collections import Counter


def solve_simple(W, S):
    if len(W) > len(S):
        return 0

    found = 0
    counts = Counter(W)
    for s in S[:len(W)]:
        if s in counts:
            counts[s] -= 1
    if not any(counts.values()):
        found += 1
    for p, c in zip(S, S[len(W):]):
        if p in counts:
            counts[p] += 1
        if c in counts:
            counts[c] -= 1
        if not any(counts.values()):
            found += 1
    return found


def solve(W, S):
    result_count = 0
    alphabet_width = (ord('z') - ord('A') + 1)
    w_counter = [0] * alphabet_width
    w_checker = [False] * alphabet_width
    b = ord('A')
    for w in W:
        i = ord(w) - b
        w_counter[i] += 1
        w_checker[i] = True

    nw_count = 0
    w_ok_remain = sum(w_checker)
    for s in S[:len(W)]:
        i = ord(s) - b
        if w_checker[i]:
            w_counter[i] -= 1
            if w_counter[i] == 0:
                w_ok_remain -= 1
            elif w_counter[i] == -1:
                w_ok_remain += 1
        else:
            nw_count += 1
    if nw_count == 0 and w_ok_remain == 0:
        result_count += 1

    for p, c in zip(S, S[len(W):]):
        # for p
        i = ord(p) - b
        if w_checker[i]:
            w_counter[i] += 1
            if w_counter[i] == 0:
                w_ok_remain -= 1
            elif w_counter[i] == 1:
                w_ok_remain += 1
        else:
            nw_count -= 1

        # for c
        i = ord(c) - b
        if w_checker[i]:
            w_counter[i] -= 1
            if w_counter[i] == 0:
                w_ok_remain -= 1
            elif w_counter[i] == -1:
                w_ok_remain += 1
        else:
            nw_count += 1

        if nw_count == 0 and w_ok_remain == 0:
            result_count += 1

    return result_count


def main():
    stdin = sys.stdin
    _ = [int(x) for x in stdin.readline().split()]
    W = stdin.readline().strip()
    S = stdin.readline().strip()
    print(solve(W, S))


if __name__ == "__main__":
    main()


from util.result_check import get_output_with_stdin


def test_main():
    in_str = """
4 11
cAda
AbrAcadAbRa
""".strip()
    assert get_output_with_stdin(main, in_str) == "2"


def test_solve():
    W = "abad"
    S = "abadab"
    print(solve(W, S))


def gen(N, M, seed=None):
    import string
    import random
    random.seed(seed)
    W = "".join(random.choices(string.ascii_letters, k=N))
    S = "".join(random.choices(string.ascii_letters, k=M))
    return W, S


# if __name__ == "__main__":
#     iter_run(solve, loop=10, gen=lambda: gen(2000, 2000000, seed=2))
