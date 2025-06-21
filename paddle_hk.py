import pygame

# Initialize pygame
pygame.init()

# Set display surface
WINDOW_WIDTH = 800
WINDOW_HEIGHT = 600
display_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("Paddle Game")


# Set FPS and clock
FPS = 60
clock = pygame.time.Clock()
font = pygame.font.Font(None, 36)  # Default font, size 36
# Colors
WHITE = (255, 255, 255)

class PlayerPaddle(pygame.sprite.Sprite):
    def __init__(self, x, y, is_player=True):
        super().__init__()
        self.image = pygame.Surface((20, 100))
        self.image.fill(WHITE)
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)
        self.velocity = 8
        self.score= 0
        velocity=self.velocity
    
           
        #write the code for the player to move
    def update(self):
        if event.type==pygame.KEYDOWN:
            if event.key==pygame.K_UP:
                self.rect.y=self.rect.y-self.velocity
            if event.key==pygame.K_DOWN:
               self.rect.y=self.rect.y+self.velocity
               
class ComputerPaddle(pygame.sprite.Sprite):
    def __init__(self, x, y, is_player=True):
        super().__init__()
        self.image = pygame.Surface((20, 100))
        self.image.fill(WHITE)
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)
        self.velocity = 8
        self.score=0
   


    def update(self):
        #write the code for the computer paddle movement
        if ball.rect.centery>self.rect.centery:
            self.rect.y+=self.velocity
        if ball.rect.centery<self.rect.centery:
            self.rect.y-=self.velocity

class Ball(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.Surface((20, 20))
        self.image.fill(WHITE)
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)
        self.velocity_x = 3
        self.velocity_y = 3
    

    def update(self):
       #write the code for ball movement
       self.rect.y+=self.velocity_y
       self.rect.x+=self.velocity_x

       #write the code for the bounce off condition
       
       if self.rect.top<=0 or self.rect.bottom>=WINDOW_HEIGHT:
           self.velocity_y*=-1

# Create game objects
player_paddle = PlayerPaddle(30, WINDOW_HEIGHT//2, is_player=True)
computer_paddle = ComputerPaddle(WINDOW_WIDTH-50, WINDOW_HEIGHT//2, is_player=False)
ball = Ball(WINDOW_WIDTH//2, WINDOW_HEIGHT//2)

# Create sprite groups
all_sprites = pygame.sprite.Group()
all_sprites.add(player_paddle, computer_paddle, ball)

# Main game loop
running = True
gameover=False
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    # Update objects
    player_paddle.update()
    computer_paddle.update()
    ball.update()

    hit=pygame.mixer.Sound("pingponggame/hit.mp3")
    game=pygame.mixer.Sound("pingponggame/game_over.mp3")

    #load the sound and play it when required
    
     
    if ball.rect.x<=0:
        game.play()

    player_score_text = font.render(f"Player Score: {player_paddle.score}", True, WHITE)
    player_score_rect = player_score_text.get_rect(topleft=(10, 10)) 

    computer_score_text = font.render(f"Computer Score: {computer_paddle.score}", True, WHITE)
    computer_score_rect = computer_score_text.get_rect(topright=(780, 10)) 


    gameover_text = font.render(f"Game Over", True, WHITE)
    gameover_rect = gameover_text.get_rect(center=(WINDOW_WIDTH // 2, WINDOW_HEIGHT // 2))


    #Write the conditions if the ball goes out of bound
    if ball.rect.x<=0:
        computer_paddle.score=computer_paddle.score+1
        ball.rect.center=400,300
        ball.velocity_x*=-1
        ball.velocity_y*=-1
 
    #write gameover condition
    if player_paddle.score==5 or computer_paddle.score==5:
        gameover=True
    if gameover:
        display_surface.fill("black")
        display_surface.blit(gameover_text,gameover_rect)
        pygame.display.update()
        
    #Write Ball collision with paddles condition
    if pygame.sprite.collide_rect(ball,player_paddle):
        hit.play()
        ball.velocity_x*=-1
    if pygame.sprite.collide_rect(ball,computer_paddle):
        hit.play()
        ball.velocity_x*=-1
   
    # Draw everything
    display_surface.fill((0,0,0))
    all_sprites.draw(display_surface)

    display_surface.blit(player_score_text, player_score_rect)
    display_surface.blit(computer_score_text, computer_score_rect)
    pygame.display.flip()
    clock.tick(FPS)
    
pygame.quit()
