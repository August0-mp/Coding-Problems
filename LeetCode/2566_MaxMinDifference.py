class Solution:
    def minMaxDifference(self, num: int) -> int:
        s = str(num)
        ch = s[0]
        l = len(s)
        m = M = ''
        for i in range(l):
            CH = s[i]
            if CH != '9':
                break
        for i in range(l):
            if s[i] == ch:
                m+=('0')
            else:
                m+=(s[i])
            if s[i] == CH:
                M+='9'
            else:
                M+=s[i]

        return int(M)-int(m)

# https://leetcode.com/problems/maximum-difference-by-remapping-a-digit