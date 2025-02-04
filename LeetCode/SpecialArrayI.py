class Solution:
    def isArraySpecial(self, nums: List[int]) -> bool:
        n0 = nums[0]%2
        for i in range(1,len(nums)):
            if nums[i]%2==n0:
                return False
            n0 = nums[i]%2
        return True
            
# https://leetcode.com/problems/special-array-i/