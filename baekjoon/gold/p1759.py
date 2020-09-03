import sys

VOWELS = {'a', 'e', 'i', 'o', 'u'}


def solve(L, C, cs):
    def loop(cur_str, idx, v_count, c_count):
        if len(cur_str) == L:
            if v_count >= 1 and c_count >= 2:
                results.append(cur_str)
            return
        elif idx >= len(cs):
            return

        c = cs[idx]
        if c in VOWELS:
            loop(cur_str + c, idx + 1, v_count + 1, c_count)
        else:
            loop(cur_str + c, idx + 1, v_count, c_count + 1)
        loop(cur_str, idx + 1, v_count, c_count)

    cs = sorted(cs)
    results = []
    loop('', 0, 0, 0)
    return results


def main():
    stdin = sys.stdin
    L, C = [int(x) for x in stdin.readline().split()]
    cs = [x for x in stdin.readline().split()]
    for res in solve(L, C, cs):
        print(res)


if __name__ == "__main__":
    main()


from util import *


def test_main():
    in_str = """
4 6
a t c i s w
    """.strip()
    out_str = """
acis
acit
aciw
acst
acsw
actw
aist
aisw
aitw
astw
cist
cisw
citw
istw
    """.strip()
    assert mock_io(main)(in_str) == out_str


def test_add():
    in_str = """
4 5
a b c d f
    """.strip()
    out_str = """
abcd
abcf
abdf
acdf
    """.strip()
    assert mock_io(main)(in_str) == out_str
