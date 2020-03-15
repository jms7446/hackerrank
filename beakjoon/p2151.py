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
    mirrors: dict = field(default_factory=dict)


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
        i = 0
        while que:
            # print("               start while", len(que), file=sys.stderr)
            p = que.popleft()
            status = self._proceed(p)
            if status == Status.TERMINATE:
                # print("terminate", file=sys.stderr)
                pass
            elif status == Status.BRANCH:
                for mirror in MIRRORS:
                    new_p = deepcopy(p)
                    new_p.mirrors[new_p.location] = mirror
                    new_p.direction = reflect(new_p.direction, mirror)
                    que.append(new_p)
                    # print("create branch in que", file=sys.stderr)
                que.appendleft(p)
            elif status == Status.SUCCESS:
                return len(p.mirrors)
        return -1

    def _proceed(self, p):
        while True:
            p.location += p.direction

            visited_key = (p.location, p.direction)
            if visited_key in self.visited:
                return Status.TERMINATE
            self.visited.add(visited_key)

            mark = self.hmap.get(p.location)
            # print(mark, p, file=sys.stderr)
            if mark is None or mark == "*":
                # print("terminate", file=sys.stderr)
                return Status.TERMINATE
            elif mark == "!":
                if p.location in p.mirrors:
                    p.direction = reflect(p.direction, p.mirrors[p.location])
                    return Status.TERMINATE     # FIXME
                else:
                    return Status.BRANCH
            elif mark == "#" and p.location == self.target:
                return Status.SUCCESS


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

    def gen_map(n):
        def gen_tile():
            r = random.random()
            if r < 0.3:
                return "*"
            elif r < 0.8:
                return "."
            else:
                return "!"
        c_lists = [[gen_tile() for _ in range(n)] for _ in range(n)]
        for _ in range(2):
            x, y = random.randint(0, n - 1), random.randint(0, n - 1)
            c_lists[y][x] = "#"
        return ["".join(cs) for cs in c_lists]

    for _ in range(100000):
        st = time.time()
        s_list = gen_map(50)
        try:
            solver = Solver(s_list)
            solver.solve()
        except Exception as ex:
            pass
            # print(ex)
            # print("\n".join(s_list), file=sys.stderr)
            # assert False
        et = time.time() - st
        if et > 0.1:
            print("elapse time: ", et, file=sys.stderr)
            print("\n".join(s_list), file=sys.stderr)
            assert False
