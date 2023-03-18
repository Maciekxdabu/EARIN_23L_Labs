import gui
import numpy as np


class State:
    x = -1
    y = -1

    def __init__(self, y, x):
        self.x = x
        self.y = y

    def __str__(self) -> str:
        return f"{self.x}:{self.y}"


# O - empty, X - wall, S - start, E - end
maze = np.array([['X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X'],
                 ['X', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'X'],
                 ['X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'O', 'X'],
                 ['X', 'O', 'O', 'O', 'O', 'S', 'O', 'O', 'O', 'X'],
                 ['X', 'O', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X'],
                 ['X', 'O', 'X', 'O', 'O', 'O', 'O', 'O', 'O', 'X'],
                 ['X', 'O', 'X', 'O', 'X', 'X', 'X', 'X', 'O', 'X'],
                 ['X', 'O', 'O', 'O', 'X', 'X', 'X', 'X', 'O', 'X'],
                 ['X', 'X', 'X', 'X', 'E', 'O', 'O', 'O', 'O', 'X'],
                 ['X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X'],
                 ['X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X']])

start_state = np.argwhere(maze == 'S')
end_state = np.argwhere(maze == 'E')
end = State(end_state[0][0], end_state[0][1])

# Heuristic definition


def h(state: State):
    return abs(state.x - end.x) + abs(state.y - end.y)


# getting the starting state
startState = State(start_state[0][0], start_state[0][1])
print(h(startState))

# ----- Stepping of the algorithm


class Step:
    def __init__(self, currentState: State, newStates: list[State]):
        self.currentState = currentState
        self.newStates = newStates


# array containing steps
steps = []

# function to add new steps


def AddNewStep(currentState: State, newStates: list[State]):
    steps.append(Step(currentState, newStates))


# frontier = [startState]
# explored = []

def main():
    while True:
        gui.clearConsole()
        print("Maze overview:")
        gui.printMazeWithFrame(maze)
        input = gui.consoleGetInt("option")


main()
