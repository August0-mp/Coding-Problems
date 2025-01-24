class Solution:
    def fib_aux(self, n1: int, n2: int):
        return n1 + n2, n1

    def fib(self, n: int) -> int:
        n1, n2 = 0, 1
        for _ in range(n-1):  
            n1, n2 = n2, n1 + n2  
        return n2  
    
# https://leetcode.com/problems/fibonacci-number/