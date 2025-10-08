class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        ans = 0
        t = 0
        for n in nums:
            if n==1:
                t+=1
            else:
                if t>ans:
                    ans=t
                t=0
        return max(t,ans)

# https://leetcode.com/problems/max-consecutive-ones/