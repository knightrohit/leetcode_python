#Recursion solution
class Solution:
    def postorder(self, root: 'Node') -> List[int]:
        if not root:
            return []
            
        self.out = []
        if root.children:
            self.traverse(root)
        else:
            self.out.append(root.val)
        return self.out
            
    
    def traverse(self, node):
        
        if node.children:
            for ch_node in node.children:
                self.traverse(ch_node)
            #Add parent node
            self.out.append(node.val)
        else:
            self.out.append(node.val)


#Iteration solution
class Solution:
    def postorder(self, root: 'Node') -> List[int]:
        if not root:
            return []
        
        stack, out  = [root], []
        
        while stack:
            node = stack.pop()
            out.append(node.val)
            for c in node.children:
                stack.append(c)
            
        return out[::-1]