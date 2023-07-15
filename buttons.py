import pygame as pg
from screen import screen
#from snake import screen


#font = pygame.font.SysFont(None, 24)


class Text:


    def __init__(self, x, y, size, color, text) -> None :
        self.x = x
        self.y = y
        self.color = color
        self.font = pg.font.SysFont(None, size)
        self.text = text
        self.width = self.font.size(self.text)[0]
        self.height = self.font.size(self.text)[1]
    
    def draw(self):
        img = self.font.render(self.text, True, self.color)
        screen.blit(img, (self.x, self.y))
        #( self.color, (self.x, self.y, self.size, self.size))



class Button:
    

    def __init__ (self, x, y, width, height, text, color, text_color):
        self.x = x
        self.y = y
        self.height = height
        self.color = color
        self.width = width
        self.text = Text(x, y, int(height * 0.9), text_color, text)
        self.text.x += (width - self.text.width) / 2
        self.text.y += (height - self.text.height) / 2

    def draw(self):
        pg.draw.rect(screen, self.color, (self.x, self.y, self.width, self.height))
        self.text.draw()

