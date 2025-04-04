import pygame
import sys
import math

pygame.init()
width, height = 1000, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption('Simple paint')

white = (255, 255, 255)
black = (0, 0 , 0)
green = (0, 255, 0)
red = (255, 0, 0)
blue = (0, 0, 255)
gray = (200, 200, 200)
fo = (80, 80, 80)

class Button:
    def __init__(self, x, y, width, height, text, color, action):
        self.rect = pygame.Rect(x, y, width, height)
        self.text= text
        self.color = color
        self.action = action
        self.font = pygame.font.Font(None, 25)

    def draw(self, screen):
        pygame.draw.rect(screen, self.color, self.rect)
        text_surface = self.font.render(self.text, True, white)  # Render text in white
        text_rect = text_surface.get_rect(center=self.rect.center)  # Center the text inside the button
        screen.blit(text_surface, text_rect)  # Draw text on the screen
        
    def check_action(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            if self.rect.collidepoint(event.pos): # checks if the mouse click happened inside the button 
                self.action()                     # event.pos gives the (x, y) position of the mouse click.

drawing = False
brush_color = black
geometric_shapes = 'Curve'
begin_pos = None
final_pos = None

def set_black():
    global brush_color
    brush_color = black
def set_green():
    global brush_color
    brush_color = green
def set_red():
    global brush_color
    brush_color = red
def set_blue():
    global brush_color
    brush_color = blue
def clear_screen():
    screen.fill(white)
def exit_app():
    pygame.quit()
    sys.exit()
def draw_rectangle():
    global geometric_shapes
    geometric_shapes = 'Rect'
def draw_circle():
    global geometric_shapes
    geometric_shapes = 'Circle'
def eraser():
    global geometric_shapes
    geometric_shapes = 'Erase'
    global brush_color
    brush_color = white
def curve():
    global geometric_shapes
    geometric_shapes = 'Curve'

# def __init__(self, x, y, width, height, text, color, action)
buttons = [
    Button(10, 10, 60, 30, 'Black', black, set_black),
    Button(80, 10, 60, 30, 'Green', green, set_green),
    Button(150, 10, 60, 30, 'Red', red, set_red),
    Button(220, 10, 60, 30, 'Blue', blue, set_blue),
    Button(290, 10, 60, 30, 'Rect', fo, draw_rectangle),
    Button(360, 10, 60, 30, 'Circle', fo, draw_circle),
    Button(430, 10, 60, 30, 'Erase', fo, eraser),
    Button(500, 10, 60, 30, 'Clear', gray, clear_screen),
    Button(570, 10, 60, 30, 'Exit', gray, exit_app),
    Button(640, 10, 60, 30, 'Curve', gray, curve)
]

clear_screen()


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            # Left mouse button == 1
            # Middle mouse button (scroll wheel click) == 2
            # Right mouse button == 3
            # Scroll up == 4
            # Scroll down == 5 
            if event.button == 1:
                drawing = True
                begin_pos = event.pos

        elif event.type == pygame.MOUSEBUTTONUP:
            if event.button == 1:
                drawing = False
                final_pos = event.pos
        
            if geometric_shapes == 'Rect':
                # Rect(left, top, width, height) -> Rect
                # rect(surface, color, rect, width=0, border_radius=0, border_top_left_radius=-1, border_top_right_radius=-1, border_bottom_left_radius=-1, border_bottom_right_radius=-1)
                x1, y1 = begin_pos
                x2, y2 = final_pos
                rect_x, rect_y = min(x1, x2), min(y1, y2)   # The rectangle must start at the smallest x and y values to ensure it is drawn correctly
                rect_width, rect_height = abs(x2 - x1), abs(y2 - y1)
                pygame.draw.rect(screen, brush_color, (rect_x, rect_y, rect_width, rect_height), 2)

            elif geometric_shapes == 'Circle':
                radius = int(math.sqrt(((final_pos[0] - begin_pos[0])**2) + ((final_pos[1] - begin_pos[1])**2)))
                #circle(surface, color, center, radius, width=0, draw_top_right=None, draw_top_left=None, draw_bottom_left=None, draw_bottom_right=None)
                pygame.draw.circle(screen, brush_color, begin_pos, radius, 2)

        for button in buttons:
            button.check_action(event)


    pygame.draw.rect(screen, gray, (0, 0, width, 50))
    if drawing  and (geometric_shapes == 'Curve' or geometric_shapes == 'Erase'):
        mouse_x , mouse_y = pygame.mouse.get_pos()  # Returns the x and y position of the mouse cursor.
        if mouse_y > 50:  
            pygame.draw.circle(screen, brush_color, (mouse_x, mouse_y), 5)   

    
    for button in buttons:
        button.draw(screen) # Draw each button

    pygame.display.flip()

