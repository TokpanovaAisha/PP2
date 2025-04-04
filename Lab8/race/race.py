#Imports
import pygame, sys
from pygame.locals import *
import random, time
 
#Initialzing 
pygame.init()
 
#Setting up FPS 
FPS = 60
clock = pygame.time.Clock()

#Creating colors
blue  = (0, 0, 255)
red   = (255, 0, 0)
green = (0, 255, 0)
black = (0, 0, 0)
white = (255, 255, 255)
 
#Other Variables for use in the program
width = 620
height = 650
speed = 5
score = 0
score_coin = 0

#Create a white screen 
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Game")

#Setting up Fonts
font = pygame.font.SysFont("Verdana", 60)
font_small = pygame.font.SysFont("Verdana", 20)
game_over = font.render("Game Over", True, black)
 
background = pygame.image.load("AnimatedStreet.png")
image_coin = pygame.image.load("coin.png")
 

 
class Enemy(pygame.sprite.Sprite):
      def __init__(self):
        super().__init__() 
        self.image = pygame.image.load("enemy_car.png")
        self.rect = self.image.get_rect() # Get the rectangle (bounding box) of the enemy car
        self.rect.inflate_ip(-34, -15)  # Reduces the hitbox by 20 pixels in width and height
        self.rect.center = (random.randint(40, width-40), 0)   # Position the enemy car at a random x-coordinate at the top of the screen
 
      def move(self):
        global score
        self.rect.move_ip(0, speed)  # Move the enemy car downwards by `speed` pixels per frame, rect.move_ip(x, y) moves the rectangle, in place
        if (self.rect.top > 650): # If the enemy car moves past the bottom of the screen
            score += 1
            self.rect.top = 0
            self.rect.center = (random.randint(40, width - 40), 0)


class Coins(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = image_coin
        self.rect = self.image.get_rect() # Get the rectangle (bounding box) of the enemy car
        #self.rect.inflate_ip(-34, -15)  # Reduces the hitbox by 20 pixels in width and height
        self.rect.center = (random.randint(40, width-40), 0)   # Position the coin at a random x-coordinate at the top of the screen
    def move(self):
        self.rect.move_ip(0, 4)  # Move down
        if self.rect.top > height:
            self.rect.top = 0
            self.rect.center = (random.randint(40, width - 40), 0)
 
 
class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__() 
        self.image = pygame.image.load("player_car.png")
        self.rect = self.image.get_rect() # Get the rectangle (bounding box) of the player car
        self.rect.inflate_ip(-34, -15)  # Reduces the hitbox by 20 pixels in width and height
        self.rect.center = (160, 520)
        
    def move(self):
        pressed_keys = pygame.key.get_pressed()
        #if pressed_keys[K_UP]:
            #self.rect.move_ip(0, -5)
        #if pressed_keys[K_DOWN]:
            #self.rect.move_ip(0,5)
         
        if self.rect.left > 0:
              if pressed_keys[K_LEFT]:
                  self.rect.move_ip(-5, 0)
        if self.rect.right < width:        
              if pressed_keys[K_RIGHT]:
                  self.rect.move_ip(5, 0)
                   
#Setting up Sprites        
Player1 = Player()
Enemy1 = Enemy()
 
#Creating Sprites Groups
enemies = pygame.sprite.Group()
enemies.add(Enemy1)

coins = pygame.sprite.Group()

for i in range(1):
    coin = Coins()
    coins .add(coin)

all_sprites = pygame.sprite.Group()
all_sprites.add(Player1)
all_sprites.add(Enemy1)
all_sprites.add(*coins)



# enemies group: Used to check for collisions with the player.
# all_sprites group: Allows easy updating and drawing of all game objects.


#Adding a new User event 
inc_en_speed = pygame.USEREVENT + 1 # Define a new custom event that increases enemy speed over time
pygame.time.set_timer(inc_en_speed, 1000) # Set a timer to trigger INC_SPEED event every 1000ms (1 second)
# Every second, the enc_en_speed event is triggered, making the game harder over time.

running = True
while running:
    screen.fill(white)
    
    for event in pygame.event.get():
        if event.type == inc_en_speed:    # If the speed increase event is triggered, increase enemy speed
            speed += 0.5     
        if event.type == QUIT:
            running = False
            pygame.quit()
            sys.exit()
 
    screen.blit(background, (0, 0))
    scores = font_small.render(f"Coins: {score_coin}", True, green) # Render the score as text
    screen.blit(scores, (500, 10))
 
    #Moves and Re-draws all Sprites
    for entity in all_sprites:
        screen.blit(entity.image, entity.rect)
        entity.move()
    
    collected = pygame.sprite.spritecollide(Player1, coins, True)  # True delete coin when player collides with it
    for coin in collected:
        score_coin += 1  # increase counter of coins
        new_coin = Coins()
        coins.add(new_coin)
        all_sprites.add(new_coin)

    #To be run if collision occurs between Player and Enemy
    if pygame.sprite.spritecollideany(Player1, enemies):
        pygame.mixer.Sound('crash.wav').play()
        time.sleep(0.5)
                    
        screen.fill(red)
        screen.blit(game_over, (150,250))
           
        pygame.display.update()

        # Remove all sprites from the game
        # This removes both the player and enemy from the game when the player crashes.
        # This ensures that no sprites remain on the screen after the game ends.
        for entity in all_sprites:
            entity.kill() 

        time.sleep(2)
        pygame.quit()
        sys.exit()        
         
    pygame.display.update()
    clock.tick(FPS)