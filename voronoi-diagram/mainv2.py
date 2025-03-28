import pygame
from random import randint

pygame.init()

screenw, screenh = 800, 600
screen = pygame.display.set_mode((screenw, screenh))




class Triangle:
    def __init__(self, vertices: list[pygame.Vector2, pygame.Vector2, pygame.Vector2]):
        self.a, self.b, self.c = vertices
        self.color = (255, 255, 255)
        self.edges = [  [self.a, self.b],
                        [self.b, self.c],
                        [self.c, self.a]]
        self.circumcenter = getCircumcenter(self.a, self.b, self.c)

    def isPointInCircumcircle(self, point: pygame.Vector2, typeOfLen: str):
        match typeOfLen:
            case "Euclidean":
                if getEuclideanDistance(self.a, self.circumcenter) > getEuclideanDistance(point, self.circumcenter):
                    return True
                return False

            case "Manhattan":
                if getManhattanDistance(self.a, self.circumcenter) > getManhattanDistance(point, self.circumcenter):
                    return True
                return False

    def hasVertex(self, point: pygame.Vector2):
        if self.a == point or self.b == point or self.c == point:
            return True
        return False
    
    def draw(self, screen):
        for edge in self.edges:
            pygame.draw.aaline(screen, self.color, edge[0], edge[1])


def getCircumcenter(a: pygame.Vector2 , b: pygame.Vector2, c: pygame.Vector2) -> pygame.Vector2:
    ax, ay = a
    bx, by = b
    cx, cy = c

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

    return pygame.Vector2(ux, uy)

def isLineEqual(l1 : list[pygame.Vector2, pygame.Vector2], l2: list[pygame.Vector2, pygame.Vector2]):

    if (l1[0] == l2[0] and l1[1] == l2[1]) or (l1[0] == l2[1] and l1[1] == l2[0]):
        return True
    return False

def getEuclideanDistance(p1: pygame.Vector2, p2: pygame.Vector2):
    p1x, p1y = p1
    p2x, p2y = p2

    return ((p2x -p1x) **2 + (p2y - p1y) **2) **0.5

def getManhattanDistance(p1: pygame.Vector2, p2: pygame.Vector2):
    p1x, p1y = p1.position
    p2x, p2y = p2.position

    return abs(p1x-p2x) + abs(p1y -p2y)

def placePoint(x: int, y: int, pointList: list):
    pointList.append(pygame.Vector2(x, y))

def delaunayTriangulation(pointList: list, screenw: int, screenh: int, typeOfLen: str):
    '''
function BowyerWatson (pointList)
      // pointList is a set of coordinates defining the points to be triangulated
      triangulation := empty triangle mesh data structure
      add super-triangle to triangulation // must be large enough to completely contain all the points in pointList
      for each point in pointList do // add all the points one at a time to the triangulation
         badTriangles := empty set
         for each triangle in triangulation do // first find all the triangles that are no longer valid due to the insertion
            if point is inside circumcircle of triangle
               add triangle to badTriangles
         polygon := empty set
         for each triangle in badTriangles do // find the boundary of the polygonal hole
            for each edge in triangle do
               if edge is not shared by any other triangles in badTriangles
                  add edge to polygon
         for each triangle in badTriangles do // remove them from the data structure
            remove triangle from triangulation
         for each edge in polygon do // re-triangulate the polygonal hole
            newTri := form a triangle from edge to point
            add newTri to triangulation
      for each triangle in triangulation // done inserting points, now clean up
         if triangle contains a vertex from original super-triangle
            remove triangle from triangulation
      return triangulation
'''
    
    
    triangulation = []
    superTriangleA = pygame.Vector2(-100, -100)
    superTriangleB = pygame.Vector2(2*screenw+100, -100)
    superTriangleC = pygame.Vector2(-100, 2*screenh+100)
    superTriangle = Triangle([superTriangleA, superTriangleB, superTriangleC])
    triangulation.append(superTriangle)

    point: pygame.Vector2
    for point in pointList:

        badTriangles = []

        triangle: Triangle
        for triangle in triangulation:
            if triangle.isPointInCircumcircle(point, typeOfLen):
                badTriangles.append(triangle)


        polygon = []
        triangle: Triangle
        for triangle in badTriangles:
            for tedge in triangle.edges:
                isShared = False
                other: Triangle
                for other in badTriangles:
                    if other == triangle:
                        continue

                    for oedge in other.edges:
                        if isLineEqual(tedge, oedge):
                            isShared = True
                    
                
                if not isShared:
                    polygon.append(tedge)


        badTriangle: Triangle
        for badTriangle in badTriangles:
            triangulation.remove(badTriangle)

        for edge in polygon:
            newTriangle = Triangle([edge[0], edge[1], point])
            triangulation.append(newTriangle)

    for i in range(len(triangulation)-1, -1, -1): #iterate backwards to avoid making shallow copy
        triangle = triangulation[i]
        if triangle.hasVertex(superTriangleA) and triangle in triangulation:
            triangulation.remove(triangle)
        if triangle.hasVertex(superTriangleB) and triangle in triangulation:
            triangulation.remove(triangle)
        if triangle.hasVertex(superTriangleC) and triangle in triangulation:
            triangulation.remove(triangle)


    return triangulation

def run():
    pointList = []
    typeOfLen = "Euclidean"    

    print("for random generation press r\n"
    "left mouse click to add wanted points\n"
    "to choose euclidean distance (default) press e \n"
    "to choose manhattan distance press m\n"
    "press space to clear the screen")

    delaunay = []
    
    run = True
    while run:
        screen.fill((0,0,0))

        for point in pointList:
            pygame.draw.circle(screen,(255,255,255), point, 5, 1)


        triangle: Triangle
        for triangle in delaunay:
            triangle.draw(screen)

        if pygame.mouse.get_just_pressed()[0]:
            placePoint(pygame.mouse.get_pos()[0], pygame.mouse.get_pos()[1], pointList)
            delaunay = delaunayTriangulation(pointList, screenw, screenh, typeOfLen)
            




        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    run = False
                if event.key == pygame.K_r:
                    pointList = []
                    for i in range(100):
                        x = randint(1, screenw-1)
                        y = randint(1, screenh-1)

                        pointList.append(pygame.Vector2(x, y))
                    delaunay = delaunayTriangulation(pointList, screenw, screenh, "Euclidean")
                    

                if event.key == pygame.K_e:
                    typeOfLen = "Euclidean"
                    print("Distance chosen: Euclidean")
                if event.key == pygame.K_m:
                    typeOfLen = "Manhattan"
                    print("Distance chosen: Manhattan")
                
                if event.key == pygame.K_SPACE:
                    pointList = []
                    delaunay = []

        pygame.display.update()



run()
