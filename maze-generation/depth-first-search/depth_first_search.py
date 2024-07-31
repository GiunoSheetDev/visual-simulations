import pygame
import random
import sys
sys.setrecursionlimit(5000)




pygame.init()

screenW, screenH = 1000, 1000
tileDimension = 10
screen = pygame.display.set_mode((screenW, screenH))
columns = int(screenW / tileDimension)
rows = int(screenH / tileDimension)

def createBoard():
    return [[0 for _ in range(columns)] for _ in range(rows)]

def drawGrid():
    screen.fill((0,0,0))
    pygame.draw.rect(screen, (0,255,0), pygame.Rect(0,0,tileDimension-5, tileDimension-5))
    pygame.draw.rect(screen, (255,0,0), pygame.Rect(screenW-tileDimension+5, screenH-tileDimension+5, tileDimension-5, tileDimension-5))
    for i in range(rows+1):
        pygame.draw.line(screen, (128,128,128), (0, i*tileDimension), (screenW, i*tileDimension))
    for j in range(columns+1):
        pygame.draw.line(screen, (128, 128, 128), (j*tileDimension, 0), (j*tileDimension, screenH))

def getNeighbors(x: int, y: int)->list[tuple]:
    n = []
    c = []
    if x > 0:
        n.append((x-1, y, "left"))
        c.append((x-1, y))
    if x < columns-1:
        n.append((x+1, y, "right"))
        c.append((x+1, y))
    if y > 0:
        n.append((x, y-1, "up"))
        c.append((x, y-1))
    if y < rows-1:
        n.append((x, y+1, "down"))
        c.append((x, y+1))
    return c, n






def cursiveBackTracker(stack : list, directionStack: list, x: int, y: int)->list[tuple]:
    #directionStack is used to get the walls to delete
    neighbors, directionNeighbors = getNeighbors(x, y)
    
    while True:
        
        if len(neighbors) == len([n for n in neighbors if n in stack]):  # Check if all neighbors are visited
            return stack, directionStack
        
        direction = random.randint(0, len(neighbors)-1)
        chosenNeighbor = neighbors[direction]
        directionNeighbor = directionNeighbors[direction]
        if chosenNeighbor not in stack: #ripete fino a che non trova un neighbor libero
            stack.append(chosenNeighbor)
            directionStack.append(directionNeighbor)
            cursiveBackTracker(stack, directionStack, chosenNeighbor[0], chosenNeighbor[1])
        
    
def drawMaze(directionStack): #TODO fix
    
    for index, cell in enumerate(directionStack):
        pygame.time.delay(25)
        if cell == (0,0): 
            continue
        match cell[2]:
            case "down":
                pygame.draw.line(screen, (0,0,0), (cell[0] * tileDimension+1, cell[1] * tileDimension), (cell[0] * tileDimension + tileDimension-1, cell[1] * tileDimension))
            case "up":
                pygame.draw.line(screen, (0,0,0), (cell[0]*tileDimension+1, cell[1]*tileDimension+tileDimension), (cell[0]*tileDimension + tileDimension-1, cell[1]*tileDimension+tileDimension))
            case "left":
                pygame.draw.line(screen, (0,0,0), (cell[0]*tileDimension+tileDimension, cell[1]*tileDimension+1), (cell[0]*tileDimension+tileDimension, cell[1]*tileDimension+tileDimension-1))
            case "right":
                pygame.draw.line(screen, (0,0,0), (cell[0]*tileDimension, cell[1]*tileDimension+1), (cell[0]*tileDimension, cell[1]*tileDimension+tileDimension-1))

        pygame.display.update()


def run():
    run = True
    board = createBoard()
    #drawGrid()
    stack, directionStack = cursiveBackTracker([(0,0)], [(0,0)], 0, 0)

    #stack = [(0, 0), (0, 1), (1, 1), (2, 1), (2, 0), (3, 0), (3, 1), (3, 2), (2, 2), (1, 2), (1, 3), (0, 3), (0, 2), (2, 3), (3, 3), (1, 0)]
    #directionStack = [(0, 0), (0, 1, 'down'), (1, 1, 'right'), (2, 1, 'right'), (2, 0, 'up'), (3, 0, 'right'), (3, 1, 'down'), (3, 2, 'down'), (2, 2, 'left'), (1, 2, 'left'), (1, 3, 'down'), (0, 3, 'left'), (0, 2, 'up'), (2, 3, 'right'), (3, 3, 'right'), (1, 0, 'left')]
    

    drawGrid()
    drawMaze(directionStack)
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    run = False
        
        pygame.display.update()

if __name__ == "__main__":
    run()