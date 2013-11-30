import unittest, game


class MoveShortSnakeTest(unittest.TestCase):
    def setUp(self):
        self.game = GameFixture(self)
        self.game.givenA_Times_Field(5, 5)
        self.game.givenTheSnakeAt([(2, 2)])

    def test_moveRight(self):
        self.game.givenItsDirectionIs(game.direction.right)
        self.game.whenTheGameIsUpdated()
        self.game.thenTheSnakeShouldBeAt([(3, 2)])

    def test_moveLeft(self):
        self.game.givenItsDirectionIs(game.direction.left)
        self.game.whenTheGameIsUpdated()
        self.game.thenTheSnakeShouldBeAt([(1, 2)])

    def test_moveUp(self):
        self.game.givenItsDirectionIs(game.direction.up)
        self.game.whenTheGameIsUpdated()
        self.game.thenTheSnakeShouldBeAt([(2, 1)])

    def test_moveDown(self):
        self.game.givenItsDirectionIs(game.direction.down)
        self.game.whenTheGameIsUpdated()
        self.game.thenTheSnakeShouldBeAt([(2, 3)])


class MoveLongSnakeTest(unittest.TestCase):
    def setUp(self):
        self.game = GameFixture(self)
        self.game.givenA_Times_Field(5, 5)
        self.game.givenTheSnakeAt([(2, 2), (1, 2), (0, 2)])

    def test_moveRight(self):
        self.game.givenItsDirectionIs(game.direction.right)
        self.game.whenTheGameIsUpdated()
        self.game.thenTheSnakeShouldBeAt([(3, 2), (2, 2), (1, 2)])

    def test_moveUp(self):
        self.game.givenItsDirectionIs(game.direction.up)
        self.game.whenTheGameIsUpdated()
        self.game.thenTheSnakeShouldBeAt([(2, 1), (2, 2), (1, 2)])

    def test_moveDown(self):
        self.game.givenItsDirectionIs(game.direction.down)
        self.game.whenTheGameIsUpdated()
        self.game.thenTheSnakeShouldBeAt([(2, 3), (2, 2), (1, 2)])


class DetectCollisionsTest(unittest.TestCase):
    def setUp(self):
        self.game = GameFixture(self)
        self.game.givenA_Times_Field(3, 3)

    def test_dontCollide(self):
        self.game.givenTheSnakeAt([(1, 1)])
        self.game.givenItsDirectionIs(game.direction.right)
        self.game.whenTheGameIsUpdated()
        self.game.thenTheGameShouldNotBeOver()

    def test_hitRightWall(self):
        self.game.givenTheSnakeAt([(2, 1)])
        self.game.givenItsDirectionIs(game.direction.right)
        self.game.whenTheGameIsUpdated()
        self.game.thenTheGameShouldBeOver()

    def test_hitLeftWall(self):
        self.game.givenTheSnakeAt([(0, 1)])
        self.game.givenItsDirectionIs(game.direction.left)
        self.game.whenTheGameIsUpdated()
        self.game.thenTheGameShouldBeOver()

    def test_hitTopWall(self):
        self.game.givenTheSnakeAt([(1, 0)])
        self.game.givenItsDirectionIs(game.direction.up)
        self.game.whenTheGameIsUpdated()
        self.game.thenTheGameShouldBeOver()

    def test_hitBottomWall(self):
        self.game.givenTheSnakeAt([(1, 2)])
        self.game.givenItsDirectionIs(game.direction.down)
        self.game.whenTheGameIsUpdated()
        self.game.thenTheGameShouldBeOver()

    def test_collidesWithItself(self):
        self.game.givenTheSnakeAt([(1, 2), (2, 2), (2, 1), (1, 1), (0, 1)])
        self.game.givenItsDirectionIs(game.direction.up)
        self.game.whenTheGameIsUpdated()
        self.game.thenTheGameShouldBeOver()

    def test_dontCollideWithItself(self):
        self.game.givenTheSnakeAt([(1, 2), (2, 2), (2, 1), (1, 1), (0, 1)])
        self.game.givenItsDirectionIs(game.direction.left)
        self.game.whenTheGameIsUpdated()
        self.game.thenTheGameShouldNotBeOver()


