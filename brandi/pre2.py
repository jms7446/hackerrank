import sys

N_NEEDED = 5
M_NEEDED = 7


def solve(N, M):
    # 5:7 ratio
    n = N // N_NEEDED
    m = M // M_NEEDED
    if n <= m:
        return n
    else:
        left_n = N - m * N_NEEDED
        left_m = M - m * M_NEEDED
        added = (left_n + left_m) // (N_NEEDED + M_NEEDED)
        return m + added


def main():
    stdin = sys.stdin
    t = int(stdin.readline())
    for _ in range(t):
        N, M = [int(x) for x in stdin.readline().split()]
        print(solve(N, M))


if __name__ == '__main__':
    main()


from util.result_check import get_output_with_stdin


def test_main(in_str, out_str):
    in_str = '''
4
12 0
10 14
4 20
5 2147483648    
    '''
    out_str = '''
1
2
0
1
    '''
    assert get_output_with_stdin(main, in_str) == out_str
