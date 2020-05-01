class Solution:
    def isValid(self, s: str) -> bool:
        
        if s == None:
            return None
        
        if s == '':
            return True
        
        if len(s) == 1:
            return False
        
        stack = []
        
        for ch in s:
            if not stack:
                stack.append(ch)
                continue
            
            prev_item = stack[-1]
            
            if (ch == ')' and prev_item == '(') or (ch == '}' and prev_item == '{') or (ch == ']' and prev_item =='['):
                stack.pop()
                continue
            
            stack.append(ch)
            
        return len(stack) == 0


####################################
# Little clean code using dictionary
####################################
class Solution:
    def isValid(self, s: str) -> bool:
        
        if s == None:
            return None
        
        if s == '':
            return True
        
        if len(s) == 1:
            return False
        
        stack = []
        mappings = {')':'(', ']':'[', '}':'{'}
        
        for ch in s:
            if not stack:
                stack.append(ch)
                continue
                
            if ch in mappings:
                prev_item = stack[-1]

                if mappings[ch] == prev_item:
                    stack.pop()
                    continue
            
            stack.append(ch)
            
        return not stack
            