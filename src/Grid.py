import src.Case as Case
import random
import pygame as pg

lost = 0
discover = 1
nothing = 2
flag_discover = 3


class Grid:

    def __init__(self, height:int, width:int, nbBombs:int):
        self.grid = [[Case.Case(i, j) for i in range(width)] for j in
                     range(height)]

        self.height = height
        self.width = width

        k = 0
        while k < nbBombs:
            i, j = random.randint(0, width - 1), random.randint(0, height - 1)
            if not self.grid[j][i].isMine:
                self.grid[j][i].isMine = True
                self.updateBombsCount(i, j)
                k += 1

    def getAdjacentCases(self, i:int, j:int):
        res = []
        if i > 0:
            res.append(self.grid[j][i-1])
            if j > 0:
                res.append(self.grid[j-1][i-1])
            if j < self.height - 1:
                res.append(self.grid[j + 1][i - 1])

        if i < self.width - 1:
            res.append(self.grid[j][i+1])
            if j > 0:
                res.append(self.grid[j-1][i+1])
            if j < self.height - 1:
                res.append(self.grid[j+1][i+1])

        if j > 0:
            res.append(self.grid[j-1][i])
        if j < self.height - 1:
            res.append(self.grid[j+1][i])

        return res

    def updateBombsCount(self, i:int, j:int):
        for case in self.getAdjacentCases(i,j):
            case.bombs += 1

    def countFlags(self, i:int, j:int):
        counter = 0
        for case in self.getAdjacentCases(i,j):
            if case.flaged:
                counter += 1
        return counter

    def draw(self, screen: pg.Surface) -> None:
        for lines in self.grid:
            for case in lines:
                screen.blit(case.image, case.rect)

    def update(self, event: pg.event):
        for lines in self.grid:
            for case in lines:
                x,y = case.coord
                state = case.update(event)
                if state == discover:
                    self.extend(x, y, True)
                if state == flag_discover and case.bombs == self.countFlags(x,y):
                    for adj_case in self.getAdjacentCases(x, y):
                        if adj_case.flaged:
                            continue
                        if adj_case.isMine:
                            return lost
                        i,j = adj_case.coord
                        self.extend(i, j, True)

                if state == lost:
                    return lost

    def extend(self, x: int, y: int, origin: bool):
        case = self.grid[y][x]  # ligne y colonne x

        if (case.shown and not origin) or case.flaged:
            return

        case.shown = True
        case.load_image(case.bombs)

        if case.bombs == 0:
            # if x > 0:
            #     self.extend(x - 1, y, False)
            # if y > 0:
            #     self.extend(x, y - 1, False)
            # if x < self.width - 1:
            #     self.extend(x + 1, y, False)
            # if y < self.height - 1:
            #     self.extend(x, y + 1, False)
            for adj_case in self.getAdjacentCases(x, y):
                i,j = adj_case.coord
                self.extend(i, j, False)

    def reveal(self):
        for line in self.grid:
            for case in line:
                case.reveal()
