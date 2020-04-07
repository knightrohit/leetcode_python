# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children

class Solution:
    def maxDepth(self, root: 'Node', depth = 1) -> int:
        
        if root == None:
            return 0
        
        if not root.children and root:
            return depth
        
        height = []
        for node in root.children:
            height.append(self.maxDepth(node, depth+1))
        return max(height)