import pygame

pygame.init()
sc_width = 500
sc_height = 500
screen = pygame.display.set_mode((sc_width, sc_height))
clock = pygame.time.Clock()

running = True
x = 200
y = 50
# pygame.draw.circle(surface, color, (x, y), radius)

while running:
    screen.fill((255, 255, 255)) 

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        
    pressed_arr = pygame.key.get_pressed()
    if pressed_arr[pygame.K_UP] and y-25 > 0: y -= 20
    if pressed_arr[pygame.K_DOWN] and y+25 < sc_height: y += 20
    if pressed_arr[pygame.K_RIGHT] and x+25 < sc_width: x += 20
    if pressed_arr[pygame.K_LEFT] and x-25 > 0: x -= 20

    pygame.draw.circle(screen, (255, 0, 0 ), (x, y), 25)
    pygame.display.flip()
    clock.tick(60)

    
pygame.quit()
        