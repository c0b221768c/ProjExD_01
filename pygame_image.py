import pygame as pg
import sys

def main():
    pg.display.set_caption("はばたけ！こうかとん")
    screen = pg.display.set_mode((800, 600))
    clock  = pg.time.Clock()
    bg_img = pg.image.load("ProjEx2023/fig/pg_bg.jpg")
    kk_img = pg.transform.flip(pg.image.load("ProjEx2023/fig/3.png"),True,False)
    kk_img_list = [kk_img, pg.transform.rotozoom(kk_img, 10, 1.0)]


    tmr = 0

    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT: return

        tmr += 1
        screen.blit(bg_img, [0, 0])
        screen.blit(kk_img_list, [300, 200])


        pg.display.update()
        clock.tick(100)


if __name__ == "__main__":
    pg.init()
    main()
    pg.quit()
    sys.exit()