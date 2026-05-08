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
class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, player_speed):
        super().__init__()
        self.image = transform.scale(image.load(player_image), (65, 65))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))
class Player(GameSprite):
    def updateR(self):
        keys = key.get_pressed()
        if keys[K_UP] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_DOWN] and self.rect.y < win_height - 80:
            self.rect.y += self.speed
    def updateL(self):
        keys = key.get_pressed()
        if keys[K_w] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_s] and self.rect.y < win_height - 80:
            self.rect.y += self.speed


            
ship = Player("rocket.png", win_width - 50, win_height - 80, 10)
ship2 = Player("rocket.png", win_width - 700, win_height - 80, 10)


while game:
    for e in event.get():
        if e.type == QUIT:
            game = False
    if not finish:
        window.blit(background, (0, 0))


    ship.reset()
    ship.updateR()
    ship2.reset()
    ship2.updateL()
    display.update()
    clock.tick(FPS)
