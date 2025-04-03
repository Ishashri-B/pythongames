import pygame
import random

pygame.init()

WIDTH=600
HEIGHT=600

screen=pygame.display.set_mode((HEIGHT,WIDTH))
pygame.display.set_caption("The Snake Game")

SNAKE_SIZE=20
APPLE_SIZE=20

head_x=WIDTH//2
head_y=HEIGHT//2

snake_dx=0
snake_dy=0

score=0
f=pygame.font.SysFont("Comic Sans",20)
scoret=f.render("Score= "+str(score),True,"black")
rect1=scoret.get_rect()
rect1=topleft=(10,10)
speed=10

FPS=20
clock=pygame.time.Clock()

appleposition=(500,500,APPLE_SIZE,APPLE_SIZE)
apple=pygame.draw.rect(screen,"red",appleposition)

snakeposition=(head_x,head_y,SNAKE_SIZE,SNAKE_SIZE)
snake=pygame.draw.rect(screen,"lime",snakeposition)

body=[]
eat=pygame.mixer.Sound("C:/Users/begou/Desktop/Python Games/apple-eating-36127.mp3")
gameloop=True
while gameloop:
    for event in pygame.event.get():
        
        if event.type==pygame.QUIT:
            gameloop=False
    if event.type==pygame.KEYDOWN:
        if event.key==pygame.K_RIGHT:
            snake_dx=1*speed
            snake_dy=0
        elif event.key==pygame.K_LEFT:
            snake_dx=-1*speed
            snake_dy=0
        elif event.key==pygame.K_UP:
            snake_dx=0
            snake_dy=-1*speed
        elif event.key==pygame.K_DOWN:
            snake_dx=0
            snake_dy=1*speed
    head_x=head_x+snake_dx
    head_y=head_y+snake_dy
    body.insert(0,snakeposition)
    body.pop()

    if snake.colliderect(apple):
        eat.play()
        x=random.randint(20,580)
        y=random.randint(20,580)
        appleposition=(x,y,APPLE_SIZE,APPLE_SIZE)
        score=score+1

        body.append(snakeposition)

    scoret=f.render("Score= "+str(score),True,"black")

    screen.fill("hotpink")
    screen.blit(scoret,rect1)
    for parts in body:
        pygame.draw.rect(screen,"green",parts)
    
    apple=pygame.draw.rect(screen,"red",appleposition)

    snakeposition=(head_x,head_y,SNAKE_SIZE,SNAKE_SIZE)
    snake=pygame.draw.rect(screen,"lime",snakeposition)
    

    pygame.display.flip()
    clock.tick(FPS)
pygame.quit()