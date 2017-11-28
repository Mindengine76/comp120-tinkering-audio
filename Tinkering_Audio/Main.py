import pygame
import Buttons
import Functions


pygame.init()
pygame.mixer.init()
pygame.font.init()

screen = pygame.display.set_mode((800,500))

current_audio = Functions.Audio(4000.0,44100.0,132000,1000.0)

Buttons.all_buttons.append(Buttons.Button((10,10),(120,50),"Play", current_audio.play)) #ADD PLAY BUTTON


play = True
while play:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            done=True
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            mousepos = pygame.mouse.get_pos()
            for b in Buttons.all_buttons:
                if b.pressed(mousepos):
                    b.do()
        screen.fill((255,255,255))
        screen.blit(Buttons.DrawButtons(),(0,0))
        pygame.display.flip()