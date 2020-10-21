from engine import *
from random import randrange
from ml import *

game = Game()

print("Random bot")
print(game)

while True:
    r = game.takeTurn(randrange(4))
    if r < -1:
        print(game)
        break