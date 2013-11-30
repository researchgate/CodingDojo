import httplib


class Screen:
    def __init__(self, snake, period, size, enabled):
        self.enabled = enabled
        self.snake = snake
        self.size = size
        self.period = period

    def draw(self):
        self.sendToTree(self.drawAsTreePattern())


    def gameOver(self):
        self.sendToTree('100-1111111111111111')


    def drawAsTreePattern(self):
        screen = ['0'] * self.size * self.size
        for c in self.snake.snake:
            screen[c[1] * self.size + c[0]] = '1'
        pattern = []
        blinks = 4
        for i in range(blinks):
            apple = '1'
            if i % 2 == 0:
                apple = '0'
            screen[self.snake.apple[1] * self.size + self.snake.apple[0]] = apple
            pattern.append(str(self.period / (blinks * 4)) + '-' + ''.join(screen))
        return '\n'.join(pattern)


    def sendToTree(self, pattern):
        if not self.enabled:
            return
        conn = httplib.HTTPConnection("192.168.178.134:8080")
        conn.request("POST", "/", pattern)
        conn.close()
