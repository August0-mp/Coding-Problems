class Solution:
    def isHappy(self, n: int) -> bool:
        def rec(seen, n):
            s = 0
            while n > 0:
                x = n % 10
                s += x ** 2
                n = n // 10
            if s == 1:
                return True
            if s in seen:
                return False
            seen.add(s)
            return rec(seen, s)
        
        seen = set()
        return rec(seen, n)
    
# https://leetcode.com/problems/happy-number/