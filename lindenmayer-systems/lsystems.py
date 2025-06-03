import turtle


class LSystem:
    def __init__(self, turtle : turtle.Turtle, variables: list, costants : list | None, axiom: str, rules : list[tuple], turningAngle: int = 90, startingAngle: int = 0, recursionDepth: int = 5, startingPos: tuple = (0, 0)):        
        self.variables = variables
        self.costants = costants
        self.axiom = axiom
        self.rules = rules
        self.drawRules = {}
        self.turningAngle = turningAngle
        self.startingAngle = startingAngle
        self.recursionDepth = recursionDepth
        self.startingPos = startingPos

        self.ruleDict = self.generateRuleDict()
        

        
        self.segmentLen = 1
        

        self.stack = []


        self.t = turtle
        self.t.setheading(self.startingAngle)
        self.t.hideturtle()
        self.t.color("white")
        self.t.penup()
        self.t.goto(self.startingPos[0], self.startingPos[1])
        self.t.pendown()
        

    def push(self):
        self.stack.append((self.t.heading(), self.t.pos()))
    
    def pop(self):
        self.currentangle, pos = self.stack.pop()
        self.t.penup()
        self.t.goto(pos[0], pos[1])
        self.t.pendown()
        self.t.setheading(self.currentangle)

    def generateRuleDict(self) -> dict:
        out = {}
        for rule in self.rules:
            out[rule[0]] = rule[1]
        return out

    def parseAxiom(self):
        self.axiom = self.axiom.translate(str.maketrans(self.ruleDict))

    def generateFinalState(self):
        for _ in range(self.recursionDepth):
            
            self.parseAxiom()

    def draw(self, screen):
        self.generateFinalState()
        screen.tracer(0)
        
        #setup turtle
        for char in self.axiom:
            self.drawRules[char]()
        
        screen.update()
        

    
if __name__ == "__main__":
    screen = turtle.Screen()
    screen.setup(800, 600)
    screen.bgcolor("black")
    

    t = turtle.Turtle()

    sierpinski_arrowhead_curve = LSystem(t, 
                                         variables=["A", "B"],
                                         costants=["+", "-"],
                                         axiom="A",
                                         turningAngle= 60,
                                         rules=[("A", "B-A-B"), ("B", "A+B+A")],
                                         recursionDepth=6,
                                         startingPos=(-300, -250))
    
    sierpinski_arrowhead_curve.drawRules = {
        "A": lambda: t.forward(8),
        "B": lambda: t.forward(8),
        "+": lambda: t.left(sierpinski_arrowhead_curve.turningAngle),
        "-": lambda: t.right(sierpinski_arrowhead_curve.turningAngle)
    }

    #sierpinski_arrowhead_curve.draw(screen)


    cantor_set = LSystem(t,
                         variables=["A", "B"],
                         costants=[],
                         axiom= "A",
                         rules=[("A", "ABA"), ("B", "BBB")],
                         startingPos=(-300, 250))
    
    cantor_set.drawRules = {
        "A": lambda: t.forward(2),
        "B": lambda: (t.penup(), t.forward(2), t.pendown())
    }

    #cantor_set.draw(screen)

    koch_curve = LSystem(t,
                         variables=["F"],
                         costants=["+", "-"],
                         axiom="F",
                         rules= [("F", "F+F-F-F+F")],
                         startingPos=(-350, -250),
                         turningAngle=90,
                         recursionDepth=6)
    
    koch_curve.drawRules = {
        "F" : lambda: t.forward(1),
        "+" : lambda: t.left(koch_curve.turningAngle),
        "-" : lambda: t.right(koch_curve.turningAngle)
    }

    #koch_curve.draw(screen)

    sierpinski_triangle = LSystem(t,
                                  variables=["F", "G"],
                                  costants=["+", "-"],
                                  axiom="F-G-G",
                                  rules=[("F", "F-G+F+G-F"), ("G", "GG")],
                                  turningAngle=120,
                                  startingAngle=90,
                                  startingPos=(-350, -250),
                                  recursionDepth=6)
    
    sierpinski_triangle.drawRules = {
        "F": lambda: t.forward(8),
        "G": lambda: t.forward(8),
        "+": lambda: t.left(sierpinski_triangle.turningAngle),
        "-": lambda: t.right(sierpinski_triangle.turningAngle)}
    
    #sierpinski_triangle.draw(screen)
    

    dragon_curve = LSystem(t,
                           variables=["G", "F"],
                           costants=["+", "-"],
                           axiom= "F",
                           rules=[("F", "F+G"), ("G", "F-G")],
                           turningAngle=90,
                           startingAngle=0,
                           recursionDepth=14)
    
    dragon_curve.drawRules ={
        "F": lambda: t.forward(8),
        "G": lambda: t.forward(8),
        "+": lambda: t.left(dragon_curve.turningAngle),
        "-": lambda: t.right(dragon_curve.turningAngle)
        }
    
    #dragon_curve.draw(screen)

    binaryTree = LSystem(t,
                         variables=["0", "1"],
                         costants=["[", "]"],
                         axiom= "0",
                         rules= [("1", "11"), ("0", "1[0]0")],
                         turningAngle=45,
                         recursionDepth=7,
                         startingAngle=90,
                         startingPos=(0, -250))
    
    binaryTree.drawRules = {
        "0" : lambda : t.forward(4),
        "1" : lambda : t.forward(4),
        "[" : lambda : (binaryTree.push(), t.left(binaryTree.turningAngle)),
        "]" : lambda : (binaryTree.pop(), t.setheading(binaryTree.currentangle - binaryTree.turningAngle))
    }

    #binaryTree.draw(screen)
    
    fractalPlant = LSystem(t, 
                           variables= ["X", "F"],
                           costants= ["+", "-", "[", "]"],
                           axiom= "-X",
                           rules=[("X", "F+[[X]-X]-F[-FX]+X"), ("F", "FF")],
                           turningAngle=25,
                           startingAngle= 90,
                           recursionDepth=8,
                           startingPos=(-350, -250))
    
    fractalPlant.drawRules = {
        "F" : lambda : t.forward(1),
        "X" : lambda : None,
        "-" : lambda : t.right(binaryTree.turningAngle),
        "+" : lambda : t.left(binaryTree.turningAngle),
        "[" : lambda : binaryTree.push(),
        "]" : lambda : binaryTree.pop()
    }

    fractalPlant.draw(screen)

    hilbertCurve = LSystem( t, 
                            variables=["A", "B"],
                            costants=["F", "+", "-"],
                            axiom= "A",
                            rules=[("A", "+BF-AFA-FB+"), ("B", "-AF+BFB+FA-")],
                            turningAngle = 90,
                            recursionDepth= 6,
                            startingPos=(-350, -250))

    hilbertCurve.drawRules = {
        "F" : lambda: t.forward(8),
        "+" : lambda: t.left(hilbertCurve.turningAngle),
        "-" : lambda: t.right(hilbertCurve.turningAngle),
        "A" : lambda: None,
        "B" : lambda: None
    }

    #hilbertCurve.draw(screen)

    turtle.done()
