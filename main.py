from pygame import *
widht=700
height=500
window=display.set_mode((widht,height))
display.set_caption('Шутер')
background = transform.scale(image.load('футболл (1).png'),(widht,height))

speed_x=0
speed_y=0
clock = time.Clock()
FPS=60
Finish= False
game= True
class GameSprite(sprite.Sprite):
    def __init__(self,player_image,player_x,player_y,size_x,size_y,player_speed):
        super().__init__()
        self.image=transform.scale(image.load(player_image),(65,65))
        self.speed=player_speed
        self.rect=self.image.get_rect()
        self.rect.x=player_x
        self.rect.y=player_y
        self.rect.x=size_x
        self.rect.y=size_y

    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))
class Player(GameSprite):
    def update_l(self):
        keys=key.get_pressed()
        if keys[K_w] and self.rect.y >5:
            self.rect.y -= self.speed
        if keys[K_s]and self.rect.y < 430:
            self.rect.y += self.speed
    def update_r(self):
        keys=key.get_pressed()
        if keys[K_UP] and self.rect.y >5:
            self.rect.y -= self.speed
        if keys[K_DOWN]and self.rect.y < 430:
            self.rect.y += self.speed


Raketka1 = Player('Raketka2.png', 20, 100, 68, 435, 1)
Raketka2=Player('Raketka2.png',300,20,570,435,1)
Mach=GameSprite('Tennis1.png', 20, 100, 317, 214, 1)

while game:
    window.blit(background, (0,0))
    for i in event.get():
        if i.type == QUIT:
            game = False
    Raketka1.reset()
    Raketka1.update_l()
    Raketka2.reset()
    Raketka2.update_r()
    Mach.reset()



    display.update()