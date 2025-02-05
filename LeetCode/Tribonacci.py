class Solution:
    def tribonacci(self, n: int) -> int:
        if n==0:
            return 0
        t0, t1, t2 = 0, 1, 1
        
        for _ in range(n-2):
            t22 = t2
            t2 += t0+t1
            t0 = t1
            t1 =t22
        return t2

# https://leetcode.com/problems/n-th-tribonacci-number/
