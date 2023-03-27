import program_classes as pc
import math


def h1(examinedTile: pc.Tile, endTile: pc.Tile):
    return abs(examinedTile.x - endTile.x) + abs(examinedTile.y - endTile.y)


def h2(state: pc.Tile, endTile: pc.Tile):
    return math.sqrt(pow((state.x - endTile.x), 2) + pow((state.y - endTile.y), 2))
