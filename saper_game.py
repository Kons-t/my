import random

class Cell:
    def __init__(self, around_mines=0, mine=False):
        self.around_mines = around_mines
        self.mine = mine
        self.fl_open = False


class GamePole:
    def __init__(self, N, M):
        self.pole = [[Cell() for _ in range(N)] for _ in range(N)]
        self.min_pol = M
        self.init()

    def init(self):
        m = 0
        while m < self.min_pol:
            i = random.randint(0, len(self.pole) - 1)
            j = random.randint(0, len(self.pole) - 1)
            if self.pole[i][j].mine == True:
                continue
            self.pole[i][j].mine = True
            m += 1
        self.sum_mines()

    def sum_mines(self):
        indx = (-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)
        for x in range(len(self.pole)):
            for y in range(len(self.pole)):
                if not self.pole[x][y].mine:
                    self.pole[x][y].around_mines = sum(self.pole[x + i][y + j].mine for i, j in indx if
                                          0 <= x+i < len(self.pole) and 0 <= y+j < len(self.pole))

    def show(self):
        for row in self.pole:
            print(*map(lambda  x: "#" if not x.fl_open else x.around_mines if not x.mine else 'x', row))



pole_game = GamePole(10, 12)
pole_game.show()
