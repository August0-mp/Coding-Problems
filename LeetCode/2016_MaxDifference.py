class Solution:
    def maximumDifference(self, nums: List[int]) -> int:
        ans = -1
        m = nums[0]
        for n in nums[1::]:
            if n <= m:
                m = n
            else:
                ans = max(ans,n-m)
        return ans
            

# https://leetcode.com/problems/maximum-difference-between-increasing-elements