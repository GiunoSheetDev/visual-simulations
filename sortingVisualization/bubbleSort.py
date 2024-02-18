import pygame
import random
from algorithms import *

pygame.init()


fps = 24
clock = pygame.time.Clock()



screenW = 800
screenH = 800
screen = pygame.display.set_mode((screenW, screenH))

numberOfValues = 800

def createList(lenList : int) -> list:
    ls = []
    for i in range(lenList):
        value = random.randint(1, 800)
        ls.append(value)

    return ls


ls = createList(numberOfValues)    
lsCopy = ls.copy()
sortedList = sorted(lsCopy, key= lambda x: x)

columnWidth = int(screenW / len(ls))





def drawBackground(ls : list):
    screen.fill((0,0,0))
    for valueIndex, value in enumerate(ls):
        pygame.draw.rect(screen, (255,0,0), pygame.Rect(columnWidth*valueIndex, 800-value, columnWidth, value))







run = True
while run:
    clock.tick(fps)

    drawBackground(ls)
    
    ls = bubbleSort(ls)
    #ls = bogoSort(ls)
    #ls = quick_sort(ls)
    if ls == sortedList:
        print("Sorted")
    
    

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                run = False
            if event.key == pygame.K_f:
                ls = createList(numberOfValues)
    
    
    pygame.display.update()