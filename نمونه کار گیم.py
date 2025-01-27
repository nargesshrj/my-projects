import pygame
from pygame.locals import Rect
width,height=500,500
display=pygame.display.set_mode((width,height))
green=(50,255,0)
BLACK=(0,0,0)
color=(100,0,2)
clock=pygame.time.Clock()

x ,y=0,0
x_change=0
y_change=0
maneha= [Rect([100,100,50,50]),
         Rect([150,150,50,50]),
         Rect([200,200,50,50]),
         Rect([250,250,50,50]),
         Rect([300,300,50,50]),
         Rect([0,480,499,100])]
colors_maneha=[(200,0,50),(50,150,50),(100,100,0),(255,100,100),(255,0,100),(150,150,150)]
player=Rect([x,y,50,50])
game=True
while game:
    
    for event in pygame.event.get():
        
        if event.type==pygame.QUIT:
            game=False
    """
        if event.type==pygame.KEYDOWN:
            if event.key==pygame.K_RIGHT:
                x_change=5
                y_change=0
            if event.key==pygame.K_LEFT:
                x_change=-5
                y_change=0
            if event.key==pygame.K_UP:
                x_change=0
                y_change=-5  
            if event.key==pygame.K_DOWN:
                x_change=0
                y_change=+5
    """
    keys=pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        player.x+=-5
        player.y+=0
        x_change=-5
        y_change=0
    if keys[pygame.K_RIGHT]:
        player.x+=5
        player.y+=0
        x_change=5
        y_change=0
    if keys[pygame.K_UP]:
        player.x+=0
        player.y+=-5
        y_change=-5
        x_change=0
    if keys[pygame.K_DOWN]:
        player.x+=0
        player.y+=5
        y_change=5
        x_change=0
    
    display.fill(BLACK)
    #player.x=player.x+x_change
    #player.y=player.y+y_change
    player.x=player.x%width
    player.y=player.y%height 
    #player.y+=1
    for mane in maneha:
        if pygame.Rect.colliderect(player,mane):
            player.x-=x_change
            player.y-=y_change
           # player.y+=1
            
    pygame.draw.rect(display,green,[player.x,player.y,player.width,player.height])
    for mane,color in zip(maneha,colors_maneha):
        pygame.draw.rect(display,color,[mane.x,mane.y,mane.width,mane.height])

    pygame.display.update()
   
    clock.tick(50)





