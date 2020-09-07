# 성곽

import sys


class Map:
    directions = ((0, -1), (-1, 0), (0, 1), (1, 0))
    walls = (1, 2, 4, 8)

    def __init__(self, tiles, num_rows, num_cols):
        self.tiles = tiles
        self.num_rows = num_rows
        self.num_cols = num_cols

    def _get_direction_pair(self, room):
        opened = []
        blocked = []
        for i, wall in enumerate(self.walls):
            direction = self.directions[i]
            if room & wall:
                blocked.append(direction)
            else:
                opened.append(direction)
        return opened, blocked

    def is_valid(self, r, c):
        return 0 <= r < self.num_rows and 0 <= c < self.num_cols

    def get_near_pos_pair(self, pos):
        r, c = pos
        opened, blocked = self._get_direction_pair(self.tiles[r][c])
        return [[(r + dr, c + dc) for dr, dc in directions if self.is_valid(r + dr, c + dc)]
                for directions in [opened, blocked]]


def solve(R, C, G):
    start = (0, 0)
    house = Map(G, R, C)
    room_labels = [[-1] * C for _ in range(R)]
    connected = set()

    room_sizes = []
    room_stack = [start]
    while True:
        if not room_stack:
            break
        r, c = room_stack.pop()
        if room_labels[r][c] > -1:
            continue
        room_idx = len(room_sizes)
        room_labels[r][c] = room_idx
        room_sizes.append(1)
        stack = [(r, c)]
        while stack:
            pos = stack.pop()
            opened, blocked = house.get_near_pos_pair(pos)
            for r, c in opened:
                near_room_idx = room_labels[r][c]
                if near_room_idx == -1:
                    room_labels[r][c] = room_idx
                    room_sizes[room_idx] += 1
                    stack.append((r, c))
            for r, c in blocked:
                near_room_idx = room_labels[r][c]
                if near_room_idx == -1:
                    room_stack.append((r, c))
                elif room_idx != near_room_idx:
                    connected.add((room_idx, near_room_idx))
    num_rooms = len(room_sizes)
    max_room_size = max(room_sizes)
    max_merged_room_size = max(room_sizes[r1] + room_sizes[r2] for r1, r2 in connected)
    return num_rooms, max_room_size, max_merged_room_size


def main():
    stdin = sys.stdin
    C, R = [int(x) for x in stdin.readline().split()]
    G = [[int(x) for x in stdin.readline().split()] for _ in range(R)]
    res = solve(R, C, G)
    print('\n'.join(str(x) for x in res))


if __name__ == "__main__":
    main()


from util import *


def test_main():
    in_str = """
7 4
11 6 11 6 3 10 6
7 9 6 13 5 15 5
1 10 12 7 13 7 5
13 11 10 8 10 12 13
    """.strip()
    out_str = """
5
9
16
    """.strip()
    assert mock_io(main)(in_str) == out_str
