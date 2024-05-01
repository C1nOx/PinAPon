from pygame import*
mixer.init()
font.init()
mw = display.set_mode((800,600))
display.set_caption('Pin Pon')
BG = transform.scale(image.load('pinpin.png') , (800 , 600))

class GameSprite(sprite.Sprite):
    def __init__(self , x ,y , w , h , filename , speed):
        super().__init__()
        self.image = transform.scale(image.load(filename) , (w , h))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.speed = speed
    def reset(self):
        mw.blit(self.image , (self.rect.x , self.rect.y))

class Left_player(GameSprite):
    def update(self):
        key_pressed = key.get_pressed()
        if key_pressed[K_w] and self.rect.y > 0:
            self.rect.y -= self.speed
        if key_pressed[K_s] and self.rect.y < 350:
            self.rect.y += self.speed

class Right_player(GameSprite):
    def update(self):
        key_pressed = key.get_pressed()
        if key_pressed[K_i] and self.rect.y > 0:
            self.rect.y -= self.speed
        if key_pressed[K_k] and self.rect.y < 350:
            self.rect.y += self.speed

class Ball(GameSprite):
    def update(self):
        self.rect.x += self.speed
        self.rect.y -= self.speed
    
    
raketki = sprite.Group()
l_p = Left_player(10, 250, 80, 250,'topor.png' , 10)
r_p = Right_player(700, 250, 80, 250,'image.png' , 10)
ball = Ball(400 , 300 , 60 , 60 , 'ponpin.png', 4)
raketli.add(l_p)
raketki.add(r_p)

run = True
finish = False
while run:
    for e in event.get():
        if e.type == QUIT:
            run = False


    if sprite.spritecollide(ball, raketki, False):
        ball.speed *= -1
    mw.blit(BG , (0,0))
    l_p.reset()
    l_p.update()
    r_p.reset()
    r_p.update()
    ball.reset()
    ball.update()


    clock = time.Clock()
    display.update()