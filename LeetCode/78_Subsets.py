class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        ans = [[]]
        
        for n in nums:
            for i in range(len(ans)):
                cp = ans[i].copy()
                cp.append(n)
                ans.append(cp)
            
        return ans

# https://leetcode.com/problems/subsets/