class Solution:
    def licenseKeyFormatting(self, s: str, k: int) -> str:
        # s = "2-5g-3-JASDS-SDASDASD"
        ans = ""
        cnt = 0
        l = len(s)
        for i in range(l-1, -1, -1):
            if s[i] != '-':
                if cnt%k == 0:
                    ans = '-' + ans
                if ord(s[i])>96:
                    ans = chr(ord(s[i])-32)+ans
                else:
                    ans = s[i]+ans
                cnt+=1
        
        return ans[:-1]

# https://leetcode.com/problems/license-key-formatting