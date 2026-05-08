class Node:
    def __init__(self,val=0,left=None,right=None):
        self.val = val
        self.left = left
        self.right = right

class Code:

    def serialize(self,root):

        def dfs(node):

            if not node:
                vals.append("null")
                return
            
            vals.append(str(node.val))
            dfs(node.left)
            dfs(node.right)
        
        vals = []
        dfs(root)
        return ",".join(vals)
    
    def deserialize(self,data):

        vals = data.split(",")
        self.i = 0
        
        def dfs():
            
            if vals[self.i] == "null":
                self.i += 1
                return None
            node = Node(int(vals[self.i]))
            self.i += 1
            node.left = dfs()
            node.right = dfs()
            return node
        
        return dfs()

root = Node(1,Node(2), Node(3,Node(4),Node(5)))

c = Code()

s = c.serialize(root)
print("Serialized: ",s)

d = c.deserialize(s)
print(f"Deserialize values: {d.val} - {d.left.val} - {d.right.val}")