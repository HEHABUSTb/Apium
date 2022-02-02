class Connect4:

    def __init__(self):
        self.player = 1
        self.column = None
        # self.turn = 1
        self.win = False
        self.field = [[0] * 7 for i in range(6)]
        # print("New game")

    def check_space(self, column):
        values = []
        for i in range(6):
            values.append(self.field[i][column])

        if 0 in values:
            return True
        else:
            return False

    def sequence(self, column_check, x):
        counter = 0
        if column_check.count(x) >= 4:
            for element in column_check:
                if x == element:
                    counter += 1
                    if counter == 4:
                        return True
                else:
                    counter = 0

    def check_winner(self, column, number):

        # check column
        column_check = []
        for i in range(6):
            column_check.append(self.field[i][column])

        if self.sequence(column_check, number) is True:
            return True
        else:
            column_check = []

        # check row
        for i in range(6):
            column_check = self.field[i]
            # print(column_check)
            if self.sequence(column_check, number) is True:
                return True
            else:
                column_check = []

        # check diagonals
        column_check = []
        for i in range(0, 3):
            if self.sequence(column_check, number) is True:
                return True
            else:
                column_check = []
            for n in range(i, 6):
                column_check.append(self.field[n][n-i])

        # check diagonals
        for i in range(1, 4):
            # print('Field', self.field)
            # print(column_check
            for n in range(0, 7 - i):
                # print('Coordinatd ', n, n + i, ' add ', self.field[n][n+i])
                column_check.append(self.field[n][n+i])
            if self.sequence(column_check, number) is True:
                return True
            else:
                column_check = []

        # check diagonals
        for i in range(3, 6):
            print('START')
            for n in range(0, i + 1):
                index = (n - i) * -1
                column_check.append(self.field[n][index])
                # print(n, n - i)
                # print('Added', self.field[n][n - i], ' to ', column_check)
            # print(self.field)

            if self.sequence(column_check, number) is True:
                return True
            else:
                column_check = []

        # check diagonals
        for i in range(0, 3):
            # print('new')
            x = 6
            for n in range(0 + i, 6):
                column_check.append(self.field[n][x])
                x -= 1
            if self.sequence(column_check, number) is True:
                return True
            else:
                column_check = []

    def play(self, col):
        self.column = col
        if self.win is True:
            return 'Game has finished!'
        elif self.check_space(col) is False:
            return 'Column full!'

        if self.player == 1:
            # print("Player ", self.player, " has a turn ", col)
            x = 1
            self.player = 2

        else:
            # print("Player ", self.player, " has a turn ", col)
            x = 2
            self.player = 1

        for i in range(6):
            if self.field[i][col] == 0:
                self.field[i][col] = x
                if self.check_winner(col, x) is True:
                    self.win = True
                    return f'Player {x} wins!'
                else:
                    return f'Player {x} has a turn'


game = Connect4()
game.play(6)
game.play(5)
game.play(3)
game.play(6)

game.play(0)
game.play(6)

game.play(6)
game.play(3)

game.play(6)
game.play(4)

game.play(1)
game.play(6)

game.play(0)
game.play(2)
game.play(1)
game.play(0)

game.play(4)
game.play(5)

game.play(0)
game.play(5)

game.play(2)
game.play(3)

print(game.play(1))
