import random

class Board():
    UP = 0
    DOWN = 1
    LEFT = 2
    RIGHT = 3

    def __init__(self):
        self.board = [0 for i in range(16)]
        self.generateTile()
        self.generateTile()

    def __str__(self):
        result = "-" * 25
        for i in range(4):
            result += "\n| "
            for j in range(4):
                tile = str(self.board[i*4 + j])
                if tile == "0":
                    tile = " "
                if len(tile) == 1:
                    result += " " + tile + " "
                elif len(tile) == 2:
                    result += tile + " "
                else:
                    result += tile
                result += " | "
            result += "\n" + "-" * 25
        return result

    def isGameOver(self):
        ''' Returns -2 if lost, -10 if won, 0 otherwise '''

        if 2048 in self.board:
            return -10
        elif 0 not in self.board:
            return -2
        else:
            return 0

    def generateTile(self):
        assert 0 in self.board
        while True:
            pos = random.randrange(16)
            # only generate tile if the space is empty
            if self.board[pos] == 0:
                # generate a 4 with a 10% chance
                if random.random() > .9:
                    self.board[pos] = 4
                else:
                    self.board[pos] = 2
                return

    def move(self, direction):
        ''' Returns -1 if nothing moved, score otherwise '''

        # cut the board into strips (rows/cols)
        if direction == Board.UP or direction == Board.DOWN:
            strips = [[self.board[i] for i in range(j, 16, 4)] for j in range(4)]
        else:
            strips = [self.board[i:i+4] for i in range(0, 16, 4)]

        # for down and right, we're moving in the reverse direcction of the strip
        if direction == Board.DOWN or direction == Board.RIGHT:
            isReversed = True
            for strip in strips:
                strip.reverse()
        else:
            isReversed = False

        # shift strips
        score = 0
        moved = False
        for j in range(4):
            strip = strips[j]

            # if the whole strip is blank do nothing
            if sum(strip) == 0:
                continue

            # remove blanks backwards
            ogSize = 4
            for i in range(len(strip)-1, -1, -1):
                if strip[i] == 0:
                    ogSize -= 1
                else:
                    break
            strip = [tile for tile in strip if tile != 0]

            # combine adjacent repeated tiles
            for i in range(len(strip) - 1):
                if strip[i] == strip[i+1]:
                    score += strip[i] * 2
                    strip[i] = strip[i] * 2
                    strip[i + 1] = 0

            # get rid of any remaining spaces
            strip = [tile for tile in strip if tile != 0]

            # shift everything to the start
            if len(strip) < ogSize:
                moved = True

            strips[j] = strip + [0] * (4 - len(strip))

        if not moved:
            return -1

        # restore reversed strips
        if isReversed:
            for strip in strips:
                strip.reverse()

        # update board to reflect strips
        if direction == Board.UP or direction == Board.DOWN:
            for i in range(16):
                self.board[i] = strips[i%4][i//4]
        else:
            for i in range(16):
                self.board[i] = strips[i//4][i%4]

        return score

class Game():
    def __init__(self):
        self.score = 0
        self.board = Board()

    def __str__(self):
        status = self.board.isGameOver()
        if status == -10:
            result = "You win!\n"
        elif status == -2:
            result = "Game over\n"
        else:
            result = ""
        return result + "Score: " + str(self.score) + "\n" + str(self.board)

    def takeTurn(self, direction):
        '''
        Returns -1 if move is illegal, -2 if lost, -10 if won
        Else, returns score gained.
        '''
        status = self.board.isGameOver()
        if status < 0:
            return status

        # TODO: case where board is full but there are moves to free up space

        newScore = self.board.move(direction)
        
        if newScore == -1:
            return -1

        status = self.board.isGameOver()
        if status < 0:
            return status

        self.board.generateTile()
        self.score += newScore
        return newScore
