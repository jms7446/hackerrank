import sys
import heapq


def str_findall(ptn, s):
    idx = s.find(ptn)
    while idx != -1:
        yield idx
        idx = s.find(ptn, idx + 1)


def str_findall_2str(ptn1, ptn2, s):
    xs1 = ((idx, ptn1) for idx in str_findall(ptn1, s))
    xs2 = ((idx, ptn2) for idx in str_findall(ptn2, s))
    return heapq.merge(xs1, xs2)


def count_cases_old(s):
    FL, TL = '((', '))'
    xc, yc, count = 0, 0, 0
    for _, m in str_findall_2str(FL, TL, s):
        if m == FL:
            xc += 1
            count -= yc
        else:
            yc += 1
    count += xc * yc
    return count


def count_cases(s):
    xc, yc, count = 0, 0, 0
    for c1, c2 in zip(s, s[1:]):
        if c1 != c2:
            continue
        if c1 == '(':
            xc += 1
            count -= yc
        else:
            yc += 1
    count += xc * yc
    return count


def main():
    stdin = sys.stdin
    s = stdin.readline().strip()
    print(count_cases(s))


if __name__ == '__main__':
    main()


from util.result_check import get_output_with_stdin


def test_main():
    in_str = '''
)((()())())
    '''.strip()

    out_str = '''
4
'''.strip()
    assert get_output_with_stdin(main, in_str) == out_str
