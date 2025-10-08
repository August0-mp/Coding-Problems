class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        ans = ""
        lengths = [len(w) for w in strs]
        l_min = min(lengths)
        for i in range(l_min):
            c = strs[0][i]
            for w in strs:
                if w[i]!=c:
                    return ans   
            ans+=c
        return ans
                
# https://leetcode.com/problems/longest-common-prefix