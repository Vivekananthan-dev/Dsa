from collections import deque
class Node:
    def __init__(self,val=0,left=None,right=None):

        self.val = val
        self.left = left
        self.right = right


def bfsSearch(root):
    
    if not root:
        return []
    
    result = []
    q = deque([root])

    while q:
        level = []
        for _ in range(len(q)):
            node = q.popleft()
            level.append(node.val)

            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)
        result.append(level)
    return result

t = Node(5,Node(1),Node(7,Node(6,Node(3)),Node(8,Node(9),Node(10))))
print(bfsSearch(t))
