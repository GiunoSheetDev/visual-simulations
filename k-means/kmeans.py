import random
import pygame
from math import pi, sin, cos, sqrt
from statistics import mean

screenw, screenh = 800, 800
screen = pygame.display.set_mode((screenw, screenh))

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
    match index:
        case 0: return (255, 0, 0)
        case 1: return (0, 255, 0)
        case 2: return (0, 0, 255)
        case 3: return (255, 255, 0)
        case 4: return (255, 0, 255)
        case 5: return (0, 255, 255)
        case 6: return (202, 255, 148)
        case 7: return (255, 158, 249)
        case _: return (random.randint(0, 255),random.randint(0, 255),random.randint(0, 255))


def drawPoints(clusters: list[list[int, int]], isShowingClusters: bool) -> None:
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


        

def run():
    points = generatePoints(7, 1500)
    centroids = generateCentroids(7)

    isShowingClusters = True
    isShowingAnimation = False
    isDistanceManhattan = False
    run = True
    
    print(  "Press f to show clusters color.\n" \
            "Press a to show animation with step half a second.\n"
            "Press Spacebar to generate a new set of points.\n"
            "Press d to change distance used. (Euclidean / Manhattan)")


    while run:
        screen.fill((0,0,0))

        if isShowingAnimation:
            pygame.time.wait(500)

        clusters = assignPointsToClusters(points, centroids, isDistanceManhattan)
        centroids = updateCentroidPosition(clusters)
       
        
        drawPoints(clusters, isShowingClusters)
        drawCentroids(centroids, isShowingClusters)

        

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    run = False
                if event.key == pygame.K_SPACE:
                    points = generatePoints(7, 1500)
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
    
    
        