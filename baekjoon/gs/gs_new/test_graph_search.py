
from .graph_search import *


def test_RangeMap():
    map = Map(3, 4)
    assert set(map.nexts(Point(1, 1))) == {Point(0, 1), Point(1, 0), Point(1, 2), Point(2, 1)}
    assert set(map.nexts(Point(0, 0))) == {Point(0, 1), Point(1, 0)}


def test_TileMap():
    tiles = '''
0 0 1 0 
1 0 0 0
0 1 0 1    
    '''
    map = TileMap.from_str(tiles, invalid_tiles={'1'})
    assert map.is_valid_point(Point(1, 1))
    assert set(map.nexts(Point(0, 1))) == {Point(0, 0), Point(1, 1)}


def test_Checker():
    checker = Checker(4, 5, default_value=False)
    assert not checker[Point(1, 2)]
    checker[Point(1, 2)] = True
    assert checker[Point(1, 2)]
