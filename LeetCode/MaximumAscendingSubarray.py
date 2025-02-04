class Solution:
    def maxAscendingSum(self, nums: List[int]) -> int:
        ans=s=nums[0]
        for x, y in pairwise(nums):
            s=y if y<=x else s+y
            ans=max(ans, s)
        return ans

# https://leetcode.com/problems/maximum-ascending-subarray-sum/