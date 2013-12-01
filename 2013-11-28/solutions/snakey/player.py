import game, sys
import Tkinter as tk
import screen_tree
import screen_gui

period = 200
size = 14
withTree = '-t' in sys.argv
paused = False

if '-p' in sys.argv:
    period = int(sys.argv[sys.argv.index('-p') + 1])

if '-s' in sys.argv:
    size = int(sys.argv[sys.argv.index('-s') + 1])

if withTree:
    size = 4


def update():
    if paused:
        top.after(period / 10, update)
        return
    snake.update()
    if snake.isOver():
        itsOver()
    else:
        top.after(period, update)
        draw()


def itsOver():
    top.after(2000, update)
    gui.gameOver()
    tree.gameOver()
    snake.reset()


def draw():
    gui.draw()
    tree.draw()


directions = {
    'Up': game.direction.up,
    'Right': game.direction.right,
    'Down': game.direction.down,
    'Left': game.direction.left,
}


def keyPressed(e):
    global paused
    if e.keysym in directions.keys():
        snake.nextDirection = directions[e.keysym]
    elif e.keysym in ['q', 'o']:
        snake.nextDirection = (snake.direction - 1) % 4
    elif e.keysym in ['w', 'p']:
        snake.nextDirection = (snake.direction + 1) % 4
    elif e.keysym == 'space':
        paused = not paused


top = tk.Tk()
top.bind_all('<Key>', keyPressed)

snake = game.Game(size, size)
gui = screen_gui.Screen(top, snake, size)
tree = screen_tree.Screen(snake, period, size, withTree)

update()

top.mainloop()