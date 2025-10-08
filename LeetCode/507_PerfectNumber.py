class Solution:
    def checkPerfectNumber(self, num: int) -> bool:
        if num <= 1:
            return False
        
        divisors_sum = 1 
        i = 2
        while i * i <= num:
            if num % i == 0:
                divisors_sum += i
                if i != num // i:
                    divisors_sum += num // i
            i += 1
        return divisors_sum == num

# https://leetcode.com/problems/perfect-number/