class Solution:
    def longestMonotonicSubarray(self, nums: List[int]) -> int:    
        ans = 1 
        current_length = 1
        direction = 0  
        
        for x, y in pairwise(nums):
            if x == y:
                current_length = 1
                direction = 0
            elif x > y:
                if direction <= 0:
                    current_length += 1
                else:
                    current_length = 2
                direction = -1
            else:
                if direction >= 0:
                    current_length += 1
                else:
                    current_length = 2
                direction = 1
            ans = max(ans, current_length)
        
        return ans
    
# https://leetcode.com/problems/longest-strictly-increasing-or-strictly-decreasing-subarray/