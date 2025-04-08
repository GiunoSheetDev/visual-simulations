import random
import pygame
from math import pi, sin, cos, sqrt
from statistics import mean

screenw, screenh = 800, 800
screen = pygame.display.set_mode((screenw, screenh))

colorDict = {
    0 : (255, 0, 0),
    1 : (0, 255, 0),
    2 : (0, 0, 255),
    3 : (255, 255, 0),
    4 : (255, 0, 255),
    5 : (0, 255, 255),
    6 : (202, 255, 148),
    7 : (255, 158, 249)
}



def generatePoints(clusterNum: int, pointsPerCluster: int) -> list:
    points = []
    for _ in range(clusterNum):
        cx, cy = random.randint(250, 650), random.randint(250, 650)
        radius = 250

        horizontalStretchFactor = random.choice([1.0, 1.5])
        verticalStretchFactor = 2.0 - horizontalStretchFactor
        for _ in range(pointsPerCluster):
            angle = random.uniform(0, 2*pi)
            r = radius * sqrt(random.uniform(0, 1))

            x = cx + r * cos(angle) * horizontalStretchFactor
            y = cy + r * sin(angle) * verticalStretchFactor

            points.append([x, y])

    return points

def generateCentroids(centroidNum: int) -> list[int]:
    return [[random.randint(0, 800), random.randint(0, 800)] for _ in range(centroidNum)]

def assignPointsToClusters(points: list[list[int, int]], centroids: list[int], distanceType: bool):
    if centroids == []:
        return []

    clusters = [[] for _ in range(len(centroids))]

    for point in points:
        distances = []


        for centroid in centroids:
            
            if distanceType:
                dist = abs(point[0]-centroid[0]) + abs(point[1]-centroid[1])
            else:
                dist = sqrt((point[0] - centroid[0]) **2 + (point[1]- centroid[1])**2)
            
            distances.append(dist)
        
        closestCentroidIndex = distances.index(min(distances))

        clusters[closestCentroidIndex].append(point)

    return clusters

def updateCentroidPosition(clusters: list[list[int, int]]):
    newCentroids = []
    
    for cluster in clusters:

        if not cluster:  # Skip empty clusters
            continue

        xvalues = []
        yvalues = []

        for point in cluster:
            xvalues.append(point[0])
            yvalues.append(point[1])

        centerx = mean(xvalues)
        centery = mean(yvalues)

        newCentroids.append([centerx, centery])

    return newCentroids


def getClusterColor(index) -> tuple[int, int, int]:
    if index in colorDict.keys():
        return colorDict[index]
    
    newColor = (random.randint(0, 255),random.randint(0, 255),random.randint(0, 255))
    colorDict[index] = newColor

    return colorDict[index]

def drawPoints(points: list[list[int, int]], clusters: list[list[int, int]], isShowingClusters: bool) -> None:
    if clusters == []:
        for point in points:
            pygame.draw.circle(screen, (255, 255, 255), point, 2)

    for index, cluster in enumerate(clusters):
        if isShowingClusters:
            color = getClusterColor(index)
        else:
            color = (255, 255, 255)

        for point in cluster:
            pygame.draw.circle(screen, color, point, 2)

def drawCentroids(centroids: list[int], isShowingClusters: bool) -> None:
    for index, centroid in enumerate(centroids):
        if isShowingClusters:
            color = getClusterColor(index)
        else:
            color = (255, 255, 255)

        pygame.draw.circle(screen, color, centroid, 5)


def placeCentroid(centroids: list[int], mousePos: list[int, int]) -> list[int]:
    centroids.append(mousePos)
    return centroids
        

def run():
    points = generatePoints(7, 1500)
    #centroids = generateCentroids(7)
    centroids = generateCentroids(0)

    isShowingClusters = False
    isShowingAnimation = False
    isDistanceManhattan = False
    run = True
    
    print(  "Press left click to place a Centroid.\n"
            "Press c to automatically set the centroid num to 7.\n"
            "Press f to show clusters color.\n" \
            "Press a to show animation with step half a second.\n"
            "Press Spacebar to generate a new set of points.\n"
            "Press d to change distance used. (Euclidean / Manhattan)")


    while run:
        #print(centroids)

        screen.fill((0,0,0))

        if isShowingAnimation:
            pygame.time.wait(500)

        clusters = assignPointsToClusters(points, centroids, isDistanceManhattan)
        centroids = updateCentroidPosition(clusters)
       
        
        drawPoints(points, clusters, isShowingClusters)
        drawCentroids(centroids, isShowingClusters)

        if pygame.mouse.get_just_pressed()[0]:
            placeCentroid(centroids, pygame.mouse.get_pos())
            isShowingClusters = True
        

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    run = False
                if event.key == pygame.K_SPACE:
                    points = generatePoints(7, 1500)
                    centroids = generateCentroids(0)
                if event.key == pygame.K_c:
                    centroids = generateCentroids(7)
                if event.key == pygame.K_f:
                    isShowingClusters = not isShowingClusters
                    print("IsShowingClustersColor: ", isShowingClusters)
                if event.key == pygame.K_a:
                    isShowingAnimation = not isShowingAnimation
                    print("IsShowingAnimationStep: ", isShowingAnimation)
                if event.key == pygame.K_d:
                    isDistanceManhattan = not isDistanceManhattan
                    print("IsDistanceUsedManhattan: ", isDistanceManhattan)


        pygame.display.update()


if __name__ == "__main__":
    run()
    
        