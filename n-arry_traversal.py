#PreOrder
class Node:
    def __init__(self, val = None, childern = []):
        self.val = val
        self.children = children

class PreOrder:
    def preorder(self, root: 'Node') -> List[int]:
        
        if not root:
            return []

        stack, out = [root], []  
        while stack:
            node = stack.pop()
            out.append(node.val)
            if node.children:
                stack.extend(node.children[::-1])
                
        return out