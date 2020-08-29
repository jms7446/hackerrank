import sys


def classify(max_rate, bit_rate):
    rate = bit_rate / max_rate * 100
    if rate >= 90:
        return 0
    elif rate >= 80:
        return 1
    elif rate >= 75:
        return 2
    elif rate >= 68:
        return 3
    elif rate >= 60:
        return 4
    else:
        return 5


def calc_max_bit_rate(age):
    return 220 - age


def solve(age, xs):
    result = [0] * 6
    max_bit_rate = calc_max_bit_rate(age)
    for x in xs:
        result[classify(max_bit_rate, x)] += 1
    return result


def main():
    stdin = sys.stdin
    age = int(stdin.readline().strip())
    xs = [int(line) for line in stdin.readlines()]
    print(' '.join(str(x) for x in solve(age, xs)))


if __name__ == '__main__':
    main()


from util.result_check import get_output_with_stdin


def test_main():
    in_str = '''
30
50
55
60
65
70
75
80
85
90
95
100
105
110
115
120
125
130
135
140
145
150
155
160
165
170
175
180
185
    '''.strip()
    out_str = '''
3 4 2 3 3 13
    '''.strip()
    assert get_output_with_stdin(main, in_str) == out_str
