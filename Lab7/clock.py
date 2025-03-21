import pygame, datetime

pygame.init()

clock = pygame.time.Clock()
width = 800
height = 600
screen = pygame.display.set_mode((width, height))
screen.fill((255, 255, 255))
running = True
mickey = pygame.image.load('Applied_materials\mickey.jpg')
minutes = pygame.image.load('Applied_materials\\right_hand.png')
seconds = pygame.image.load('Applied_materials\left_hand.png')



rect_sec = seconds.get_rect(center=(400, 300))  
rect_min = minutes.get_rect(center=(400, 300))  

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.blit(mickey, (0, 0))

    n = datetime.datetime.now()
    angle_sec = n.second * 6
    angle_min = n.minute * 6 + n.second * 0.1 

    
    rotated_seconds = pygame.transform.rotate(seconds, -angle_sec)  # Поворачиваем
    changing_rect_sec = rotated_seconds.get_rect(center = rect_sec.center)  # Корректируем позицию
    screen.blit(rotated_seconds, changing_rect_sec.topleft)  # Рисуем повернутое изображение


    rotated_minutes = pygame.transform.rotate(minutes, -angle_min)  # Поворачиваем
    changing_rect_min = rotated_minutes.get_rect(center = rect_min.center)  # Корректируем позицию
    screen.blit(rotated_minutes, changing_rect_min.topleft)  # Рисуем повернутое изображение


    pygame.display.flip()
    clock.tick(60)
    
pygame.quit()