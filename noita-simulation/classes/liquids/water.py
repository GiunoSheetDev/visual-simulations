from classes.liquids.liquid import Liquid

class Water(Liquid):
    def __init__(self, i, j) -> None:
        super().__init__(i, j)
        self.color = (43, 156, 237)

    def update(self, tiles: list[list]) -> list[list]:
        return super().update(tiles)