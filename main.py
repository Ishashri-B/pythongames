import pygame
from nano import NanoBot
from bacteria import Bacteria
pygame.init()

breach=pygame.mixer.Sound("C:/Users/begou/Desktop/Python Games/breach.wav")
bacteria_fire=pygame.mixer.Sound("C:/Users/begou/Desktop/Python Games/bacteria_fire.wav")
game_over=pygame.mixer.Sound("C:/Users/begou/Desktop/Python Games/game_over.mp3")
game_win=pygame.mixer.Sound("C:/Users/begou/Desktop/Python Games/game_win.mp3")

WIDTH=1200
HEIGHT=700
screen=pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption("Character Movement")

Nano_group=pygame.sprite.Group()
Nano_lasergroup=pygame.sprite.Group()


Nano=NanoBot(Nano_lasergroup)
Nano_group.add(Nano)
Bacteria_group=pygame.sprite.Group()
Bacteria_lasergroup=pygame.sprite.Group()


FPS=20
clock=pygame.time.Clock()

font=pygame.font.Font(None,36)
rows=5
columns=11
sx=100
sy=50
xspace=100
yspace=70

for i in range(rows):
    for n in range(columns):
        x=sx+n*xspace
        y=sy+i*yspace
        b=Bacteria(x,y,2,Bacteria_lasergroup,Bacteria_group)
        Bacteria_group.add(b)
gameover=False
gameloop=True
gamewin=False
while gameloop:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            gameloop=False
        if event.type==pygame.KEYDOWN:
            if event.key==pygame.K_SPACE:
                Nano.fire()

    
    screen.fill("black")


    st=font.render(f"Score= {Nano.score}",True,"white")
    sr=st.get_rect(centerx=WIDTH-250,top=60)
    screen.blit(st,sr)
    lt=font.render(f"Lives= {Nano.lives}",True,"white")
    lr=lt.get_rect(centerx=WIDTH-130,top=60)
    screen.blit(lt,lr)

   
    

    #draw lines
    pygame.draw.line(screen,"red",(0,100),(WIDTH,100),2)
    pygame.draw.line(screen,"red",(0,600),(1200,600),2)

    Nano_lasergroup.update()
    Bacteria_group.update()
    Nano_lasergroup.draw(screen)
    Nano_group.update(event)
    Nano_group.draw(screen)
    Bacteria_group.draw(screen)
    Bacteria_lasergroup.update()
    Bacteria_lasergroup.draw(screen)
    if pygame.sprite.groupcollide(Nano_lasergroup,Bacteria_group,True,True):
        Nano.score=Nano.score+100
    if pygame.sprite.spritecollide(Nano,Bacteria_lasergroup,True):
        Nano.lives=Nano.lives-1


    
    for bacteria in Bacteria_group: 
        if bacteria.rect.bottom>HEIGHT or Nano.lives<1:
            go=font.render("Game Over",True, "white")
            got=go.get_rect(center=(WIDTH//2,HEIGHT//2))
            gameover=True
    if gameover==True:
        screen.fill("black")
        screen.blit(go,got)
        pygame.display.update()
        pygame.time.delay(2000)
        gameloop=False
    
    if len(Bacteria_group)==0:
        wo=font.render("You won",True,"white")
        wot=wo.get_rect(center=(WIDTH//2,HEIGHT//2))
        gamewin=True

    if gamewin==True:
        screen.fill("black")
        screen.blit(wo,wot)
        pygame.display.update()
        pygame.time.delay(2000)
        gameloop=False
            
    pygame.display.flip()
    clock.tick(FPS)
pygame.quit()
