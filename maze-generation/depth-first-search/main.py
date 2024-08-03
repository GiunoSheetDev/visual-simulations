import depth_first_search as dfs
import dijkstra as dj

import sys
import pygame

pygame.init()

screen = pygame.display.set_mode((dfs.screenW, dfs.screenH))
mazeGenerated = False


sys.setrecursionlimit(5000)




if __name__ == "__main__":
    run = True
    print("Press 1 to generate the maze.",
          "\nPress 2 to solve the maze."
          )
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    run = False

                if event.key == pygame.K_1:
                    mazeGenerated = True
                    print(">>> Generating maze using depth first search...")
                    stack, directionStack = dfs.generateStacks()
                    dfs.run(stack=stack, directionStack= directionStack, screen=screen)
                    mazeGraph = dfs.generateFinalMazeGraph(stack, directionStack)
                    print("maze generated")
                
                if event.key == pygame.K_2 and mazeGenerated:
                    print("using dj")
                    dj.run(screen, mazeGraph)    
                    print("done dj")
                    mazeGenerated = False

    
    