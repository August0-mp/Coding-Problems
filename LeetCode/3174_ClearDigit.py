class Solution:
    def clearDigits(self, s: str) -> str:
        ans=[]
        for i in range(len(s)):
            if s[i].isnumeric():
                ans.pop()
            else:
                ans.append(s[i])
        return ''.join(ans)
            
# https://leetcode.com/problems/clear-digits