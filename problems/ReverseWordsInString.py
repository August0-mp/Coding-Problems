class Solution:
    def reverseWords(self, s: str) -> str:
        ans = ""
        for w in reversed(s.split(' ')):
            if w=='':
                continue
            ans+=w
            ans+=' '
            
        return ans[:-1]
            
# https://leetcode.com/problems/reverse-words-in-a-string