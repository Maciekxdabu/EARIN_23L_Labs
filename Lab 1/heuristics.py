import program_classes as pc


def h1(self, state: pc.tile):
    return abs(state.x - self.__end_tile.x) + abs(state.y - self.__end_tile.y)


def h2(self, state: pc.tile):
    return abs(state.x - self.__end_tile.x) ^ 5 + abs(state.y - self.__end_tile.y) ^ 10
