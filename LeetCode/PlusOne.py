class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        i = len(digits)-1
        while i>=0:
            digits[i]=(digits[i]+1)%10
            if digits[i]>0:
                break
            i-=1
        if i<0:
            digits=[1]+digits
        return digits\
        
# https://leetcode.com/problems/plus-one