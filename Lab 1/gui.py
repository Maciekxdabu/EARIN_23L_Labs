from tkinter import *

root = Tk()


label = Label(
    root, text="Maze solver using Greedy Best-First search algorithm!")
label.pack()


def visblock():
    block = Label(root)
    block.image = PhotoImage(file="images\wall.png")
    block['image'] = block.image
    return block
# These act like walls


def invisblock():
    block = Button(root)
    block.image = PhotoImage(file="images\empty.png")
    block['image'] = block.image
    return block
# These act like empty spaces"""


maze = [[visblock(), visblock(), visblock(), visblock()],
        [visblock(), invisblock(), invisblock(), visblock()],
        [invisblock(), invisblock(), visblock(), invisblock()],
        [visblock(), invisblock(), invisblock(), invisblock()],
        [visblock(), visblock(), visblock(), visblock()]]

for i, block_row in enumerate(maze):
    for j, block in enumerate(block_row):
        block.grid(row=i, column=j)


button_1 = Button(root, text="Load file")
button_1.pack()

button_2 = Button(root, text="Show solution/Hide solution")
button_2.pack()

button_3 = Button(root, text="Previous step")
button_3.pack()

button_4 = Button(root, text="Next step")
button_4.pack()

root.mainloop()
