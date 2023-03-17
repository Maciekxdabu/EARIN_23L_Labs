import numpy as np

# O - empty, X - wall, S - start, E - end
maze = [['X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X'],
        ['X', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'X'],
        ['X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'O', 'X'],
        ['X', 'O', 'O', 'O', 'O', 'S', 'O', 'O', 'O', 'X'],
        ['X', 'O', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X'],
        ['X', 'O', 'X', 'O', 'O', 'O', 'O', 'O', 'O', 'X'],
        ['X', 'O', 'X', 'O', 'X', 'X', 'X', 'X', 'O', 'X'],
        ['X', 'O', 'O', 'O', 'X', 'X', 'X', 'X', 'O', 'X'],
        ['X', 'X', 'X', 'X', 'E', 'O', 'O', 'O', 'O', 'X'],
        ['X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X'],
        ['X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X']]

result = list(zip(*np.where(maze == 'S')))
print(result)

#print(maze.index('S'))
# maze.where
# for rows in maze:
#     print(maze.index('S'))


# frontier = 
# explored = []

# class State:
#     x = -1
#     y = -1
#     h = 100000000

# def h(s):
#     return 5