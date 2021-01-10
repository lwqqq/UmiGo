import enum
from collections import namedtuple


class Player(enum.Enum)
    black = 1
    white = 2

    @property
    def other(self):
        #return Player.black if self == Player.white else Player.white
        if self == Player.white:
            return Player.black
        else:
            return Player.white


class Point(namedtuple('Point', 'row col')):
    def neighbors(self):
        return [
            Point(self.row - 1, self.col),
            Point(self.row + 1, self.col),
            Point(self.row, self.col - 1),
            Point(self.row, self.col + 1),
        ]


class Bored():
    def __init__(self, num_rows, num_cols):
        self.num_rows = num_rows
        self.num_cols = num_cols
        self._grid = {}


