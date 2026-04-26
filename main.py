from pygame import *
widht=700
height=500
window=display.set_mode((widht,height))
display.set_caption('Шутер')
background = transform.scale(image.load('футболл.jfif'),(widht,height))


clock = time.Clock()
FPS=60

game= True




while game:
    window.blit(background, (0,0))
    for i in event.get():
        if i.type == QUIT:
            game = False
    display.update()