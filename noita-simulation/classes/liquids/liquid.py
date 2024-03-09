from classes.particle import Particle

class Liquid(Particle):
    def __init__(self, i, j) -> None:
        super().__init__(i, j)

        
    def getNeighbors(self, tiles : list[list]) -> list:
        pass

    def update(self, tiles : list[list]) -> list:
        try:
            bottom = tiles[self.i][self.j+1]
        except: 
            pass