class Solution:
    def climbStairs(self, n: int) -> int:
        if n<4:
            return n
        
        dw1 = 2
        dw2 = 3

        while n>3:
            dw = dw1
            dw1 = dw2
            dw2 = dw+dw2
            n-=1
        
        return dw2

# https://leetcode.com/problems/climbing-stairs/
