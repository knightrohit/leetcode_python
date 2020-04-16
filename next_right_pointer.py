
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next

from collections import deque

class Solution:
    def connect(self, root: 'Node') -> 'Node':
        
        if not root:
            return root

        level = 0
        queue = deque()
        queue.append(root)
        while queue:
            curr = prev = None
            for _ in range(2**level):
                curr = queue.popleft()
                if curr.left:
                    queue.append(curr.left)
                    queue.append(curr.right)
                if not prev:
                    prev = curr
                else:
                    prev.next = curr
                prev = curr
            level += 1
            
        return root