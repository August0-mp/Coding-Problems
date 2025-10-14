class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        if n == 0:
            return False
        while n%2 == 0:
            if n//2 != n/2:
                return False
            n/=2
        if n==1:
            return True
        return False

# https://leetcode.com/problems/power-of-two