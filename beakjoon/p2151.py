import sys
from dataclasses import dataclass, field
import enum
from typing import List
from copy import deepcopy
from collections import deque


@dataclass(frozen=True)
class Point:
    x: int = 0
    y: int = 0

    def __add__(self, other):
        return Point(self.x + other.x, self.y + other.y)

    def __neg__(self):
        return Point(-self.x, -self.y)

    def __sub__(self, other):
        return Point(self.x - other.x, self.y - other.y)


class Direction(Point):
    pass


################################################################################


class Status(enum.Enum):
    SUCCESS = enum.auto()
    BRANCH = enum.auto()
    TERMINATE = enum.auto()


class Mirror(enum.Enum):
    UpperLeft = enum.auto()
    UpperRight = enum.auto()


east, south, west, north = (Direction(1, 0), Direction(0, 1), Direction(-1, 0), Direction(0, -1))
DIRECTIONS = [east, south, west, north]
MIRRORS = [Mirror.UpperLeft, Mirror.UpperRight]

REFLECTION = {
    Mirror.UpperLeft: {
        east: south,
        south: east,
        west: north,
        north: west,
    },
    Mirror.UpperRight: {
        east: north,
        south: west,
        west: south,
        north: east,
    }
}


def reflect(direction: Direction, mirror: Mirror) -> Direction:
    return REFLECTION[mirror][direction]


@dataclass
class ProceedInfo:
    location: Point
    direction: Direction

    def copy(self, location=None, direction=None):
        copied = deepcopy(self)
        if location is not None:
            copied.location = location
        if direction is not None:
            copied.direction = direction
        return copied


class HouseMap:
    def __init__(self, s_list):
        self.s_list = s_list
        self.N = len(s_list)

    def get(self, point):
        if 0 <= point.x < self.N and 0 <= point.y < self.N:
            return self.s_list[point.y][point.x]
        else:
            return None

    def __len__(self):
        return len(self.s_list)

    def find(self, mark) -> List[Point]:
        return [Point(x, y) for y, s in enumerate(self.s_list) for x, c in enumerate(s) if c == mark]


class Solver:
    def __init__(self, s_list):
        self.hmap = HouseMap(s_list)
        self.visited = set()
        self.start, self.target = self.hmap.find("#")

    def solve(self):
        que = deque([ProceedInfo(self.start, direction) for direction in DIRECTIONS])
        mirror_count = 0
        while que:
            q_count = len(que)
            for _ in range(q_count):
                p = que.popleft()
                while True:
                    p.location += p.direction
                    mark = self.hmap.get(p.location)
                    if mark is None or mark == "*":
                        break
                    elif mark == "!":
                        if p.location in self.visited:
                            break
                        self.visited.add(p.location)
                        for mirror in MIRRORS:
                            que.append(p.copy(direction=reflect(p.direction, mirror)))
                    elif mark == "#" and p.location == self.target:
                        return mirror_count
            mirror_count += 1
        return -1


def main():
    stdin = sys.stdin
    _ = stdin.readline()
    s_list = [line.strip() for line in stdin.readlines()]
    print(Solver(s_list).solve())


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


def test_solver():
    import random
    import time
    from beakjoon.p2151_short import solve

    def gen_map(n):
        def gen_tile():
            r = random.random()
            if r < 0.3:
                return "*"
            elif r < 0.7:
                return "."
            else:
                return "!"
        c_lists = [[gen_tile() for _ in range(n)] for _ in range(n)]
        sharp_set = set()
        while True:
            x, y = random.randint(0, n - 1), random.randint(0, n - 1)
            c_lists[y][x] = "#"
            sharp_set.add((x, y))
            if len(sharp_set) == 2:
                break
        return ["".join(cs) for cs in c_lists]

    for _ in range(100000):
        s_list = gen_map(10)
        solver = Solver(s_list)
        r1 = solver.solve()
        r2 = solve(s_list)
        if r1 != r2:
            print(f"r1: {r1}, r2: {r2}")
            print("\n".join(s_list), file=sys.stderr)
            assert False
