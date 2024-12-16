import pygame
import pygame as pg

plain = 9
flag = 10
mine = 11

lost = 0
discover = 1
nothing = 2
flag_discover = 3


class Case(pg.sprite.Sprite):

    def __init__(self, x: int, y: int):
        pg.sprite.Sprite.__init__(self)
        self.image = pg.image.load("Sprite/tile_plain.png").convert_alpha()
        self.rect = self.image.get_rect()
        self.coord = (x,y)
        self.rect.x = x*17
        self.rect.y = y*17

        # State can be : Nothing (False) or Bomb (True)
        self.isMine = False

        # At first the content isn't shown
        self.shown = False

        # At first a case isn't flaged
        self.flaged = False

        self.bombs = 0

    def load_image(self, number:int):
        if number == 0:
            self.image = pg.image.load("Sprite/tile_clicked.png")
        if number == 1:
            self.image = pg.image.load("Sprite/tile_1.png")
        if number == 2:
            self.image = pg.image.load("Sprite/tile_2.png")
        if number == 3:
            self.image = pg.image.load("Sprite/tile_3.png")
        if number == 4:
            self.image = pg.image.load("Sprite/tile_4.png")
        if number == 5:
            self.image = pg.image.load("Sprite/tile_5.png")
        if number == 6:
            self.image = pg.image.load("Sprite/tile_6.png")
        if number == 7:
            self.image = pg.image.load("Sprite/tile_7.png")
        if number == 8:
            self.image = pg.image.load("Sprite/tile_8.png")
        if number == plain:
            self.image = pg.image.load("Sprite/tile_plain.png")
        if number == flag:
            self.image = pg.image.load("Sprite/tile_flag.png")
        if number == mine:
            self.image = pg.image.load("Sprite/tile_mine.png")

        # Peut être ajouter une conversion de taille

    def reveal(self):
        if self.isMine:
            self.load_image(mine)
        else:
            self.load_image(self.bombs)



    def update(self, event: pg.event) -> int:
        if event.type == pygame.MOUSEBUTTONUP:
            if self.rect.collidepoint(event.pos):
                # leftclick on not shown
                if not self.shown:
                    if event.button == 1:
                        if self.flaged:
                            return nothing
                        else:
                            self.shown = True

                        if self.isMine:
                            self.reveal()
                            # The player lost
                            return lost

                        # Show the number of mines arround
                        else:
                            self.reveal()
                            # The player is safe
                            if self.bombs == 0:
                                return discover
                            else:
                                return nothing

                else:
                    if event.button == 1:
                        return flag_discover

                # rightclick
                if event.button == 3 and not self.shown:
                    if self.flaged:
                        self.load_image(plain)
                        self.flaged = False
                    else:
                        self.load_image(flag)
                        self.flaged = True
                    # The player is safe
                    return nothing

        return nothing

    def __repr__(self):
        return f'Case({self.coord[0]}, {self.coord[1]}, {self.isMine}, {self.flaged})'
