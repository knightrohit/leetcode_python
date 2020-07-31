"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""
#Using DFS
class Solution:
    
    def __init__(self):
        self.visited = {}
    
    def cloneGraph(self, node: 'Node') -> 'Node':

        if not node:
            return node
        
        if node in self.visited:
            return self.visited[node]

        clone_node = Node(node.val, [])
        self.visited[node] = clone_node
        
        if node.neighbors:
            for child in node.neighbors:
                clone_node.neighbors.append(self.cloneGraph(child))
                
        return clone_node