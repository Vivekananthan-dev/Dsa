class TreeNode:
    def __init__(self,val=0, left = None, right = None):
        self.val = val
        self.left = left
        self.right = right

def isValidBST(root):

    def dfs(node,low, high):
        if not node:
            return True
        if not (low<node.val<high):
            return False
        
        return dfs(node.left,low,node.val) and dfs(node.right,node.val,high)
    return dfs(root,float('-inf'),float("inf"))


t = TreeNode(5,TreeNode(1),TreeNode(4,TreeNode(3),TreeNode(6)))
t1 = TreeNode(2,TreeNode(1),TreeNode(3))

print(isValidBST(t))
print(isValidBST(t1))
