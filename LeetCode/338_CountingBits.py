class Solution:
    def countBits(self, n: int) -> List[int]:
        ans = []

        for i in range(n+1):
            j = i
            oc = 0
            while j>=1:
                oc+=j%2
                j=j//2
                
            ans.append(oc)
        return ans
    
# https://leetcode.com/problems/counting-bits