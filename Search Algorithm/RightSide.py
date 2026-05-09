#Given the root of a binary tree, return the values of the nodes you can see from the right side.

from collections import deque

class Node:
    def __init__(self,val=0,left=None,right=None):
        self.val = val
        self.right = right
        self.left = left

def rightSideView(root):

    if not root:
        return []
    
    res = []
    q = deque([root])

    while q:

        level_size = len(q)

        for i in range(level_size):
            node = q.popleft()

            if  i == level_size-1:
                res.append(node.val)
            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)
    return res


n = Node(1,Node(2,Node(5)),Node(3,Node(4)))

print(rightSideView(n))
