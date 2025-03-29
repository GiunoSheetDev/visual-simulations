from delaunay import *

import pygame

pygame.init()

screenw, screenh = 800, 600
screen = pygame.display.set_mode((screenw, screenh))


def voronoiTesselation(delaunay: list):
    '''
The center of each triangle's circumcircle is a vertex (point) for the
Voronoi tesselation. Then simply connect the centers of all the circumcircles of 
the neighboring triangles to derive the tesselation.    
'''

    #get all neighbors of triangles for each triangles

    triangle: Triangle
    for triangle in delaunay:
        triangle.neighbors = []
        other: Triangle
        for other in delaunay:
            if triangle == other:
                continue

            if any(edge in triangle.edges for edge in other.edges) or any(edge[::-1] in triangle.edges for edge in other.edges):
                #they are neighbors
                triangle.neighbors.append(other)

    connections = []

    triangle: Triangle
    for triangle in delaunay:

        neighbor: Triangle
        for neighbor in triangle.neighbors:
            #all 3 neighbors
            connection = [triangle.circumcenter, neighbor.circumcenter]
            reverseConnection = connection[::-1]
            
            if connection not in connections or reverseConnection not in connections:
                connections.append(connection)

        #triangle.unconnectedEdges = [x for x in connections if x not in triangle.edges]
        #TODO fix this


    return connections















def run():

    typeOfLen = "Euclidean"
    pointList = []
    delaunay = []
    voronoi = []


    isShowingDelaunay = False
    isShowingVoronoi = True

    
    run = True

    print("for random generation press r\n"
        "left mouse click to add wanted points\n"
        "to choose euclidean distance (default) press e \n"
        "to choose manhattan distance press m\n"
        "press space to clear the screen\n"
        "press 1 to toggle delaunay triangolation")
    while run:
        screen.fill((0, 0, 0))

        

        

        if isShowingDelaunay:
            

            triangle: Triangle
            for triangle in delaunay:
                triangle.draw(screen)

            for triangle in delaunay:
                pygame.draw.circle(screen, (255, 0, 0), triangle.circumcenter, 5, 1)

        if isShowingVoronoi:

            for point in pointList:
                pygame.draw.circle(screen,(255,255,255), point, 5, 1)
            
            for line in voronoi:
                pygame.draw.aaline(screen, (255, 0, 0), line[0], line[1])

            '''
            for triangle in delaunay:
                print(triangle.unconnectedEdges)
                for uedge in triangle.unconnectedEdges:
                    midPoint = pygame.Vector2((uedge[0][0] + uedge[1][0])/2, (uedge[0][1] + uedge[1][1])/2) 
                    pygame.draw.aaline(screen, (255, 0, 0), triangle.circumcenter, midPoint)
            '''
            
            


        if pygame.mouse.get_just_pressed()[0]:
            placePoint(pygame.mouse.get_pos()[0], pygame.mouse.get_pos()[1], pointList)
            delaunay = delaunayTriangulation(pointList, screenw, screenh, typeOfLen)
            voronoi = voronoiTesselation(delaunay)



        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    run = False

                if event.key == pygame.K_e:
                    typeOfLen = "Euclidean"
                
                if event.key == pygame.K_m:
                    typeOfLen = "Manhattan"

                if event.key == pygame.K_r:
                    pointList = []
                    for i in range(100):
                        x = randint(1, screenw-1)
                        y = randint(1, screenh-1)

                        pointList.append(pygame.Vector2(x, y))
                    delaunay = delaunayTriangulation(pointList, screenw, screenh, "Euclidean")
                    voronoi = voronoiTesselation(delaunay)

                
                if event.key == pygame.K_1:
                    isShowingDelaunay = not isShowingDelaunay
                
                

                if event.key == pygame.K_SPACE:
                    pointList = []
                    delaunay = []
                    voronoi = []


        pygame.display.update()


if __name__ == "__main__":
    run()




























