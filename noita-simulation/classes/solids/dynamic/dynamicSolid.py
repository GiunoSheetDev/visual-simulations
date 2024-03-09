from classes.solids.solid import  Solid
from classes.liquids.liquid import Liquid
from classes.solids.static.staticSolid import StaticSolid
from classes.particle import Particle
from random import randint


class DynamicSolid(Solid):
    def __init__(self, i, j) -> None:
        super().__init__(i, j)

    def getNeighbors(self, tiles : list[list]) -> list:
        
        if 0 < self.i < len(tiles)-1 and self.j < len(tiles[0]):
            diagonalLeft = tiles[self.i-1][self.j+1]
            diagonalRight = tiles[self.i+1][self.j+1]
            isDiagonalLeftSolid = isinstance(diagonalLeft, Solid)
            isDiagonalRightSolid = isinstance(diagonalRight, Solid)
        if self.i == 0: #means particle is in the left most column, cant have a diagonalLeft neighbor
            diagonalLeft = None
            isDiagonalLeftSolid = True
            diagonalRight = tiles[self.i+1][self.j+1]
            isDiagonalRightSolid = isinstance(diagonalRight, Solid)
        elif self.i == len(tiles)-1 :#particle at right most column, cant have diagonalRight neighbor
            diagonalRight = None
            isDiagonalRightSolid = True
            diagonalLeft = tiles[self.i-1][self.j+1]
            isDiagonalLeftSolid = isinstance(diagonalLeft, Solid)

        return [diagonalLeft, diagonalRight, isDiagonalLeftSolid, isDiagonalRightSolid]
    
    def update(self, tiles: list[list]) -> list[list]:
        
        try:
            bottom = tiles[self.i][self.j+1]
            
            
            if bottom == 0: 
                self.moveToEmptyCell(self.i, self.j+1, tiles)
                
            
        
            elif isinstance(bottom, Liquid):
                self.switchWithAnotherParticle(self.i, self.j+1, tiles)

            elif isinstance(bottom, Solid):
                
                neighbor = self.getNeighbors(tiles)
                diagonalLeft = neighbor[0]
                diagonalRight = neighbor[1]
                isDiagonalLeftSolid = neighbor[2]
                isDiagonalRightSolid = neighbor[3]

                
    

                if not isDiagonalLeftSolid and not isDiagonalRightSolid:
                     #can go both ways. both diagonalLeft and diagonalRight arent solids
                    direction = randint(0,1)
                    if direction == 0:
                        if isinstance(diagonalLeft, Particle): #if diagonalLeft not empty
                            self.switchWithAnotherParticle(self.i-1, self.j+1, tiles)
                        else:
                            self.moveToEmptyCell(self.i-1, self.j+1, tiles)

                    else:
                        if isinstance(diagonalRight, Particle):
                            self.switchWithAnotherParticle(self.i+1, self.j+1, tiles)
                        else:
                            self.moveToEmptyCell(self.i-1, self.j-1, tiles)


                elif isDiagonalLeftSolid and not isDiagonalRightSolid: #can only move right
                    print(isDiagonalLeftSolid, isDiagonalRightSolid)
                    
                    if isinstance(diagonalRight, Particle): #is either liquid or gas
                        self.switchWithAnotherParticle(self.i+1, self.j+1, tiles)
                    else:
                        self.moveToEmptyCell(self.i+1, self.j+1, tiles)

                elif not isDiagonalLeftSolid and isDiagonalRightSolid: #can only move left
                    
                    if isinstance(diagonalLeft, Particle):
                        self.switchWithAnotherParticle(self.i-1, self.j+1, tiles)
                    else:
                        self.moveToEmptyCell(self.i-1, self.j+1, tiles)
        
        
        except Exception as e:
            pass #print(f"Error: {e}")

            



                
                    



        
    
    


