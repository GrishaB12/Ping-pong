from pygame import *
from random import *
font.init()
font1 = font.SysFont(None, 36)
font2 = font.SysFont(None, 80)
win_width = 700
win_height = 500
window = display.set_mode((win_width, win_height))
display.set_caption("Степан Дильдин")
background = transform.scale(image.load("galaxy.jpg"), (win_width, win_height))
score = 0
lost = 0
game = True
finish = False
clock = time.Clock()
FPS = 60
mixer.init()
mixer.music.load("space.ogg")
mixer.music.play()
fire_sound = mixer.Sound("fire.ogg")



            

while game:
    for e in event.get():
        if e.type == QUIT:
            game = False
    if not finish:
        window.blit(background, (0, 0))


    display.update()
    clock.tick(FPS)
