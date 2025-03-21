import pygame

pygame.init()
width = 1000
height = 600
running = True
screen = pygame.display.set_mode((width, height))
myfont = pygame.font.Font('Applied_materials\DeliusSwashCaps-Regular.ttf', 40)
billie_songs = ['songs/Billie Eilish - Ocean Eyes.mp3', 'songs/Billie Eilish - No Time To Die.mp3', 
                'songs/Billie Eilish - Idontwannabeyouanymore.mp3', 'songs/Billie Eilish - Burn.mp3']

screen.fill((255, 255, 255))

l = ["Press left arrow to play next song!", 
     "Press right arrow to play previous song!", 
     "Press down arrow to pause the song!", 
     "Press up arrow to unpause the song!"]


pygame.mixer.init()
num_song = 0

pygame.mixer.music.load(billie_songs[num_song])
pygame.mixer.music.play()



def text():
    y = 90
    for i in l:
        text_surface = myfont.render(i, False, (0, 0, 0))
        screen.blit(text_surface, (100, y))
        y += 50
    pygame.display.update()

def next_song():
    global num_song
    num_song = (num_song + 1) % len(billie_songs)
    pygame.mixer.music.load(billie_songs[num_song])
    pygame.mixer.music.play()

def prev_song():
    global num_song
    num_song = (num_song - 1) % len(billie_songs)
    pygame.mixer.music.load(billie_songs[num_song])
    pygame.mixer.music.play()


pygame.mixer.music.set_endevent(pygame.USEREVENT)

while running:

    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            running = False
        elif  event.type == pygame.USEREVENT:
            next_song() 
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                next_song()
            elif event.key == pygame.K_LEFT:
                prev_song()
            elif event.key == pygame.K_DOWN:
                pygame.mixer.music.pause()
            elif event.key == pygame.K_UP:
                pygame.mixer.music.unpause()
        
        text()
            
pygame.quit()
            