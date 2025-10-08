class Solution:
    def longestPalindrome(self, s: str) -> str:
        l = len(s)
        ans = ""
        m = 0
        for i in range(l):
            for j in range(l, i, -1):
                sub = s[i:j]
                if sub == sub[::-1]:
                    if j-i > m:
                        ans = sub
                        m = j-i
        return ans

# https://leetcode.com/problems/longest-palindromic-substring