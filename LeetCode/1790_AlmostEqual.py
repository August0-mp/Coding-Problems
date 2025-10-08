class Solution:
    def areAlmostEqual(self, s1: str, s2: str) -> bool:
        if s1 == s2:
            return True
        m = []
        for i in range(len(s1)):
            if s1[i] != s2[i]:
                m.append(i)
        
        if len(m) != 2:
            return False
        
        i, j = m
        return s1[i] == s2[j] and s1[j] == s2[i]

# https://leetcode.com/problems/check-if-one-string-swap-can-make-strings-equal/