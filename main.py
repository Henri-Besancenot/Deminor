import pygame as pg
import src.Grid as Grid

lost = 0
discover = 1
nothing = 2


if __name__ == "__main__":
    pg.init()
    width, height, nbMines = 40, 40, 200
    # Title
    pg.display.set_caption("Minesweeper")

    # Window creation and modes
    screen = pg.display.set_mode((height*17, width*17))

    # FPS
    fpsClock = pg.time.Clock()

    game_grid = Grid.Grid(width,height,nbMines)
    launched = True

    while launched:
        game_grid.draw(screen)
        pg.display.flip()

        for event in pg.event.get():
            if event.type == pg.QUIT or (event.type == pg.KEYDOWN and event.key == pg.K_ESCAPE):
                launched = False

            if game_grid.update(event) == lost:
                game_grid.reveal()

    pg.quit()