from config import *

class breadthfirstsearch:
    def __init__(self):
        self.tree = tree
        self.path = []
        self.fringe = []

    def expandNode(self, node:str, depth: int) -> None:
        for node in self.tree[node]:
            self.fringe.append((node, depth))

    def search(self, node: str, depth: int, path: list) -> bool:

        if node == "g":
            print("Path to goal:", " -> ".join(path))
            return 1
        
        if self.tree[node] == []:
            return 0
        
        shallowestDepth = min(self.fringe, key=lambda x: x[1])[1]
        nodesToCheck = list(filter(lambda x: x[1] == shallowestDepth, self.fringe))

        for nodes in nodesToCheck:
            if self.search(nodes, depth+1, path):
                return 1

    def run(self):
        currentNode = "s"
        currentDepth = 0

        self.expandNode(currentNode, currentDepth)

        self.search(currentNode, currentDepth, self.path)

if __name__ == "__main__":
    bfs = breadthfirstsearch()
    bfs.run()