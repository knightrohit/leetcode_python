'''
Time complexity = O(N^2*log N)
Space complexity = O(N)
'''

import math

class Solution:
    def numPoints(self, points: List[List[int]], r: int) -> int:
        ans = 1
        for x, y in points:
            out = []
            for x0, y0 in points:
                
                d = ((x0 - x)**2 + (y0-y)**2)**0.5
                if (x!= x0 or y != y0) and d <= 2*r:
                    
                    angle = math.atan2(y0 - y, x0 - x)
                    delta = math.acos(d/(2*r))
                    #entry
                    out.append((angle - delta, 1))
                    #exit
                    out.append((angle + delta, -1))
            
            val = 1
            for _ , entry in sorted(out, key = lambda x: (x[0], -x[1])):
                val = val + entry
                ans = max(ans, val)
                
        return ans