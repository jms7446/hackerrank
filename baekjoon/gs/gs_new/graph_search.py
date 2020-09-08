from abc import abstractmethod, ABC
from dataclasses import dataclass
from typing import Iterable, Tuple, List
from numbers import Real
from itertools import count


@dataclass(frozen=True)
class Point:
    row: int
    col: int

    def __add__(self, other):
        return Point(self.row + other.row, self.col + other.col)


EAST = Point(0, 1)
WEST = Point(0, -1)
SOUTH = Point(1, 0)
NORTH = Point(-1, 0)
BASE_MOVES = (EAST, WEST, SOUTH, NORTH)


class Map:
    def __init__(self, num_rows, num_cols, moves=None):
        self.num_rows = num_rows
        self.num_cols = num_cols
        self.moves = moves or BASE_MOVES

    def is_valid_point(self, point: Point) -> bool:
        return 0 <= point.row < self.num_rows and 0 <= point.col < self.num_cols

    def nexts(self, point: Point):
        for move in self.moves:
            next_point = point + move
            if self.is_valid_point(next_point):
                yield next_point

    def nexts_with_cost(self, point: Point) -> Iterable[Tuple[Point, Real]]:
        return ((p, 0) for p in self.nexts(point))


class TileMap(Map):
    def __init__(self, tiles, moves=None, invalid_tiles=None):
        # we assume that all column lengths are equal.
        super().__init__(len(tiles), len(tiles[0]), moves=moves)
        self.tiles = tiles
        self.invalid_tiles = invalid_tiles or set()

    @classmethod
    def from_str(cls, in_str, *args, **kwargs):
        tiles = tuple([tuple(line.split()) for line in in_str.strip().split('\n')])
        return cls(tiles, *args, **kwargs)

    def __getitem__(self, point: Point):
        return self.tiles[point.row][point.col]

    def is_valid_point(self, point: Point) -> bool:
        return super().is_valid_point(point) and self[point] not in self.invalid_tiles

    def find_all(self, tile):
        for r in range(self.num_rows):
            for c in range(self.num_cols):
                if self.tiles[r][c] == tile:
                    yield Point(r, c)

    def is_equals(self, value):
        return [tile == value for rows in self.tiles for tile in rows]


class Checker:
    def __init__(self, num_rows, num_cols, default_value=None, map: TileMap = None):
        self.arr = [[default_value] * num_cols for _ in range(num_rows)]
        self.map = map

    @classmethod
    def from_map(cls, map: TileMap, default_value=None):
        return cls(map.num_rows, map.num_cols, default_value=default_value, map=map)

    def __getitem__(self, point: Point):
        return self.arr[point.row][point.col]

    def __setitem__(self, point: Point, value):
        self.arr[point.row][point.col] = value

    def is_equals(self, value):
        return [elem == value for rows in self.arr for elem in rows]

    def count_value_with_map(self, checker_value, map_value):
        count = 0
        for r in range(self.map.num_rows):
            for c in range(self.map.num_cols):
                if self.arr[r][c] == checker_value and self.map.tiles[r][c] == map_value:
                    count += 1
        return count


################################################################################
# Searcher
################################################################################

class Searcher(ABC):
    @abstractmethod
    def search(self, start_point, target):
        pass


class BFS:
    def __init__(self, map, target_condition=None, checker=None, block_points=None):
        self.map = map
        self.target_condition = target_condition
        self.checker = checker or Checker.from_map(map, default_value=False)
        self.block_points = block_points or set()

    def search(self, starts: List[Point]) -> int:
        stack = []
        for start in starts:
            stack.append(start)
            self.checker[start] = True

        for step in count(1):
            if not stack:
                return -1
            next_stack = []
            for point in stack:
                for next_point in self.map.nexts(point):
                    if self.target_condition and self.target_condition(next_point):
                        return step
                    if self.checker[next_point] or next_point in self.block_points:
                        continue
                    self.checker[next_point] = True
                    next_stack.append(next_point)
            stack = next_stack


