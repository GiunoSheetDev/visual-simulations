import pygame
from particle import *
from random import randint

pygame.init()

screenW = 800
screenH = 800
screen = pygame.display.set_mode((screenW, screenH))


fps = 5
clock = pygame.time.Clock()

tileDimension = 50
rows = int(screenH/tileDimension)
columns = int(screenW/tileDimension)


def drawBackground(tiles: list[list]):
    screen.fill((0,0,0))
    for i in range(rows):
        for j in range(columns):
            
            currentTile = tiles[i][j]
            if isinstance(currentTile, Particle):
                referenceTypeId = currentTile.id

                match referenceTypeId:
                    case 0: #Sand
                        pygame.draw.rect(screen, currentTile.color, pygame.Rect(tileDimension*i, tileDimension*j, tileDimension, tileDimension))
                   


def getEmptyGrid():
    tiles = [[0 for i in range(rows)] for j in range(columns)]
    return tiles


def updateGrid(tiles):
    newGrid = getEmptyGrid()
    
    for i in range(rows-1, -1, -1):
        for j in range(columns):
            currentTile = tiles[i][j]
            print(currentTile)
            








'''            
            currentTile = tiles[i][j]

            if j == (rows-1): #non checka la bottom 
               newGrid[i][j] = currentTile 

            else:
                if isinstance(currentTile, Particle):
            

                    referenceTypeId = currentTile.id
                

                    match referenceTypeId:
                        case 0: #Sand
                        

                            bottom = tiles[i][j+1]
                            if bottom == 0: #nothing on the bottom
                            
                                tiles[i][j] = 0
                                newGrid[i][j+1] = currentTile

                        
                            else: #check if bottomTile is traversable, if yes go down, if not go downLeft or downRight
                                bottomState = bottom.state
                                print(bottom, bottomState)
                            
                                if bottomState == 0: #bottom tile is solid, not traversable
                                    direction = randint(1,2)
                                    if direction == 1:
                                        bottomLeft = tiles[i-1][j+1]
                                        isBottomLeftParticle = isinstance(bottomLeft, Particle)
                                        if isBottomLeftParticle:
                                            if bottomLeft.state != 0: #if is liquid or gas
                                                newGrid[i-1][j] = bottomLeft
                                                newGrid[i-1][j+1] = currentTile
                                                continue #loop goes to next iteration, particle has moved
                                        else:
                                            newGrid[i-1][j+1] = currentTile
                                            continue
                                    else:
                                        bottomRight = tiles[i+1][j+1]
                                        isBottomRightParticle = isinstance(bottomRight, Particle)
                                        if isBottomRightParticle:
                                            if bottomRight.state != 0: #if is liquid or gas
                                                newGrid[i-1][j] = bottomRight
                                                newGrid[i+1][j+1] = currentTile
                                                continue
                                        else:
                                            newGrid[i+1][j+1] = currentTile
                                            continue

                                    #This following statement should be reachable only if particle cant move 
                                    newGrid[i][j] = currentTile

                                else: #bottomTile is traversable
                                    newGrid[i][j] = newGrid[i][j+1] #fluid goes up, sand goes down
                                    newGrid[i][j+1] = currentTile

'''
                #i = y TOP 2 BOTTOM
                #j = x LEFT 2 RIGHT

                



    
    




tiles = getEmptyGrid()
tiles[2][2] = Sand(id=0)
tiles[2][3] = Sand(id=0)
tiles[2][4] = Sand(id=0)
print(tiles)
run = True
while run:

    #clock.tick(fps)
    #print(tiles[2]) 
    #drawBackground(tiles= tiles)
    newTiles = updateGrid(tiles)
    tiles = newTiles



    #event handler
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                run = False


    
