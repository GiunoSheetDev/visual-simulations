import pygame
import random
import math

pygame.init()

screenW, screenH = 821, 821
screen = pygame.display.set_mode((screenW, screenH))

cellW, cellH = 1, 1
rows = screenH // cellH
columns = screenW // cellW

rulenum = 60


def drawBackground(cells : list[int], y):
    
    for i in range(rows):
        if cells[i] == 1:
            pygame.draw.rect(screen, (0,0,0), pygame.Rect(cellW*i, y, cellW, cellH))

    y += cellH
    
    return y


def getRule(rulenum):
    rule = []
    ruleBin = bin(rulenum)[2:]
    ruleBin = ruleBin.zfill(8)
    for char in ruleBin:
        rule.append(int(char))

    return rule




def getEmptyCells(rows : int, columns: int) -> list[int]:
    cells = [0 for _ in range(columns)] #for _ in range(rows)]
    cells[math.floor(columns/2)] = 1
    return cells


def updateCells(cells):
    
    nextCells = getEmptyCells(rows=rows, columns=columns)

    rule = getRule(rulenum)
    length = len(cells)
    for i in range(0, len(cells)):
        left = cells[(i-1 + length) % length]
        right = cells[(i+1 + length) % length]
        state = cells[i]
        newState = calculateState(left, state, right, rule=rule)
        nextCells[i] = newState


    cells = nextCells
    return cells
 

def calculateState(left : int, state: int, right: int, rule: list[int]):
    neighborhood = str(left) + str(state) + str(right)
    value = 7 - int(neighborhood, 2)
    return rule[value]
    if left == 1 and state == 1 and right == 1: return rule[0]
    if left == 1 and state == 1 and right == 0: return rule[1]
    if left == 1 and state == 0 and right == 1: return rule[2]
    if left == 1 and state == 0 and right == 0: return rule[3]
    if left == 0 and state == 1 and right == 1: return rule[4]
    if left == 0 and state == 1 and right == 0: return rule[5]
    if left == 0 and state == 0 and right == 1: return rule[6]
    if left == 0 and state == 0 and right == 0: return rule[7]


def run():
    screen.fill((255,255,255))
    run = True
    cells = getEmptyCells(rows=rows, columns=columns)
    y = 0
    
    while run:
        cells = updateCells(cells)
        y = drawBackground(cells=cells, y=y)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    run = False
        
        pygame.display.update()
        
        


if __name__ == "__main__":
    print(getRule(rulenum=rulenum))
    run()
    
    