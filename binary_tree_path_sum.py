# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def hasPathSum(self, root: TreeNode, sum: int) -> bool:
        
        self.sum = sum
        self.flag = False

        def traverse(node, val):
            if not node:
                return False
            
            val = val + node.val            
            if not node.left and not node.right:
                if val == self.sum:
                    self.flag = True
            
            else:
                traverse(node.left, val)
                traverse(node.right, val)
                
        traverse(root, 0)
        return self.flag


# Modified
# Smaller code
class Solution:
    def hasPathSum(self, root: TreeNode, sum: int) -> bool:
        
        def traverse(node, val):
            if not node:
                return False
            
            val += node.val            
            if not node.left and not node.right:
                if val == sum:
                    return True
            
            return traverse(node.left, val) or traverse(node.right, val)
        
        return traverse(root, 0)