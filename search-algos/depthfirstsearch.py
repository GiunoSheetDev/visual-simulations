from config import *

class depthfirstsearch:
    def __init__(self):
        self.tree = tree
        self.fringe = []
        self.path = []
        
    def expandNode(self, node: str, depth: int) -> None:
        for node in self.tree[node]:
            self.fringe.append((node, depth))

    def search(self, node: str, depth: int, path: list) -> bool:
        path.append(node)
        self.fringe.append((node, depth))

        
        
        if node == "g":  # Goal condition
            print("Path to goal:", " -> ".join(path))
            return 1
        
        if self.tree[node] == []:  # Leaf node
            path.pop()
            self.fringe.pop()
            return 0 
        
        

        # Process children in a depth-first manner
        for child in self.tree[node]:  # Directly iterate over child nodes
            if self.search(child, depth + 1, path):
                return 1 #if child already found solution just return to interrupt after first solution
        
        path.pop()
        self.fringe.pop()

    def run(self):
        currentNode = "s"
        currentDepth = 0

        self.expandNode(currentNode, currentDepth)

        self.search(currentNode, currentDepth, self.path)


if __name__ == "__main__":
    dfs = depthfirstsearch()
    dfs.run()
        