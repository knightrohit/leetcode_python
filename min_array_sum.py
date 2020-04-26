"""
Input: s = 7, nums = [2,3,1,2,4,3]
Output: 2 => [4,3] is the least sum
"""
class Solution:
    def minSubArrayLen(self, s: int, nums: List[int]) -> int:
        
        if not nums:
            return 0       
        
        curr_pos = 0
        sum_val = 0
        out = float('inf')
        
        for i in range(len(nums)):
            sum_val += nums[i]
            
            while sum_val >= s:
                out = min(out, i - curr_pos + 1)
                sum_val -= nums[curr_pos]
                curr_pos += 1
                
        return out if out != float('inf') else 0