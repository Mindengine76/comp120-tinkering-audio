import pygame
import time

all_buttons = []
error_start_time = 0
error_length = 0


def clear_textbox():
    all_buttons[0].text = ""


def btn_action_get_time11():
    try:
        all_buttons[11].text = str(float(all_buttons[0].text))+"s"
    except:
        display_error_text("Please input valid number")


def btn_action_get_time13():
    try:
        a = float(all_buttons[0].text)
        if a <= float(all_buttons[11].text[-1]):
            display_error_text("Please input larger number")
            return
        all_buttons[13].text = str(a) + "s"
    except:
        display_error_text("Please input valid number")


def display_error_text(text="", seconds=10):  # todo Get this working
    global error_start_time, error_length
    if text != "":
        error_start_time == time.clock()
        error_length = seconds
        all_buttons[1].visible = True
        all_buttons[1].text = text
    elif time.clock >= error_start_time + error_length:
        all_buttons[1].visible = False


def draw_buttons():
    myfont = pygame.font.SysFont("monospace", 20)
    surf = pygame.Surface((800,500))
    surf.fill((0,0,1))
    for b in all_buttons:
        if b.is_visible:
            if b.is_pressed:  # todo get this working
                pygame.draw.rect(surf, (50, 50, 50), (b.location[0], b.location[1], b.size[0], b.size[1]), 2)
            else:
                pygame.draw.rect(surf, (0, 0, 0), (b.location[0], b.location[1], b.size[0], b.size[1]), 2)
            label = myfont.render(b.text, 1, (0, 0, 0))
        else:
            label = myfont.render("", 1, (0, 0, 0))
        surf.blit(label, (b.location[0]+ (b.size[0]/2)-len(b.text)*6,b.location[1] + b.size[1]/2 - 8))  # Centers text in button

    surf.set_colorkey((0,0,1))
    return surf.convert()


class Button:
    is_visible = True
    is_pressed = False
    text = ""
    location=[0,0]
    size = [0,0]
    function = lambda x : None

    def __init__(self,loc,size,text,vis,func):
        self.location = loc
        self.size = size
        self.function = func
        self.text = text
        self.is_visible = vis

    def is_text_int(self):
        if self.name.isdigit():
            return int(self.name)

    def pressed(self,mouse_loc):

        if mouse_loc[0] > self.location[0] and mouse_loc[0] < self.location[0]+self.size[0]:
            if mouse_loc[1] > self.location[1] and mouse_loc[1] < self.location[1]+self.size[1]:
                self.is_pressed = True
                return True
        self.is_pressed = False
        return False

    def do(self):
        self.function()

