import pygame
import math
from random import randint

pygame.init()

screenw, screenh = 800, 600
screen = pygame.display.set_mode((screenw, screenh))



centroidList = []
lineList = []


class Centroid:
    def __init__(self, x: int, y: int):
        self.position = (x, y)
        self.color = (randint(0, 255),randint(0, 255),randint(0, 255))
        self.minimumConnections = 3
        self.currentConnections = 0
        self.lineList = []

    
    def draw(self, screen):
        pygame.draw.circle(screen, self.color, self.position, 5, width=1)


class Line:
    def __init__(self, startCentroid: Centroid, endCentroid: Centroid):
        self.start= startCentroid.position
        self.end = endCentroid.position
        self.color = (255, 255, 255)
        self.length = ((endCentroid.position[0] - startCentroid.position[0]) **2 + (endCentroid.position[1] - startCentroid.position[1])**2)**0.5
        self.midPoint = ((startCentroid.position[0] + endCentroid.position[0])/2, (startCentroid.position[1] + endCentroid.position[1])/ 2)



    def draw(self, screen):
        pygame.draw.line(screen, (255, 255, 255), self.start, self.end)


        




def createLines():

    if len(centroidList) == 1:
        return

    for index, centroid in enumerate(centroidList):
        tempList = centroidList[:index] + centroidList[index+1:]
        
        for endPoint in tempList:
            
            #TODO this creates twice the lines (A-> B , B-> A) FIX
            l = Line(centroid, endPoint)
            lineList.append(l)
            centroid.lineList.append(l)
            endPoint.lineList.append(l)
            

def pruneLines():
    for index, line in enumerate(lineList):
        tempList = lineList[:index] + lineList[index+1:]

        for tempLine in tempList:
            


def placeCentroid(centroid: Centroid) -> None:
    centroidList.append(centroid)
    lineList = []
    createLines()







def run():
    run = True
    while run:



        for centroid in centroidList:
            centroid.draw(screen)

        
        for line in lineList:
            line.draw(screen)
        



        if pygame.mouse.get_just_pressed()[0]:
            placeCentroid(Centroid(pygame.mouse.get_pos()[0], pygame.mouse.get_pos()[1]))



        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    run = False
                if event.key == pygame.K_p:
                    for line in lineList:
                        print(line.length, line.start, line.end)
                if event.key == pygame.K_d:
                    lineList.append(Line(centroidList[0], centroidList[1]))
                    #TODO create function that also appends line inside the centroid.linelist
                    

        pygame.display.update()




run()


















