import sys


def str_findall(c, s):
    idx = s.find(c)
    while idx != -1:
        yield idx
        idx = s.find(c, idx + 1)


def iter_pair_in_order(xs, ys):
    for x in xs:
        for y in ys:
            if x < y:
                yield x, y


def is_possible_board(name, board):
    c1_indices = list(str_findall(name[0], board))
    c2_indices = list(str_findall(name[1], board))
    for (c1, c2) in iter_pair_in_order(c1_indices, c2_indices):
        gap = c2 - c1
        if board[c1::gap].startswith(name):
            return True
    return False


def main():
    stdin = sys.stdin
    _ = int(stdin.readline())
    name = stdin.readline().strip()
    boards = [line.strip() for line in stdin.readlines()]
    num_possible_board = sum(is_possible_board(name, board) for board in boards)
    print(num_possible_board)


if __name__ == '__main__':
    main()


from util.result_check import get_output_with_stdin


def test_main():
    in_str = '''
4
bar
abracadabra
bear
bar
baraxbara
    '''.strip()

    out_str = '''
3
'''.strip()
    assert get_output_with_stdin(main, in_str) == out_str
