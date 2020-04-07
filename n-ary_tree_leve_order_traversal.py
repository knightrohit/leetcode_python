#Iterative solution using deque
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children

from collections import deque

class Solution:
    def levelOrder(self, root: 'Node') -> List[List[int]]:
        
        if not root:
            return []
        
        out = []
        node_queue = deque()        
        node_queue.append(root)
        
        while node_queue:
            level = []
            for _ in range(len(node_queue)):
                node = node_queue.popleft()
                level.append(node.val)
                node_queue.extend(node.children)
                
            out.append(level)           
            
        return out 