import pygame
import Buttons
import Functions


pygame.init()
pygame.mixer.init()
pygame.font.init()

screen = pygame.display.set_mode((1000,600))

Functions.new_audio()

Buttons.all_buttons.append(Buttons.Button((10,350),(650,50),"Textbox",True, lambda: None ))  # Text Box
Buttons.all_buttons.append(Buttons.Button((10,420),(700,50),"Errorbox",True, lambda: None ))  # Error Bar
Buttons.all_buttons.append(Buttons.Button((670,350),(60,50),"Clr",True, lambda: None ))  # Clear Text Box

Buttons.all_buttons.append(Buttons.Button((10,10),(120,50),"Play",True, Functions.current_audio.play)) # Play button
Buttons.all_buttons.append(Buttons.Button((10,90),(120,50),"New",True,Functions.new_audio))  # New file button
Buttons.all_buttons.append(Buttons.Button((10,170),(120,50),"Save",True,Functions.current_audio.save_wave_file))  # Save file button
Buttons.all_buttons.append(Buttons.Button((10,250),(120,50),"Delete",True,Functions.current_audio.del_file))  # Delete file button



play = True
input_string = ''
while play:
    Buttons.display_error_text()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            play = False
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            mousepos = pygame.mouse.get_pos()
            for b in Buttons.all_buttons:
                if b.pressed(mousepos):
                    b.do()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                play = False
            if event.key == pygame.K_BACKSPACE:
                try:
                    input_string = input_string[:-1]
                    Buttons.all_buttons[0].text = input_string
                except:
                    pass
            elif event.key != pygame.K_LSHIFT:
                input_string += pygame.key.name(event.key)
                Buttons.all_buttons[0].text = input_string

            print pygame.key.name(event.key)
    screen.fill((255,255,255))
    screen.blit(Buttons.DrawButtons(),(0,0))
    pygame.display.flip()
pygame.quit()