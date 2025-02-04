class Solution:
    def climbStairs(self, n: int) -> int:
        if n<=3: 
            return n

        p1 = 3
        p2 = 2
        ans = p1+p2

        for _ in range(3,n):
            ans = p1+p2
            p2 = p1
            p1 = ans
        
        return ans
    
# https://leetcode.com/problems/climbing-stairs/