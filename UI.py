import pygame
import Buttons
import Audio

# todo Setting audio doesn't work.


pygame.init()
pygame.mixer.init()
pygame.font.init()

screen = pygame.display.set_mode((1000,600))

Audio.new_audio()

""" Text Boxes """
Buttons.all_buttons.append(Buttons.Button((10,350),(650,50),"",True, lambda: None))  # Text Box [0]
Buttons.all_buttons.append(Buttons.Button((10,420),(700,50),"Errorbox",True, lambda: None))  # Error Bar [1]
Buttons.all_buttons.append(Buttons.Button((670,350),(60,50),"Clr",True, Buttons.clear_textbox))  # Clear Text Box [2]
""" Data Boxes """
Buttons.all_buttons.append(Buttons.Button((10,10),(120,50),"Play",True, Audio.current_audio.play)) # Play button [3]
Buttons.all_buttons.append(Buttons.Button((10,90),(120,50),"New",True,Audio.new_audio))  # New file button [4]
Buttons.all_buttons.append(Buttons.Button((10,170),(120,50),"Save",True,Audio.current_audio.btn_save))  # Save file button [5]
Buttons.all_buttons.append(Buttons.Button((10,250),(120,50),"Del File",True,Audio.current_audio.del_file))  # Delete file button [6]
""" Function Boxes """
Buttons.all_buttons.append(Buttons.Button((180,10),(180,50),"Inc Volume",True,Audio.current_audio.increase_volume))  # increase volume [7]
Buttons.all_buttons.append(Buttons.Button((180,90),(180,50),"Flatten Volume",True,Audio.current_audio.flatten))  # flatten button [8]
Buttons.all_buttons.append(Buttons.Button((180,170),(180,50),"Cut",True,Audio.current_audio.cut))  # Cut button [9]
Buttons.all_buttons.append(Buttons.Button((180,250),(180,50),"Linear Increase",True,Audio.current_audio.linear_vol))  # linear increase vol button [10]

Buttons.all_buttons.append(Buttons.Button((410,10),(180,50),"Exponential Increase",True,Audio.current_audio.linear_vol))  # Exponential increase [11]
Buttons.all_buttons.append(Buttons.Button((410,90),(180,50),"Echo",True,Audio.current_audio.linear_vol))  # Add Echo [12]
#Buttons.all_buttons.append(Buttons.Button((410,170),(180,50),"Echo",True,Audio.current_audio.linear_vol))
#Buttons.all_buttons.append(Buttons.Button((410,250),(180,50),"Linear Increase",True,Audio.current_audio.linear_vol))



""" Pygame Loop """
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
                    Buttons.all_buttons[0].text = Buttons.all_buttons[0].text[:-1]
                except:
                    pass
            elif event.key != pygame.K_LSHIFT:
                Buttons.all_buttons[0].text += pygame.key.name(event.key)

            print pygame.key.name(event.key)
    screen.fill((255,255,255))
    screen.blit(Buttons.draw_buttons(),(0,0))
    pygame.display.flip()
pygame.quit()