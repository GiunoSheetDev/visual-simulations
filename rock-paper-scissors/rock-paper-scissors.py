import pygame
from random import randint

pygame.init()

screenW, screenH = 800, 800
screen = pygame.display.set_mode((screenW, screenH))

tileDimension = 10
columns = int(screenW/tileDimension)
rows = int(screenH/tileDimension)

fps = 30
clock = pygame.time.Clock()



def getTiles():
    # 0: Rock, 1: Paper, 2: Scissors
    return [[randint(0, 2) for i in range(columns)] for j in range(rows)]

def getEmptyTiles():
    return [[0 for i in range(columns)] for j in range(rows)]


def drawBackground(tiles):
    screen.fill((0,0,0))
    for i in range(len(tiles)):
        for j in range(len(tiles[0])):
            currentTile = tiles[i][j]
            match currentTile:
                case 0:
                    pygame.draw.rect(screen, (155, 52, 235), pygame.Rect(tileDimension*i, tileDimension*j, tileDimension, tileDimension))

                case 1:
                    pygame.draw.rect(screen, (235, 89, 52), pygame.Rect(tileDimension*i, tileDimension*j, tileDimension, tileDimension))

                case 2:
                    pygame.draw.rect(screen, (95, 153, 14), pygame.Rect(tileDimension*i, tileDimension*j, tileDimension, tileDimension))




def getNeighbors(tiles, i, j):
    topRight = None
    top = None
    topLeft = None
    left = None
    right = None
    bottomLeft = None
    bottom = None
    bottomRight = None
    
    
    
    try:
        topLeft = tiles[i-1][j-1]
        top = tiles[i][j-1]
        topRight = tiles[i+1][j-1]
        left = tiles[i-1][j]
        right = tiles[i+1][j]
        bottomLeft = tiles[i-1][j+1]
        bottom = tiles[i][j+1]
        bottomRight = tiles[i+1][j+1]
    except:
        pass

    return [topLeft, top, topRight, left, right, bottomLeft, bottom, bottomRight]


def updateTiles(tiles):
    newTiles = getEmptyTiles()
    for j in range(columns-1):
        for i in range(rows-1):
            currentTile = tiles[i][j]
            neighbors = getNeighbors(tiles, i, j)
            newTiles[i][j] = currentTile #set currentTile in newTiles
            match currentTile:
                # 0: Rock, 1: Paper, 2: Scissors
                case 0:
                    count = neighbors.count(1)
                    if count > 2:
                        newTiles[i][j] = 1
                case 1:
                    count = neighbors.count(2)
                    if count > 2:
                        newTiles[i][j] = 2
                case 2:
                    count = neighbors.count(0)
                    if count > 2:
                        newTiles[i][j] = 0

    return newTiles


tiles = getTiles()

run = True
while run:
    clock.tick(fps)
    
    drawBackground(tiles)
    newTiles = updateTiles(tiles)
    tiles = newTiles


    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                run = False

    pygame.display.update()

updateTiles(tiles)
