# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        
        def comparision(node1, node2):
            
            if node1 == None and node2 == None:
                return True
            
            if node1 == None or node2 == None:
                return False
            
            return (node1.val == node2.val) and comparision(node1.left, node2.right) and comparision(node1.right, node2.left)
            
        if root:
            return comparision(root.left, root.right)
        else:
            return True