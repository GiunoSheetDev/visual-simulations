import pygame
import heapq

pygame.init()


screenW, screenH = 800, 800
tileDimension = 10
startPos = (0,0)
#endPos = (41, 40)
endPos = (screenW/tileDimension-1, screenH/tileDimension-1)




def dijkstra_algorithm_with_path(mazeGraph, startPos): #https://www.phind.com/search?cache=ajxt0mi2t1hradmaglwnc6d0
    # Initialize the distance dictionary with infinity for all nodes except the start node
    distances = {node: float('infinity') for node in mazeGraph}
    distances[startPos] = 0
    
    # Dictionary to keep track of the path
    predecessors = {node: None for node in mazeGraph}
    
    # Priority queue for nodes to visit, starting with the start node
    queue = [(0, startPos)]
    
    while queue:
        current_distance, current_node = heapq.heappop(queue)
        
        # Skip if this path is not optimal
        if current_distance > distances[current_node]:
            continue
        
        # Update neighbors
        for neighbor in mazeGraph[current_node]:
            distance = current_distance + 1  # Uniform cost of 1
            
            # Update the shortest distance if a shorter path is found
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                predecessors[neighbor] = current_node  # Update predecessor
                heapq.heappush(queue, (int(distance), neighbor))
    
    return distances, predecessors


def reconstruct_path(predecessors, start_node, end_node):
    path = []
    current_node = end_node
    while current_node is not None:
        path.append(current_node)
        current_node = predecessors[current_node]
    path.reverse()  # Reverse to get path from start to end
    return path


def drawPath(path, screen):
    for index, node in enumerate(path):
        pygame.time.delay(10)
        if index == len(path)-1:
            continue
        pygame.draw.line(screen, (255,0,0), (node[0]*tileDimension + tileDimension/2, node[1]*tileDimension+tileDimension/2), (path[index+1][0]*tileDimension+tileDimension/2, path[index+1][1]*tileDimension+tileDimension/2))
        pygame.display.update()


def find_indices_of_elements_in_list(list_a, list_b):
    return [i for i, x in enumerate(list_a) if x in list_b]



def shortenPath(path, mazeGraph):
    tempPath =[]

    for index, node in enumerate(path):
        indices = find_indices_of_elements_in_list(path, mazeGraph[node])
        furthestElem = max(indices)
        tempPath.append((index, furthestElem))

    


        





def run(screen, mazeGraph):
    distances, predecessors = dijkstra_algorithm_with_path(mazeGraph, startPos)
    path = reconstruct_path(predecessors, startPos, endPos)

    
    shortenPath(path, mazeGraph)
    


    drawPath(path, screen)
    





if __name__ == "__main__":
    run()