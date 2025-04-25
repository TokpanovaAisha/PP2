import pygame
import random
import psycopg2
import sys


conn = psycopg2.connect(
    dbname="postgres",
    user="postgres",
    password="AlIyA2015",
    host="localhost",
    port="5432"
)
cur = conn.cursor()

your_name = input("Enter your name: ")        # Вводит имя

cur.execute("SELECT id FROM users WHERE user_name = %s;", (your_name,)) # из таблицы users выберает id с именем your_name
user = cur.fetchone() # Возвращает только одну строку с именем your_name(выведет только id например(3,))

# cur.execute("SELECT * FROM user_score WHERE user_id = %s", (user_id,))
# save = cur.fetchone()

# user_id это в таблице user_score
if user:    # если существует 

    print(f"User '{your_name}' already exists!")
    cur.execute("SELECT * FROM user_score WHERE user_id = %s;", (user[0],)) # выбирает все столбцы из user_score по id 
    save = cur.fetchone() # например(4, 20, 5, "UP", 30, 20, ..., 15) 
    print(f"{your_name}, your last level and score: {save[2]} and {save[1]}")
    
else: # если не существует 
    print(f"Welcome, {your_name}!")
    cur.execute("INSERT INTO users (user_name, state) VALUES (%s, %s);", (your_name, None))
    conn.commit()
    save = False


pygame.init()

        

def generate_food():
    while True:
        pos = [random.randrange(1, (width // cell_size)) * cell_size, random.randrange(1, ((height -30) // cell_size)) * cell_size]
        if pos not in snake_body:
            return pos
        

def from_table(body_text):
    return [list(map(int, pos.split(':'))) for pos in body_text.split(',') if pos]

def to_table(body):
    return ','.join(f'{x}:{y}' for x, y in body)

width, height, cell_size = 500, 530, 10 
velocity = 10
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption('Simple Snake')
clock = pygame.time.Clock()

black = (0, 0 , 0)
green = (0, 255, 0)
red = (255, 0, 0)
gray = (150, 150, 150)


if save:   
    _, score, level, direction, x, y, body_str, velocity = save
    snake_pos = [x, y]
    snake_body = from_table(body_str)
else:
    score, level, velocity = 0, 0, 10
    direction = 'RIGHT'
    snake_pos = [100, 100]
    snake_body = [[100, 100], [80, 100], [60, 100]]
    

change_to = direction

food_gen = False
food_pos = generate_food()

cur.execute("SELECT id FROM users WHERE user_name = %s;", (your_name,))
user_id = cur.fetchone()[0]
running = True
paused = False

cur.execute("SELECT * FROM users WHERE user_name = %s;", (your_name,))
state_us = cur.fetchone()[2]

if save:
    if state_us == "Dead":
        restart = True

        font = pygame.font.Font(None, 36)
        screen.fill(black)
        text = font.render("Press R to restart the game", True, green)
        screen.blit(text, (width // 2 - text.get_width() // 2, height // 2 - 40))
        pygame.display.flip()

        while restart:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_r:
                        score, level, velocity = 0, 0, 10
                        direction = 'RIGHT'
                        snake_pos = [100, 100]
                        snake_body = [[100, 100], [80, 100], [60, 100]]
                        restart = False
    elif state_us == "Pause":
        start = True

        font = pygame.font.Font(None, 36)
        screen.fill(black)
        text = font.render("Press C to continue the game", True, green)
        screen.blit(text, (width // 2 - text.get_width() // 2, height // 2 - 30))
        text1 = font.render("Press R to restart the game ", True, green)
        screen.blit(text1, (width // 2 - text.get_width() // 2 +30, height // 2 + 20 ))
        pygame.display.flip()

        while start:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_c:
                        _, score, level, direction, x, y, body_str, velocity = save
                        snake_pos = [x, y]
                        snake_body = from_table(body_str)
                        start = False
                    if event.key == pygame.K_r:
                        score, level, velocity = 0, 0, 10
                        direction = 'RIGHT'
                        snake_pos = [100, 100]
                        snake_body = [[100, 100], [80, 100], [60, 100]]
                        start = False
 

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
            elif event.key == pygame.K_p:
                # Pause and save
                cur.execute("""
                    INSERT INTO user_score (user_id, score, level, direction, snake_head_x, snake_head_y, snake_body, velocity)
                    VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
                    ON CONFLICT (user_id)
                    DO UPDATE SET score=%s, level=%s, direction=%s, snake_head_x=%s, snake_head_y=%s, snake_body=%s, velocity=%s
                """, (
                    user_id, score, level, direction, snake_pos[0], snake_pos[1],
                    to_table(snake_body), velocity,
                    score, level, direction, snake_pos[0], snake_pos[1],
                    to_table(snake_body), velocity
                ))
                cur.execute("UPDATE users SET state = %s WHERE id = %s;", ('Pause', user_id))
                conn.commit()
                print("Game saved!")
                paused = True
                
    
    if paused:
        font = pygame.font.Font(None, 36)
        text = font.render("Game paused. Press any key to continue.", True, green)
        while paused:
            screen.fill(black)
            screen.blit(text, (width // 2 - text.get_width() // 2, height // 2))
            pygame.display.flip()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                elif event.type == pygame.KEYDOWN:
                    paused = False
    
    direction = change_to

    if (snake_pos[0] >= width or snake_pos[0] <= 0 or snake_pos[1] >= height or snake_pos[1] <= 30) or (snake_pos in snake_body[1:]):
        cur.execute("""
                    INSERT INTO user_score (user_id, score, level, direction, snake_head_x, snake_head_y, snake_body, velocity)
                    VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
                    ON CONFLICT (user_id)
                    DO UPDATE SET score=%s, level=%s, direction=%s, snake_head_x=%s, snake_head_y=%s, snake_body=%s, velocity=%s
                    """, 
                    (user_id, score, level, direction, snake_pos[0], snake_pos[1],
                    to_table(snake_body), velocity,
                    score, level, direction, snake_pos[0], snake_pos[1],
                    to_table(snake_body), velocity
                    ))
        cur.execute("UPDATE users SET state = %s WHERE id = %s;", ('Dead', user_id))
        conn.commit()
        
        print("You're dead! Your game data is saved")
        
        cur.close()
        conn.close()
        pygame.quit()
        sys.exit() # if snake faces the wall, then the game is over



    # if snake_pos in snake_body[1:]:  # if head faces with body
    #     print("Game is over!")
    #     running = False  
    
    
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
            level += 1
            velocity += 2
    else:
        snake_body.pop() # if snake doesn't eat food, its tail removes, allows movement without growth

    if not food_gen:
        food_pos = generate_food()
        food_gen = True
        
    
    

    screen.fill(black)

    for block in snake_body:
        pygame.draw.rect(screen, green, pygame.Rect(block[0], block[1], cell_size, cell_size)) #draw the snake
    
    pygame.draw.rect(screen, red, pygame.Rect(food_pos[0], food_pos[1], cell_size, cell_size)) # draw food
    pygame.draw.rect(screen, gray, pygame.Rect(0, 0, 500, 30)) #draw panel with score and level

    font = pygame.font.Font(None, 20)
    

    # draw score on a screen
    text_surface_score = font.render(f"Score: {score}", True, black) 
    screen.blit(text_surface_score, (15, 10))
    # draw level on a screen
    text_surface_level = font.render(f"Level: {level}", True, black) 
    screen.blit(text_surface_level, (430, 10)) 
    
    pygame.display.flip()
    
    clock.tick(velocity)

cur.close()
conn.close()
pygame.quit()
sys.exit()