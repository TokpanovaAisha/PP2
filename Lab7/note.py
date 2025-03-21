# # Add this somewhere after the event pumping and before the display.flip()
# # pygame.draw.rect(screen, (0, 128, 255), pygame.Rect(30, 30, 60, 60))


# The first argument is the surface instance to draw the rectangle to.
# The second argument is the (red, green, blue) tuple that represents the color to draw with.
# The third argument is a "pygame.Rect instance". 
# The arguments for this constructor are the x and y coordintaes of the top left corner, the width, and the height.

# pygame.QUIT → Нажата кнопка закрытия окна.
# pygame.KEYDOWN → Нажата клавиша.
# pygame.KEYUP → Клавиша отпущена.
# pygame.MOUSEBUTTONDOWN → Нажата кнопка мыши.
# pygame.MOUSEBUTTONUP → Кнопка мыши отпущена.
# pygame.MOUSEMOTION → Движение мыши.

# pygame.display.flip()	Обновляет весь экран (рекомендуется для игр с анимацией)
# pygame.display.update()	Обновляет только нужные области (быстрее, если обновлять маленькие зоны)
# event.key == pygame.K_SPACE    Если это "Пробел"

#RECTANGLE
# pygame.draw.rect(surface, color, pygame.Rect(left, top, width, height))
#CIRCLE
# pygame.draw.circle(surface, color, (x, y), radius)
