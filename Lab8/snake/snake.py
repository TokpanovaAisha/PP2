import pygame
import random
import sys
pygame.init()

width, height = 500, 530
cell_size = 10
velocity = 10

screen = pygame.display.set_mode((width, height))
pygame.display.set_caption('Simple Snake')

clock = pygame.time.Clock()

black = (0, 0 , 0)
green = (0, 255, 0)
red = (255, 0, 0)
gray = (150, 150, 150)
snake_pos = [100, 100]
snake_body = [[100, 100], [80, 100], [60, 100]] # head, body, tail

direction = 'RIGHT'
change_to = direction
score = 0


#Randomly generate food on the screen
food_pos = [random.randrange(1, (width // cell_size)) * cell_size, random.randrange(1, ((height - 30) // cell_size)) * cell_size]
food_gen = True


running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP and direction != 'DOWN':
                change_to = 'UP'
            elif event.key == pygame.K_DOWN and direction != 'UP':
                change_to = 'DOWN'
            elif event.key == pygame.K_RIGHT and direction != 'LEFT':
                change_to = 'RIGHT'
            elif event.key == pygame.K_LEFT and direction != 'RIGHT':
                change_to = 'LEFT'
    
    direction = change_to

    if snake_pos[0] >= width or snake_pos[0] <= 0 or snake_pos[1] >= height or snake_pos[1] <= 30:
        print("Game is over!")
        pygame.quit()
        sys.exit() # if snake faces the wall, then the game is over
    
    
    if direction == 'UP':
        snake_pos[1] -= cell_size
    elif direction == 'DOWN':
        snake_pos[1] += cell_size
    elif direction == 'LEFT':
        snake_pos[0] -= cell_size
    elif direction == 'RIGHT':
        snake_pos[0] += cell_size        # changes the directon


    snake_body.insert(0, list(snake_pos)) # allow to move, insert to the begin of the list new pos

    if snake_pos == food_pos:
        food_gen = False # it means the snake ate food, so it does not remove the tail, so snake grows
        score += 1
        if score % 4 == 0:
            velocity += 2
    else:
        snake_body.pop() # if snake doesn't eat food, its tail removes, allows movement without growth

    if not food_gen: #if there is no food, then it randomly generate
        food_pos = [random.randrange(1, (width // cell_size)) * cell_size, random.randrange(1, ((height -30) // cell_size)) * cell_size]
        food_gen = True 

    if snake_pos in snake_body[1:]:  # if head faces with body
        print("Game is over!")
        running = False  
    

    screen.fill(black)

    for block in snake_body:
        pygame.draw.rect(screen, green, pygame.Rect(block[0], block[1], cell_size, cell_size)) #draw the snake
    
    pygame.draw.rect(screen, red, pygame.Rect(food_pos[0], food_pos[1], cell_size, cell_size)) # draw food
    pygame.draw.rect(screen, gray, pygame.Rect(0, 0, 500, 30)) #draw panel with score and level

    font = pygame.font.Font(None, 20)
    level = score // 3

    # draw score on a screen
    text_surface_score = font.render(f"Score: {score}", True, black) 
    screen.blit(text_surface_score, (15, 10))
    # draw level on a screen
    text_surface_level = font.render(f"Level: {level}", True, black) 
    screen.blit(text_surface_level, (430, 10)) 
    
    pygame.display.flip()
    
    clock.tick(velocity)

pygame.quit()
sys.exit()