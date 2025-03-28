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
        
    
    def draw(self, screen):
        pygame.draw.circle(screen, self.color, self.position, 5, width=1)



    


class Triangle:
    def __init__(self, vertices: list[Centroid, Centroid, Centroid]):
        self.a, self.b, self.c = vertices
        self.color = (255, 255, 255)
        self.edges = [  [self.a, self.b],
                        [self.b, self.c],
                        [self.c, self.a]]
        self.circumcenter = getCircumcenter(self.a, self.b, self.c)

    def isPointInCircumcircle(self, point: Centroid, typeOfLen: str):
        match typeOfLen:
            case "Euclidean":
                if getEuclideanDistance(self.a, self.circumcenter) > getEuclideanDistance(point, self.circumcenter):
                    return True
                return False

            case "Manhattan":
                if getManhattanDistance(self.a, self.circumcenter) > getManhattanDistance(point, self.circumcenter):
                    return True
                return False

    def hasVertex(self, point: Centroid):
        if self.a == point or self.b == point or self.c == point:
            return True
        return False
    
    def draw(self, screen):
        for edge in self.edges:
            pygame.draw.aaline(screen, self.color, edge[0].position, edge[1].position)


def getCircumcenter(a: Centroid, b: Centroid, c: Centroid) ->Centroid:
    ax, ay = a.position
    bx, by = b.position
    cx, cy = c.position

    d = 2 *(ax*(by-cy) + bx*(cy-ay) + cx*(ay-by))

    ux = (1/d) *(   (ax**2 + ay**2)*(by-cy) +
                    (bx**2 + by**2)*(cy-ay) +
                    (cx**2 + cy**2)*(ay-by)
    )
    uy = (1/d)  *(
                    (ax**2 + ay**2)*(cx-bx)+
                    (bx**2 + by**2)*(ax-cx)+
                    (cx**2 + cy**2)*(bx-ax)
    )

    return Centroid(ux, uy)

def isLineEqual(l1 : list[Centroid, Centroid], l2: list[Centroid, Centroid]):
    

    if (l1[0].position == l2[0].position and l1[1].position == l2[1].position) or (l1[0].position== l2[1].position and l1[1].position == l2[0].position):
        return True
    return False

def getEuclideanDistance(p1: Centroid, p2: Centroid):
    p1x, p1y = p1.position
    p2x, p2y = p2.position

    return ((p2x -p1x) **2 + (p2y - p1y) **2) **0.5

def getManhattanDistance(p1: Centroid, p2: Centroid):
    p1x, p1y = p1.position
    p2x, p2y = p2.position

    return abs(p1x-p2x) + abs(p1y -p2y)


def placeCentroid(centroid: Centroid) -> None:
    centroidList.append(centroid)
    

def delaunayTriangulation(centroidList: list, screenw: int, screenh: int, typeOfLen: str):
    triangulation = []

    superTriangleA = Centroid(-100, -100)
    superTriangleB = Centroid(2*screenw+100, -100)
    superTriangleC = Centroid(-100, 2*screenh+100)

    superTriangle = Triangle([superTriangleA, superTriangleB, superTriangleC])
    triangulation.append(superTriangle)

    for point in centroidList:
        badTriangles = []

        
        for triangle in triangulation:
            if triangle.isPointInCircumcircle(point, typeOfLen):
                badTriangles.append(triangle)

        polygon = []
        for triangle in triangulation[:]:
            for edge in triangle.edges:
                isShared = False

                for otherTriangle in badTriangles:
                    if otherTriangle == triangle:
                        continue
                    for otherEdge in otherTriangle.edges:
                        if isLineEqual(otherEdge, edge):
                            isShared = True
                
                if not isShared:
                    polygon.append(edge)



        for badtriangle in badTriangles:
            triangulation.remove(badtriangle)

        for edge in polygon:
            newTriangle = Triangle([edge[0], edge[1], point])
            triangulation.append(newTriangle)

    for triangle in triangulation[:]:
        if triangle.hasVertex(superTriangleA) and triangle in triangulation:
            triangulation.remove(triangle)
        if triangle.hasVertex(superTriangleB) and triangle in triangulation:
            triangulation.remove(triangle)
        if triangle.hasVertex(superTriangleC) and triangle in triangulation:
            triangulation.remove(triangle)
        
        
    return triangulation



def run():

    

    delaunay = []


    run = True
    while run:
        for point in centroidList:
            point.draw(screen)


        for triangle in delaunay:
            triangle.draw(screen)



        if pygame.mouse.get_just_pressed()[0]:
            placeCentroid(Centroid(pygame.mouse.get_pos()[0], pygame.mouse.get_pos()[1]))



        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    run = False
                if event.key == pygame.K_SPACE:
                    delaunay = delaunayTriangulation(centroidList, screenw, screenh, "Euclidean")

        pygame.display.update()




run()


















