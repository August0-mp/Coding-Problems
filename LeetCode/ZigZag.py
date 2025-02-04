class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1:
            return s
        
        ans = ["" for _ in range(numRows)]
        i = 0
        sign = 1
        
        for c in s:
            ans[i] += c
            i += sign
            
            if i == 0 or i == numRows - 1:
                sign *= -1
        
        return "".join(ans)

# https://leetcode.com/problems/zigzag-conversion/