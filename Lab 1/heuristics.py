import program_classes as pc
import math


def h1(examinedTile: pc.Tile, endTile: pc.Tile):
    examinedTile.h = abs(examinedTile.x - endTile.x) + abs(examinedTile.y - endTile.y)
    return examinedTile.h


def h2(state: pc.Tile, endTile: pc.Tile):
    state.h = math.sqrt(pow(abs(state.x - endTile.x),2) + pow(abs(state.y - endTile.y),2))
    return state.h
