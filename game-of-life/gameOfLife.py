import pygame

pygame.init()

screenW = 1200
screenH = 1200
screen = pygame.display.set_mode((screenW, screenH))

fps = 30
clock = pygame.time.Clock()

tiles = []
tileDimension = 20
columns = int(screenW/tileDimension)
rows = int(screenH/tileDimension)


def drawBackground():
    screen.fill((0,0,0))

    for i in range(len(tiles)):
        for j in range(len(tiles[i])):
            if tiles[i][j] == 1:
                pygame.draw.rect(screen, (255,255,255), pygame.Rect(tileDimension*i,tileDimension*j, tileDimension, tileDimension))



def getTiles() -> list[list]: #get empty board to then fill with conditions
    l = []
    for i in range(rows):
        tempList = []
        for j in range(columns):
            tempList.append(0)

        l.append(tempList)
    
    return l


def updateTiles(tiles : list[list]) -> list[list]: #update empty board following conway's rule
    newTiles = getTiles()

    for i in range(columns):
        for j in range(rows):
            try: #TODO handle edge cases
                cellValue = tiles[i][j]
                topLeft = tiles[i-1][j-1]
                top = tiles[i][j-1]
                topRight = tiles[i+1][j-1]
                left = tiles[i-1][j]
                right = tiles[i+1][j]
                bottomLeft = tiles[i-1][j+1]
                bottom = tiles[i][j+1]
                bottomRight = tiles[i+1][j+1]
                neighborCells = [topLeft, top, topRight, left, right, bottomLeft, bottom, bottomRight]
                liveCount = neighborCells.count(1)
                
                if cellValue == 1: #cell is alive
                    if liveCount < 2:
                        newTiles[i][j] = 0
                    elif 2 <= liveCount <= 3:
                        newTiles[i][j] = 1
                    else:
                        newTiles[i][j] = 0
                else: #cell is dead
                    if liveCount == 3:
                        newTiles[i][j] = 1


            except:
                pass
    
    return newTiles
    

def mousePos():
    mousex = pygame.mouse.get_pos()[0]
    mousey = pygame.mouse.get_pos()[1]
    
    currentTile = (int(mousex/tileDimension), int(mousey/tileDimension))
    return currentTile





tiles = getTiles()

''' 
GLIDER

tiles[1][2] = 1
tiles[2][2] = 1
tiles[3][2] = 1
tiles[3][1] = 1
tiles[2][0] = 1

'''



run = True
runSimulation = False

print("Press f to start/stop simulation")
while run:
    clock.tick(fps)
    
    currentTile = mousePos()

    drawBackground()
    newTiles = updateTiles(tiles)
    if runSimulation:
        tiles = newTiles
    else:
        if pygame.mouse.get_just_pressed()[0]: #left click mouse to draw cell
            if tiles[currentTile[0]][currentTile[1]] == 0:
                tiles[currentTile[0]][currentTile[1]] = 1
        if pygame.mouse.get_pressed()[2]: #right click mouse to erase cell
            if tiles[currentTile[0]][currentTile[1]] == 1:
                tiles[currentTile[0]][currentTile[1]] = 0


    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                run = False
 
            if event.key == pygame.K_f: #pause the simulation but not the main game loop
                runSimulation = not runSimulation

    

    pygame.display.update()