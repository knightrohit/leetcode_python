# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children

# Calculate max depth using dfs
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


# Calculate max depth using bfs
from collections import deque
class BFSSolution:
    def maxDepth(self, root: 'Node') -> int:
        
        if root == None:
            return 0
               
        if not root.children and root:
            return 1
        
        depth = 0
        queue = deque() 
        queue.append(root)
        
        while queue:
            temp = []
            for _ in range(len(queue)):
                node = queue.popleft()
                temp.extend(node.children)

            queue.extend(temp)
            depth +=1
        
        return depth