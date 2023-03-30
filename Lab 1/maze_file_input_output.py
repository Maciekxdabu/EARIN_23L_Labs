import os
import numpy as np


def load_maze(file_path: str) -> np.array:
    maze_file = loaded_maze = open(file_path, "r")
    loaded_maze = maze_file.read()
    maze_file.close()
    loaded_maze = loaded_maze.split("\n")
    list_of_lists = []

    for x in loaded_maze:
        # split the line into single character elements
        list_of_lists.append(list(x))

    final_maze = np.array(list_of_lists)

    return final_maze


def save_maze(filePath: str, maze):
    # Get the directory path
    dir_path = os.path.dirname(filePath)

    # Create the directory if it doesn't exist
    if not os.path.exists(dir_path):
        os.makedirs(dir_path)

    # Convert maze to string
    maze_str = ""
    for row in maze:
        maze_str += "".join(row) + "\n"

    # Write maze string to file (since we open file using "with" it closes the file correctly when it ends)
    with open(filePath, "w") as f:
        f.write(maze_str[:-1])


def get_maze_save_path(file_name: str) -> str:
    mazes_directory = 'mazes'
    maze_dir = os.path.realpath(os.path.join(
        os.getcwd(), os.path.dirname(__file__),  mazes_directory))

    return os.path.join(maze_dir, file_name)
