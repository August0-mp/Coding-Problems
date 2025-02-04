class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        # lh = len(haystack)
        # ln = len(needle)
        # for i in range(lh):
        #     j=0
        #     for j in range(ln):
        #         if(i+j==lh or haystack[i+j]!=needle[j]):
        #             break
        #         else:
        #             j+=1
        #     if(ln==j):
        #         return i
        # return -1

        if needle in haystack:
            return haystack.find(needle)

        return -1

# https://leetcode.com/problems/find-the-index-of-the-first-occurrence-in-a-string/