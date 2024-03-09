class Particle:
    def __init__(self, i, j) -> None:
        self.i = i
        self.j = j
        self.heat = 0
        self.lifespan = 0

    def moveToEmptyCell(self, targetI: int, targetJ: int, tiles: list[list]) -> list[list]:
        tiles[targetI][targetJ] = self #set self at target position
        tiles[self.i][self.j] = 0 #set current tile = 0
        self.i, self.j = targetI, targetJ #set self coords to target coords
        return tiles
    
    def switchWithAnotherParticle(self, targetI: int, targetJ: int, tiles: list[list]) -> list[list]:
        target = tiles[targetI][targetJ] #get target instance
        tiles[self.i][self.j] = target #set current tile = target
        tiles[targetI][targetJ] = self #set self at target position
        target.i, target.j = self.i, self.j #set target coords to current coords
        self.i, self.j = targetI, targetJ #set self coords to target coords
        return tiles
    
    def applyHeatToNeighborsIfIgnited(self, tiles : list[list]):
        pass

    def checkLifeSpan(self): 
        pass

    def takeDamage(self):
        pass

    def update(self):
        pass
    
    def getNeighbors(self):
        pass
    

