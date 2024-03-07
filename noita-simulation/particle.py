class Particle():
    def __init__(self, id : int):
        colors = [(242, 162, 24)]
        self.id = id
        self.color = colors[id]
        # state #0 -> Solid (NOT TRAVERSABLE) // #1 -> Liquid (TRAVERSABLE) // #2 -> Gas (TRAVERSABLE)
        
    
#i = y TOP 2 BOTTOM
#j = x  LEFT 2 RIGHT

class Sand(Particle):
    def __init__(self, id):
        super().__init__(id)
        self.id = 0
        self.lifetime = -1 #Infinite, TODO change when adding fire so it becomes glass
        self.state = 0

        
