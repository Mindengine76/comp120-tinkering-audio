import pygame

all_buttons = []

def DrawButtons():
    myfont = pygame.font.SysFont("monospace", 15)
    surf = pygame.Surface((800,500))
    surf.fill((0,0,1))
    for b in all_buttons:
        pygame.draw.rect(surf,(0,0,0),(b.location[0],b.location[1],b.size[0],b.size[1]),2)

        label = myfont.render("Play", 1, (0, 0, 0))
        surf.blit(label, (b.location[0]+ (b.size[0]/2)-len(b.text)-10,b.location[1] + b.size[1]/2 - 8))

    surf.set_colorkey((0,0,1))
    return surf


class Button:
    text = ""
    location=[0,0]
    size = [0,0]
    function =  lambda x : None

    def __init__(self,loc,size,text,func):
        self.location = loc
        self.size = size
        self.function = func
        self.text = text


    def pressed(self,mouse_loc):
        if mouse_loc[0] > self.location[0] and mouse_loc[0] < self.location[0]+self.size[0]:
            if mouse_loc[1] > self.location[1] and mouse_loc[1] < self.location[1]+self.size[1]:
                return True
        return False

    def do(self):
        self.function()


