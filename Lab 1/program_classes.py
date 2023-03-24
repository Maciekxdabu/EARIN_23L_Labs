class tile:
    x: int = -1
    y: int = -1

    def __init__(self, y, x):
        self.x = x
        self.y = y
    
    # the tile is the same tile in the maze if they have the same coordinates
    def __eq__(self, __o: object) -> bool:
        return self.x == __o.x and self.y == __o.y

    def __str__(self) -> str:
        return f"x:{self.x}-y:{self.y}"


class step:
    evaluatedTile: tile
    newFrontierTiles: list[tile]

    def __init__(self, evaluatedTile: tile, newFrontierTiles: list[tile]):
        self.evaluatedTile = evaluatedTile
        self.newFrontierTiles = newFrontierTiles
