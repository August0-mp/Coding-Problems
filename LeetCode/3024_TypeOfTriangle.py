class Solution:
    def triangleType(self, nums: List[int]) -> str:
        numsSet = set(nums)
        if len(numsSet)==1:
            return "equilateral"
        
        def triangleIneq():
            if nums[0]+nums[1]<=nums[2] or nums[0]+nums[2]<=nums[1] or nums[2]+nums[1]<=nums[0]:
                return False
            return True
        
        if not triangleIneq():
            return "none"
        if len(numsSet)==2:
            return "isosceles"
        else:
            return "scalene"

# https://leetcode.com/problems/type-of-triangle