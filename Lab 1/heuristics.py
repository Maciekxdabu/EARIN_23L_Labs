import program_classes as pc
import math


def h1(examined_tile: pc.Tile, end_tile: pc.Tile):
    return abs(examined_tile.x - end_tile.x) + abs(examined_tile.y - end_tile.y)


def h2(examined_tile: pc.Tile, end_tile: pc.Tile):
    return math.sqrt(pow((examined_tile.x - end_tile.x), 2) + pow((examined_tile.y - end_tile.y), 2))
