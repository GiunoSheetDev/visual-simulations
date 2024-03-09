from classes.particle import Particle

class StaticSolid(Particle):
    def __init__(self, i, j) -> None:
        super().__init__(i, j)

    def update(self, tiles: list[list]) -> list[list]:
        self.applyHeatToNeighborsIfIgnited(tiles)
        self.takeDamage()
        self.checkLifeSpan()
        return tiles