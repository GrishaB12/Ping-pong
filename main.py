from pygame import *
from random import *
font.init()
font = font.Font(None, 36)

lose1 = font.render("ИГРОК ОДИН ПРОИГРАЛ!", True, (0, 0, 0))

lose2 = font.render("ИГРОК ДВА ПРОИГРАЛ!", True, (0, 0, 0))






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
        self.image = transform.scale(image.load(player_image), (60, 85))
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
ball = GameSprite('ufo.png', win_width - 350, win_height - 250, 10 )
speed_x = 3
speed_y = 3

while game:
    for e in event.get():
        if e.type == QUIT:
            game = False
    if not finish:
        
        
        window.blit(background, (0, 0))
        ball.rect.x += speed_x
        ball.rect.y += speed_y
        if sprite.collide_rect(ship, ball) or sprite.collide_rect(ship2, ball):
            speed_x *= -1
            speed_y *= 1
        if ball.rect.y > win_height - 50 or ball.rect.y < 0:
            speed_y *= -1
        if ball.rect.x < 0:
            finish = True
            window.blit(lose1, (200, 200))
        if ball.rect.x > win_width:
            finish = True
            window.blit(lose2, (200, 200))
        
    ball.reset()
    ship.reset()
    ship.updateR()
    ship2.updateL()
    ship2.reset()
    display.update()

    clock.tick(FPS)
