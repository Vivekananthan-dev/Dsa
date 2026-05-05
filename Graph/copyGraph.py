#create a Node
class Node:
    def __init__(self,val=0,neighbors=None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
    
    def printGraph(self,node,visited=None):
        if visited is None:
            visited = set()
        if node in visited:
            return
        visited.add(node)

        print(f"Node {node.val} neighbours: {[n.val for n in node.neighbors]}")

        for n in node.neighbors:
            self.printGraph(n,visited)
        


def cloneGraph(node):
    if not node:
        return None
    
    old_to_new = {}

    def dfs(curr):
        if curr in old_to_new:
            return old_to_new[curr]
        
        clone = Node(curr.val)
        old_to_new[curr] = clone

        for n in curr.neighbors:
            clone.neighbors.append(dfs(n))
        
        return clone
    return dfs(node)


n1 = Node(1)
n2 = Node(2)
n3 = Node(3)
n4 = Node(4)

n1.neighbors = [n2,n4]
n2.neighbors = [n1,n3]
n3.neighbors = [n2,n4]
n4.neighbors = [n1,n3]

cloned = cloneGraph(n1)

cloned.printGraph(cloned)


