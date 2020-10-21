from engine import *

game = Game()

print("Welcome to AD s2dios 2048")

while True:
    print(game)
    cmd = input("> ")
    if cmd == "w":
        game.takeTurn(0)
    elif cmd == "s":
        game.takeTurn(1)
    elif cmd == "a":
        game.takeTurn(2)
    elif cmd == "d":
        game.takeTurn(3)
    else:
        print("WASD - Up Left Down Right")