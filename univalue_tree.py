# Definition for a binary tree node.
# Recursion
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def countUnivalSubtrees(self, root: TreeNode) -> int:
        
        self.count = 0
        def traverse(node):            
            if not node:
                return False
            if node.left == node.right == None:
                self.count += 1
                return True
    
            univ = True
            if node.left:
                univ = traverse(node.left) and  node.left.val == node.val
                
            if node.right:
                univ = traverse(node.right) and univ and node.right.val == node.val
                    
            self.count += univ
            return univ
        
        traverse(root)
        return self.count
        