#Created by Luca Cottone on 2/17/26
#This is the client part of PyRace
import socket
import threading
import json
import pygame

width = 500
height = 500
win = pygame.display.set_mode((width,height))
pygame.display.set_caption("Client") #Labes window

clientNumber = 0

class Player():
    #initiates all the variables needed to move the rectangle
    def __init__(self, x, y, width, height, color):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.color = color
        self.rect = (x,y,width,height)
        self.vel = 3
    
    #Draws rectangle
    def draw(self, win):
        pygame.draw.rect(win, self.color, self.rect)
    
    #recognizes if key is pressed and sets the new rectangle dimensions
    def move(self):
        key = pygame.key.get_pressed()

        if key[pygame.K_LEFT]:
            self.x -= self.vel
        if key[pygame.K_RIGHT]:
            self.x += self.vel
        if key[pygame.K_UP]:
            self.y -=self.vel
        if key[pygame.K_DOWN]:
            self.y += self.vel
        self.rect = (self.x, self.y, self.width, self.height) #redrawing rectangle dimensions

#draws window
def redrawWindow(win,player):
    win.fill((255,255,255))
    player.draw(win)
    pygame.display.update()

def main():
    run = True
    p = Player(50,50,100,100,(0,255,0))
    clock = pygame.time.Clock()
    while run:
        clock.tick(60) #refresh rate
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()
        p.move()
        redrawWindow(win, p)

main()