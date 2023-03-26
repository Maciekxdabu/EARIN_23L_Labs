import constants as c
import gui
import mazeFileInputOutput as fileIO

import numpy as np
import random


def generate_maze(width, height, filePath: str):
    # Initialize maze with empty space on every cell with odd coordinates
    maze = np.full((height, width), 'X')
    maze[1::2, 1::2] = ' '
    # Create a list of walls that connect empty cells
    walls = []
    for i in range(1, height - 1):
        for j in range(1, width - 1):
            if i % 2 == 0 and j % 2 == 1 and maze[i-1][j] == ' ' and maze[i+1][j] == ' ':
                walls.append((i, j, 'H'))
            elif i % 2 == 1 and j % 2 == 0 and maze[i][j-1] == ' ' and maze[i][j+1] == ' ':
                walls.append((i, j, 'V'))
    # Shuffle the list of walls
    random.shuffle(walls)
    # Create a list of sets, where each set represents a group of cells
    sets = [{(i, j)} for i in range(height)
            for j in range(width) if maze[i][j] == ' ']
    # Perform Kruskal's algorithm
    for x, y, wall_type in walls:
        if wall_type == 'H':
            set1 = next((s for s in sets if (x-1, y) in s), None)
            set2 = next((s for s in sets if (x+1, y) in s), None)
        else:  # wall_type == 'V'
            set1 = next((s for s in sets if (x, y-1) in s), None)
            set2 = next((s for s in sets if (x, y+1) in s), None)
        if set1 != set2:
            set1.update(set2)
            sets.remove(set2)
            maze[x][y] = ' '
    # set start and end positions in maze
    startWidth = __makeEven(width // 4)  # - width % 4
    startHeight = __makeEven(height // 4)  # - height % 4

    endWidth = __makeEven(width // 2 + width // 4)  # - width % 4
    endHeight = __makeEven(height // 2 + height // 4)  # - height % 4
    maze[startHeight][startWidth] = "S"
    maze[endHeight][endWidth] = "E"

    # Save maze to provided file
    fileIO.saveMaze(filePath, maze=maze)
    # Return maze
    return maze


def __makeEven(x: int):
    if x % 2 == 0:
        x = x + 1
    return x
