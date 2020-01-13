import pygame
import sys
from variables import *

class button():
    def __init__(self, x, y, width, height, text):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.text = text
        self.MouseIsOver = False
        self.ButtonClicked = False
        self.addtextLine = False
    def draw(self):
        #Remember rectangle is drawn by (x, y) of top left corner.
        pygame.draw.rect(DISPLAY, GREY, (self.x, self.y, self.width, self.height)) #draw.rect(DISPLAY, COLOUR, (x, y, width, height))
    def isOver(self, event):
        #Checks if the mouse is over the button.
        #If the mouse is within the rectangles region of coordinates as represented by the if statements boundary, redraw the screen.
        #And create a new rectangle with the same position, to make it seem as if you are hovering over the button.
        if event.type == pygame.MOUSEMOTION:
            self.MouseIsOver = True
            position = pygame.mouse.get_pos()
            if (position[0] >= self.x and position[0] <= (self.x + self.width)) and (position[1] >= self.y and position[1] <= (self.y + self.height)):
                DISPLAY.fill(WHITE, (self.x, self.y, self.width, self.height))
                pygame.draw.rect(DISPLAY, HOVER_COLOUR, (self.x, self.y, self.width, self.height))
            else:
                self.MouseIsOver = False
                DISPLAY.fill(WHITE, (self.x, self.y, self.width, self.height))
                pygame.draw.rect(DISPLAY, GREY, (self.x, self.y, self.width, self.height))
    def checkClick(self, event):
        #event.button value shows the mouse button clicked: 1 is left, 3 is right.
        #If the mouse is hovering over the button and left-clicked, it is considered pressed!
        #For now, an output is printed to test this.
        if self.MouseIsOver == True and (event.type == pygame.MOUSEBUTTONDOWN and event.button == 1):
            print(event)
            print("Button clicked!")
            self.ButtonClicked = True
        else:
            self.ButtonClicked = False
    def addText(self, addtextLine):
        #Text position is the same position as the button
        #Font will be a pre-installed font, for now an example is used.
        #Blitted on the screen as a surface.
        #Remember addtext is a list! Meant to draw strings on new lines.
        self.addtextLine = addtextLine
        text_pos = ((self.x), (self.y))
        font = pygame.font.SysFont("courier new", 40)
        text = font.render(self.text, True, TEXT_COLOUR)
        DISPLAY.blit(text, text_pos)
        if addtextLine != False:
            count = 50
            #Adding new lines by use of a list and iterating through it.
            #The count is used to increase the Y position every time so a "newline" effect is created.
            for s in addtextLine:
                text_pos = ((self.x), (self.y) + count)
                addendum = font.render(s, True, TEXT_COLOUR)
                DISPLAY.blit(addendum, text_pos)
                count += 50
    def update(self, event):
        #Updates the button by doing all of above; run every frame.
        self.isOver(event)
        self.checkClick(event)
        self.addText(self.addtextLine)
