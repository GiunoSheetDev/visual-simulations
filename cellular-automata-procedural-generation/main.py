import pygame
import random


pygame.init()

screenW, screenH = 1200, 1200
screen = pygame.display.set_mode((screenW, screenH))

tileDimension = 2
columns = int(screenW / tileDimension)
rows = int(screenH / tileDimension)

fps = 30
clock = pygame.time.Clock()


def getTiles(noise : int) -> list[list[int]]: #0 WALL BLACK, 1 FLOOR WHITE  
    #NOISE AT ITS BEST BETWEEN 45-65
    tiles = []
    for _ in range(rows):
        tempList = []
        for _ in range(columns):
            num = random.randint(0, 100)
            if num >= noise:
                tempList.append(1)
            else:
                tempList.append(0)
        
        tiles.append(tempList)

    return tiles

def getEmptyTiles() -> list[list[0]]:
    return [[0 for _ in range(rows)] for _ in range(columns)] 

def drawBackground(tiles):
    for i in range(len(tiles)):
        for j in range(len(tiles[0])):
            currentTile = tiles[i][j]
            match currentTile:
                case 0:
                    pygame.draw.rect(screen, (0,0,0), pygame.Rect(tileDimension*i, tileDimension*j, tileDimension, tileDimension))
                case 1:
                    pygame.draw.rect(screen, (255,255,255), pygame.Rect(tileDimension*i, tileDimension*j, tileDimension, tileDimension))

def getNeighbors(tiles, i, j):
    topRight = 0
    top = 0
    topLeft = 0
    left = 0
    right = 0
    bottomLeft = 0
    bottom = 0
    bottomRight = 0
    
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


def updateTiles(tiles, iterations):
    for _ in range(iterations):
        newTiles = getEmptyTiles()
        for i in range(rows):
            for j in range(columns):
                neighbors = getNeighbors(tiles, i, j)
                if neighbors.count(0) > 4:
                    newTiles[i][j] = 0
                else:
                    newTiles[i][j] = 1

        tiles = newTiles

    return tiles
    
    


tiles = getTiles(60)
firstIteration = True
run = True
while run:



    drawBackground(tiles)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

        if event.type == pygame.KEYDOWN: 
            if event.key == pygame.K_ESCAPE:
                run = False
            if event.key == pygame.K_SPACE:
                tiles = updateTiles(tiles, 1)
            
                
            


    pygame.display.update()

