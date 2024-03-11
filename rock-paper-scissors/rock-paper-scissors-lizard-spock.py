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
    # 0: Rock, 1: Paper, 2: Scissors, 3: Lizard, 4: Spock
    return [[randint(0, 4) for i in range(columns)] for j in range(rows)]

def getEmptyTiles():
    return [[0 for i in range(columns)] for j in range(rows)]


def drawBackground(tiles):
    screen.fill((0,0,0))
    for i in range(len(tiles)):
        for j in range(len(tiles[0])):
            currentTile = tiles[i][j]
            match currentTile:
                case 0:
                    pygame.draw.rect(screen, (235, 125, 91), pygame.Rect(tileDimension*i, tileDimension*j, tileDimension, tileDimension))

                case 1:
                    pygame.draw.rect(screen, (254, 210, 63), pygame.Rect(tileDimension*i, tileDimension*j, tileDimension, tileDimension))

                case 2:
                    pygame.draw.rect(screen, (181, 211, 61), pygame.Rect(tileDimension*i, tileDimension*j, tileDimension, tileDimension))
                
                case 3:
                    pygame.draw.rect(screen, (108, 162, 234), pygame.Rect(tileDimension*i, tileDimension*j, tileDimension, tileDimension))

                case 4:
                    pygame.draw.rect(screen, (68, 34, 136), pygame.Rect(tileDimension*i, tileDimension*j, tileDimension, tileDimension))


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
                # 0: Rock, 1: Paper, 2: Scissors, 3: Lizards, 4: Spock
                case 0: #Rock # 0: Rock, 1: Paper, 2: Scissors, 3: Lizards, 4: Spock
                    papercount = neighbors.count(1)
                    spockcount = neighbors.count(4)
                    if papercount > spockcount and papercount >2:
                        newTiles[i][j] = 1
                    elif spockcount > papercount and spockcount >2:
                        newTiles[i][j] = 4
                    elif spockcount == papercount and papercount >2:
                        choose = randint(0,1)
                        if choose == 1:
                            newTiles[i][j] = 1
                        else: 
                            newTiles[i][j] = 4
                case 1: #Paper # 0: Rock, 1: Paper, 2: Scissors, 3: Lizards, 4: Spock
                    scissorcount = neighbors.count(2)
                    lizardcount = neighbors.count(3)
                    if scissorcount > lizardcount and scissorcount >2:
                        newTiles[i][j] = 2
                    elif lizardcount > scissorcount and lizardcount >2:
                        newTiles[i][j] = 3
                    elif lizardcount == scissorcount and scissorcount >2:
                        choose = randint(0,1)
                        if choose == 1:
                            newTiles[i][j] = 2
                        else: 
                            newTiles[i][j] = 3
                case 2: #Scissors # 0: Rock, 1: Paper, 2: Scissors, 3: Lizards, 4: Spock
                    rockcount = neighbors.count(0)
                    spockcount = neighbors.count(4)
                    if rockcount > spockcount and rockcount >2:
                        newTiles[i][j] = 0
                    elif spockcount > rockcount and spockcount >2:
                        newTiles[i][j] = 4
                    elif spockcount == rockcount and rockcount >2:
                        choose = randint(0,1)
                        if choose == 1:
                            newTiles[i][j] = 0
                        else: 
                            newTiles[i][j] = 4

                case 3: #Lizard # 0: Rock, 1: Paper, 2: Scissors, 3: Lizards, 4: Spock
                    rockcount = neighbors.count(0)
                    scissorscount = neighbors.count(2)
                    if rockcount > scissorscount and rockcount >2:
                        newTiles[i][j] = 0
                    elif scissorscount > rockcount and scissorscount >2:
                        newTiles[i][j] = 2
                    elif scissorscount == rockcount and rockcount >2:
                        choose = randint(0,1)
                        if choose == 1:
                            newTiles[i][j] = 0
                        else: 
                            newTiles[i][j] = 2
    
                case 4: #spock # 0: Rock, 1: Paper, 2: Scissors, 3: Lizards, 4: Spock
                    papercount = neighbors.count(1)
                    lizardcount = neighbors.count(3)
                    if papercount > lizardcount and papercount >2:
                        newTiles[i][j] = 1
                    elif lizardcount > papercount and lizardcount >2:
                        newTiles[i][j] = 3
                    elif lizardcount == papercount and papercount >2:
                        choose = randint(0,1)
                        if choose == 1:
                            newTiles[i][j] = 1
                        else: 
                            newTiles[i][j] = 3
    
    
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
            if event.key == pygame.K_SPACE:
                tiles = getTiles()

    pygame.display.update()

updateTiles(tiles)
