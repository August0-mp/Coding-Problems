class Solution:
    def removeOccurrences(self, s: str, part: str) -> str:
        lp = len(part)

        ans=s
        while True:
            temp=ans
            ans = ans.replace(part, "", 1)
            if temp==ans:
                return ans

# https://leetcode.com/problems/remove-all-occurrences-of-a-substring