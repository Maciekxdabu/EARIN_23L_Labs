import program_classes as pc


def h1(examinedTile: pc.tile, endTile: pc.tile):
    return abs(examinedTile.x - endTile.x) + abs(examinedTile.y - endTile.y)


def h2(state: pc.tile, endTile: pc.tile):
    return abs(state.x - endTile.x) ^ 2 + abs(state.y - endTile.y) ^ 24
