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
    # Randomize start and end positions
    quadrant_start = random.choice([(0, 0), (0, 1), (1, 0), (1, 1)])
    quadrant_end = random.choice([(0, 0), (0, 1), (1, 0), (1, 1)])
    while quadrant_end == quadrant_start:
        quadrant_end = random.choice([(0, 0), (0, 1), (1, 0), (1, 1)])

    # choose random odd coordinates for start and end positions in the chosen quadrants
    start_x = random.randrange(
        quadrant_start[0] * width // 2 + 1, (quadrant_start[0] + 1) * width // 2, 2)
    start_y = random.randrange(
        quadrant_start[1] * height // 2 + 1, (quadrant_start[1] + 1) * height // 2, 2)
    end_x = random.randrange(
        quadrant_end[0] * width // 2 + 1, (quadrant_end[0] + 1) * width // 2, 2)
    end_y = random.randrange(
        quadrant_end[1] * height // 2 + 1, (quadrant_end[1] + 1) * height // 2, 2)

    # set start and end positions in maze
    maze[start_y][start_x] = "S"
    maze[end_y][end_x] = "E"

    # Save maze to provided file
    fileIO.saveMaze(filePath, maze=maze)
    # Return maze
    return maze


maze = generate_maze(25, 25, "mazes/maze1.txt")

gui.initConsole()
gui.printMazeWithFrame(maze=maze)
