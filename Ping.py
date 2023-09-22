from pygame import*
from time import clock
bg = (240, 0, 250)
wind_width = 500
wind_height = 500
window = display.set_mode((wind_width, wind_height))
window.fill(bg)
class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, player_speed, player_width, player_height):
        super().__init__()
        self.image = image.load(loadimage)
        self.speed = player_speed
        self.rect.x=player_x
        self.rect.y=player_y
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))
class Player(GameSprite):
    def update_o(self):
        key = key.get_pressed()
        if key[K_UP] and self.rect.y>5:
            self.rect.y-=self.speed
        if key[K_DOWN] and self.rect.y<445:
            self.rect.y+=self.speed
    def update_second(self):
        key = key.get_pressed()
        if key[K_w] and self.rect.y>5:
            self.rect.y-=self.speed
        if key[K_s] and self.rect.y<395:
            self.rect.y+=self.speed
game = True
game_over = False
clock = time.Clock()
FPS = 60
platform1 = Player("", 30, 250, 4, 20 ,50)
platform2 = Player("", 440, 250, 4, 20 ,50)
ball = GameSprite("", 250, 250, 4, 35)
font.init()
font = font.Font("Arial", 30)
lose1 = font.render("Player 1 Lose!", True, (250, 215, 0))
lose2 = font.render("Player 1 Lose!", True, (250, 10, 1))


speed_x=3
speed_y=3


while game:
    for e in event.get():
        if e.type == QUIT:
            game = game_over
    if game_over != True:
        window.fill(bg)
        platform1.update_o()
        platform2.update_second()
        ball.rect.x += speed_x
        ball.rect.y += speed_y
        if sprite.colide_rect(ball, platform1) or sprite.collide_rect(ball, platform2):
            speed_x *= -1
            speed_y *= -1
        if ball.rect.y > wind_height-10 or ball.rect.y <0:
            speed_y*=-1
        if ball.rect.x >= wind_width:
            game = False
            window.blit(lose1, (200, 200))
        if ball.rect.x<=0:
            game = False
            window.blit(lose2, (200, 200))
        platform1.reset()
        platform2.reset()



platform1.update_o()
display.update()
clock.tick(FPS)