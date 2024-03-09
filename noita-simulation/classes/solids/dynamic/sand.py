from classes.solids.dynamic.dynamicSolid import DynamicSolid


class Sand(DynamicSolid):
    def __init__(self, i, j) -> None:
        super().__init__(i, j)
        self.color = (255, 159, 25)

    def update(self, tiles: list[list]) -> list[list]:
        return super().update(tiles)

    

    