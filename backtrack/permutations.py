"""
Time Complexity = Σ k =1 to N P(N,k)
Space Compleixty = O(N!)
"""
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        
        if not nums:
            return nums
        
        if len(nums) == 1:
            return [nums]       
        
        out = []
        
        def find_p(i=0):
            if i == len(nums):
                out.append(nums[:])
                return

            for j in range(i, len(nums)):
                nums[i], nums[j] = nums[j], nums[i]
                find_p(i + 1)
                nums[i], nums[j] = nums[j], nums[i]                
        
        find_p()
        return out