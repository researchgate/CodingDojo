import Tkinter as tk


class Screen():
    cellsize = 20
    padding = 2

    def __init__(self, top, snake, size):
        self.snake = snake
        self.size = size

        self.canvas = tk.Canvas(top, width=size * self.cellsize, height=size * self.cellsize)
        self.canvas.pack()


    def draw(self):
        self.canvas.delete("all")
        for i in range(len(self.snake.snake)):
            self.drawSegment(i)
        self.drawApple()


    def gameOver(self):
        self.canvas.create_rectangle(0, 0, self.size * self.cellsize, self.size * self.cellsize, fill="black")


    def drawApple(self):
        x = self.snake.apple[0] * self.cellsize
        y = self.snake.apple[1] * self.cellsize
        self.canvas.create_oval(x, y, x + self.cellsize, y + self.cellsize, fill="red", width=0)


    def drawSegment(self, i):
        p = self.padding
        x = self.snake.snake[i][0] * self.cellsize
        y = self.snake.snake[i][1] * self.cellsize
        dx = x + self.cellsize
        dy = y + self.cellsize

        nextSeg = None
        prevSeg = None

        if i > 0:
            prevSeg = tuple(a - b for a, b in zip(self.snake.snake[i - 1], self.snake.snake[i]))
        if i < len(self.snake.snake) - 1:
            nextSeg = tuple(a - b for a, b in zip(self.snake.snake[i + 1], self.snake.snake[i]))

        if len(self.snake.snake) == 1 or i < len(self.snake.snake) - 1:
            self.canvas.create_oval(x + p, y + p, dx - p, dy - p, fill="black")

        self.drawSegmentPart(nextSeg, p, x, y, dx, dy)

        if i > 0:
            self.drawSegmentPart(prevSeg, p, x, y, dx, dy)


    def drawSegmentPart(self, otherSeg, p, x, y, dx, dy):
        if otherSeg == (-1, 0):
            self.canvas.create_rectangle(x, y + p, x + self.cellsize / 2, dy - p, fill="black")
        elif otherSeg == (1, 0):
            self.canvas.create_rectangle(x + self.cellsize / 2, y + p, dx, dy - p, fill="black")
        elif otherSeg == (0, -1):
            self.canvas.create_rectangle(x + p, y, dx - p, y + self.cellsize / 2, fill="black")
        elif otherSeg == (0, 1):
            self.canvas.create_rectangle(x + p, y + self.cellsize / 2, dx - p, dy, fill="black")

