"""
Input: ["2", "1", "+", "3", "*"]
Output: 9
Solution - ((2 + 1) * 3) = 9
"""
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        
        if not tokens:
            return None
        
        stack = []
        operations = {'*' : lambda x, y : x * y,
                     '/' : lambda x, y : int(x / y), 
                     '+' : lambda x, y : x + y,
                     '-' : lambda x, y : x - y
                    }

        for token in tokens:
            
            if token not in operations:
                stack.append(int(token))
                
            else:
                no2, no1 = stack.pop(), stack.pop()
                out = operations[token]
                stack.append(out(no1, no2))
                
        return stack.pop()