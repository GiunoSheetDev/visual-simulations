import pygame
from classes.particle import Particle
from classes.solids.dynamic.sand import Sand
from classes.solids.solid import Solid
from random import randint

pygame.init()

screenW, screenH = 800, 800
screen = pygame.display.set_mode((screenW, screenH))

fps = 30
clock = pygame.time.Clock()

tileDimension = 20
rows = int(screenH/tileDimension)
columns = int(screenW/tileDimension)

currentId = 0




def getMousePos() -> tuple: 
    mousex, mousey = pygame.mouse.get_pos()
    currentTile = (int(mousex/tileDimension), int(mousey/tileDimension))
    return currentTile

def getEmptyTiles() -> list[list]:
    tiles = [[0 for i in range(columns)] for j in range(rows)]
    return tiles

def drawBackground(tiles: list[list]) -> None:
    screen.fill((0,0,0))
    for i in range(rows):
        for j in range(columns):
            currentTile = tiles[i][j]
            if isinstance(currentTile, Particle):
                pygame.draw.rect(screen, currentTile.color, pygame.Rect(tileDimension*i, tileDimension*j, tileDimension, tileDimension))


def updateTiles(tiles: list[list]) -> list[list]:
    for j in range(columns-1, -1, -1):
        for i in range(rows-1, -1, -1):
            currentTile = tiles[i][j]
            
            if isinstance(currentTile, Particle):
                currentTile.update(tiles)
                
            




def mainLoop():
    
    tiles = getEmptyTiles()
    run = True
    pygame.event.set_grab(True)
    
    while run:
        
        clock.tick(fps)
        drawBackground(tiles)
        updateTiles(tiles)
        mousePos = getMousePos()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    run = False

        if pygame.mouse.get_pressed()[0]:
            if currentId == 0: #Sand
                tiles[mousePos[0]][mousePos[1]] = Sand(mousePos[0], mousePos[1])

        pygame.display.update()



if __name__ == "__main__":
    mainLoop()