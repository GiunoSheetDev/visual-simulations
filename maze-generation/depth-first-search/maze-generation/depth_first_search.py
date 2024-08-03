import pygame
import random
import sys



sys.setrecursionlimit(5000)




pygame.init()

screenW, screenH = 800, 800
tileDimension = 10
screen = pygame.display.set_mode((screenW, screenH))
columns = int(screenW / tileDimension)
rows = int(screenH / tileDimension)
startPos = (0,0)
endPos = (screenW-1, screenH-1)
complexityValue = 120 #easier is 1200 -> harder is 200




def createBoard():
    return [[0 for _ in range(columns)] for _ in range(rows)]

def drawGrid(screen: pygame.Surface):
    screen.fill((0,0,0))
    #pygame.draw.rect(screen, (0,255,0), pygame.Rect(0,0,tileDimension-5, tileDimension-5))
    #pygame.draw.rect(screen, (255,0,0), pygame.Rect(screenW-tileDimension+5, screenH-tileDimension+5, tileDimension-5, tileDimension-5))
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


def generateRandomWallsToDestroy(directionStack: list, stack: list):
    indexSet = set()
    i = 0
    while i < complexityValue: #800
        randomIndex = random.randint(1, len(directionStack)-1)
        if randomIndex not in indexSet:
            indexSet.add(randomIndex)
            referenceTuple = directionStack[randomIndex]
            referenceTupleDirection = referenceTuple[2]
            #generate new Direction
            directions = ["up", "down", "left", "right"]
            if referenceTuple[0] == 0:
                directions.remove("right")
            if referenceTuple[0] == (rows)-1:
                directions.remove("left")
            if referenceTuple[1] == 0:
                directions.remove("down")
            if referenceTuple[1] == (columns)-1:
                directions.remove("up")

            directions.remove(referenceTupleDirection)
            randomDirection = directions[random.randint(0,len(directions)-1)]
            newTuple = (referenceTuple[0], referenceTuple[1], randomDirection)
            directionStack.append(newTuple)
            stack.append(newTuple[:-1])
            i+= 1
            
    return stack, directionStack
    

    
def drawMaze(directionStack, screen: pygame.Surface): 
    
    for index, cell in enumerate(directionStack):
        #pygame.time.delay(5)
        if cell == (0,0): 
            continue
        match cell[2]:
            case "down":
                pygame.draw.line(screen, (0,0,0), (cell[0] * tileDimension, cell[1] * tileDimension), (cell[0] * tileDimension + tileDimension, cell[1] * tileDimension))
            case "up":
                pygame.draw.line(screen, (0,0,0), (cell[0]*tileDimension, cell[1]*tileDimension+tileDimension), (cell[0]*tileDimension + tileDimension, cell[1]*tileDimension+tileDimension))
            case "left":
                pygame.draw.line(screen, (0,0,0), (cell[0]*tileDimension+tileDimension, cell[1]*tileDimension), (cell[0]*tileDimension+tileDimension, cell[1]*tileDimension+tileDimension))
            case "right":
                pygame.draw.line(screen, (0,0,0), (cell[0]*tileDimension, cell[1]*tileDimension), (cell[0]*tileDimension, cell[1]*tileDimension+tileDimension))

        pygame.display.update()



def generateStacks():
    stack, directionStack = cursiveBackTracker([(0,0)], [(0,0)], 0, 0)
    return stack, directionStack


def generateFinalMazeGraph(stack, directionStack):
    mazeGraph = {}

    for node in stack:
        mazeGraph[node] = []

    for direction, node in zip(directionStack, stack):
        match direction[-1]:
            case "up":
                cell = (node[0], node[1]+1)
                mazeGraph[node].append(cell)
                mazeGraph[cell].append(node)
            case "down":
                cell = (node[0], node[1]-1)
                mazeGraph[node].append(cell)
                mazeGraph[cell].append(node)
            case "left":
                cell = (node[0]+1, node[1])
                mazeGraph[node].append(cell)
                mazeGraph[cell].append(node)
            case "right":
                cell = (node[0]-1, node[1])
                mazeGraph[node].append(cell)
                mazeGraph[cell].append(node)

    return mazeGraph

stack, directionStack = generateStacks()

def run(stack, directionStack, screen):
    board = createBoard()
    drawGrid(screen)
    stack, directionStack = generateRandomWallsToDestroy(directionStack, stack)
    mazeGraph = generateFinalMazeGraph(stack, directionStack)
    
    
    drawMaze(directionStack, screen)

    

if __name__ == "__main__":
    
    run(stack, directionStack, screen)