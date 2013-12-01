import random


class direction:
    up = 0
    right = 1
    down = 2
    left = 3


class Game:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.reset()

    def reset(self):
        self.snake = [(0, 0)]
        self.apple = self._nextApple()
        self.direction = direction.right
        self.nextDirection = direction.right

    def isOver(self):
        return self._isCollidingWall() or self._isCollidingWithSnake()

    def _isCollidingWall(self):
        head = self.snake[0]
        return head[0] < 0 or head[0] >= self.width \
                   or head[1] < 0 or head[1] >= self.height

    def _isCollidingWithSnake(self):
        for s in self.snake[1:]:
            if self.snake[0] == s:
                return True
        return False

    def update(self):
        tail = self.snake[-1]
        self._changeDirection()
        self._move()
        if self.snake[0] == self.apple:
            self.apple = self._nextApple()
            self.snake.append(tail)

    def _move(self):
        dc = {
            direction.left: (-1, 0),
            direction.right: (1, 0),
            direction.up: (0, -1),
            direction.down: (0, 1)
        }
        newHead = tuple(a + b for a, b in zip(self.snake[0], dc[self.direction]))
        self.snake.insert(0, newHead)
        del self.snake[-1]

    def _nextApple(self):
        cells = [(w, h) for h in range(self.height) for w in range(self.width) \
                 if (w, h) not in self.snake]
        if len(cells) > 0:
            return cells[self._random(len(cells) - 1)]

    def _changeDirection(self):
        if abs(self.direction - self.nextDirection) != 2:
            self.direction = self.nextDirection

    def _random(self, max):
        return random.randint(0, max)
