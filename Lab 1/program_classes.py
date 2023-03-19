class tile:
    x: int = -1
    y: int = -1

    def __init__(self, y, x):
        self.x = x
        self.y = y

    def __str__(self) -> str:
        return f"{self.x}:{self.y}"


class step:
    evaluatedTile: tile
    newFrontierTiles: list[tile]

    def __init__(self, evaluatedTile: tile, newFrontierTiles: list[tile]):
        self.evaluatedTile = evaluatedTile
        self.newFrontierTiles = newFrontierTiles
