import pygame
import random
pygame.init()

screenWidth = 800
screenHeigth = 800 #SCREEN MUST BE A SQUARE
screen = pygame.display.set_mode((screenWidth, screenHeigth))

fps = 1000
clock = pygame.time.Clock()



tiles = []
tileDimension = 2
columns = int(screenWidth / tileDimension)
rows = int(screenHeigth / tileDimension)
    

def drawBackground():
    screen.fill((0,0,0))
    
    '''
    for i in range(rows):
        pygame.draw.line(screen, (255,255,255), (0, 0 + tileDimension * i), (screenWidth, 0 + tileDimension * i), 1)

    for i in range(columns):
        pygame.draw.line(screen, (255, 255, 255), (0+tileDimension*i, 0), (0+tileDimension*i, screenHeigth), 1)

    '''
        
    for i in range(len(tiles)):
        for j in range(len(tiles[i])):
            if tiles[i][j] == 1:
                pygame.draw.rect(screen, (237, 155, 40), pygame.Rect(tileDimension*i, tileDimension*j, tileDimension, tileDimension))

            
def getTiles():
    l = []
    for i in range(rows):
        tempList = []
        for j in range(columns):
            tempList.append(0)

        l.append(tempList)
    
    return l



def updateTiles(tiles):
    newTiles = getTiles()
    for i in range(columns):
        for j in range(rows):
            try: #DELETE SAND THAT GOES OFF SCREEN TO THE SIDES
                if j == (rows-1): #CANT FALL BELOW LAST ROW
                    if tiles[i][j] == 1:
                        newTiles[i][j] = 1
                
                    
                else:
                    if tiles[i][j] == 1: #GO DOWN THE GRID
                        
                        if tiles[i][j+1] != 1: #IF THERE'S NOTHING BELOW
                            tiles[i][j] = 0
                            newTiles[i][j+1] = 1

                        else: #IF THERE'S ANOTHER FILLED TILE BELOW
                            #CHECK IF CAN GO DIAGONALLY
                            diagonalLeft = tiles[i-1][j+1]
                            diagonalRight = tiles[i+1][j+1]



                            if diagonalLeft == 0 and diagonalRight == 0: #IF CAN GO TO EITHER DIRECTION
                                chooseDirection = random.randint(1,2)
                                if chooseDirection == 1: #GO LEFT
                                    newTiles[i-1][j+1] = 1
                                else: #GO RIGHT
                                    newTiles[i+1][j+1] = 1

                            elif diagonalLeft == 1 and diagonalRight == 0: #CAN ONLY GO RIGHT  
                                newTiles[i+1][j+1] = 1
                            
                            elif diagonalLeft == 0 and diagonalRight == 1: #CAN ONLY GO LEFT    
                                newTiles[i-1][j+1] = 1
                        
                            else:
                                newTiles[i][j] = 1

            except : pass
    return newTiles


def mousePos():
    mousex = pygame.mouse.get_pos()[0]
    mousey = pygame.mouse.get_pos()[1]
    
    currentTile = (int(mousex/tileDimension), int(mousey/tileDimension))
    return currentTile



tiles = getTiles()






run = True
while run:
    clock.tick(fps)

  
    drawBackground()
    newTiles = updateTiles(tiles)
    tiles = newTiles

    currentTile = mousePos()
    
    
    



    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                run = False
    
    if pygame.mouse.get_pressed()[0]:
        if tiles[currentTile[0]][currentTile[1]] == 0:
            tiles[currentTile[0]][currentTile[1]] = 1
            tiles[currentTile[0]][currentTile[1]+1] = 1
            tiles[currentTile[0]][currentTile[1]-1] = 1
            tiles[currentTile[0]-1][currentTile[1]] = 1
            tiles[currentTile[0]-1][currentTile[1]+1] = 1
            tiles[currentTile[0]-1][currentTile[1]-1] = 1
            tiles[currentTile[0]+1][currentTile[1]] = 1
            tiles[currentTile[0]+1][currentTile[1]+1] = 1
            tiles[currentTile[0]+1][currentTile[1]-1] = 1

            
                
                
                

    pygame.display.update()

    

