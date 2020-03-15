import sys
from collections import deque


directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]
reflects = [(1, 3), (0, 2), (1, 3), (0, 2)]


def solve(hmap):
    N = len(hmap)
    visited = set()     # only '!' can change direction, so checking whether visited is performed only here.
    start, target = [(x, y) for y, row in enumerate(hmap) for x, c in enumerate(row) if c == "#"]
    que = deque([(start[0], start[1], d) for d in range(len(directions))])
    mirror_count = 0
    while que:
        for _ in range(len(que)):
            x, y, d = que.popleft()
            dx, dy = directions[d]
            while True:
                x, y = x + dx, y + dy
                if (x, y) == target:
                    return mirror_count

                if not (0 <= x < N and 0 <= y < N):
                    break
                mark = hmap[y][x]
                if mark == "*":
                    break
                elif mark == "!":
                    if (x, y) in visited:
                        break
                    visited.add((x, y))
                    que.extend([(x, y, new_d) for new_d in reflects[d]])
        mirror_count += 1
    return -1


def main():
    stdin = sys.stdin
    _ = stdin.readline()
    s_list = [line.strip() for line in stdin.readlines()]
    print(solve(s_list))


if __name__ == "__main__":
    main()


from util.result_check import get_output_with_stdin


def test_main():
    in_str = """
5
***#*
*.!.*
*!.!*
*.!.*
*#***
""".strip()
    assert get_output_with_stdin(main, in_str) == "2"