class EatApplesTest(unittest.TestCase):
    def setUp(self):
        self.game = GameFixture(self)
        self.game.givenA_Times_Field(3, 3)
        self.game.givenTheAppleIsAt((2, 0))
        self.game.givenItsDirectionIs(game.direction.right)
        self.game.givenTheNextRandomNumberIs(1)

    def test_replaceWithNewApple(self):
        self.game.givenTheSnakeAt([(1, 0)])
        self.game.whenTheGameIsUpdated()
        self.game.thenThereShouldBeAnAppleAt((1, 0))

    def test_dontPutNewAppleOnSnake(self):
        self.game.givenTheSnakeAt([(1, 0), (0, 0)])
        self.game.whenTheGameIsUpdated()
        self.game.thenThereShouldBeAnAppleAt((0, 1))

    def test_grow(self):
        self.game.givenTheSnakeAt([(1, 0), (0, 0)])
        self.game.whenTheGameIsUpdated()
        self.game.thenTheSnakeShouldBeAt([(2, 0), (1, 0), (0, 0)])


class ChangeDirection(unittest.TestCase):
    def setUp(self):
        self.game = GameFixture(self)
        self.game.givenA_Times_Field(3, 3)
        self.game.givenTheSnakeAt([(1, 1)])
        self.game.givenItsDirectionIs(game.direction.up)

    def test_turnLeft(self):
        self.game.givenThenNextDirectionIs(game.direction.left)
        self.game.whenTheGameIsUpdated()
        self.game.thenTheSnakeShouldBeAt([(0,1)])

    def test_turnRight(self):
        self.game.givenThenNextDirectionIs(game.direction.right)
        self.game.whenTheGameIsUpdated()
        self.game.thenTheSnakeShouldBeAt([(2,1)])

    def test_doNotTurnAround(self):
        self.game.givenThenNextDirectionIs(game.direction.down)
        self.game.whenTheGameIsUpdated()
        self.game.thenTheSnakeShouldBeAt([(1,0)])

    def test_doNotTurnAroundGoinfLeft(self):
        self.game.givenItsDirectionIs(game.direction.left)
        self.game.givenThenNextDirectionIs(game.direction.right)
        self.game.whenTheGameIsUpdated()
        self.game.thenTheSnakeShouldBeAt([(0,1)])


class GameFixture():
    def __init__(self, test):
        self.test = test

    def givenA_Times_Field(self, width, height):
        self.game = game.Game(width, height)
        self.givenTheAppleIsAt((width - 1, height - 1))

    def givenTheSnakeAt(self, coordinates):
        self.game.snake = coordinates

    def givenItsDirectionIs(self, direction):
        self.game.direction = direction
        self.game.nextDirection = direction

    def givenTheAppleIsAt(self, coordinates):
        self.game.apple = coordinates

    def givenTheNextRandomNumberIs(self, number):
        self.game._random = lambda max: number

    def whenTheGameIsUpdated(self):
        self.game.update()

    def thenTheSnakeShouldBeAt(self, coordinates):
        self.test.assertEquals(coordinates, self.game.snake)

    def thenTheGameShouldBeOver(self):
        self.test.assertTrue(self.game.isOver())

    def thenTheGameShouldNotBeOver(self):
        self.test.assertFalse(self.game.isOver())

    def thenThereShouldBeAnAppleAt(self, coordinates):
        self.test.assertEquals(coordinates, self.game.apple)

    def givenThenNextDirectionIs(self, direction):
        self.game.nextDirection = direction


if __name__ == '__main__':
    unittest.main()
