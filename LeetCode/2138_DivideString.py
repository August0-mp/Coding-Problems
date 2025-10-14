class Solution:
    def divideString(self, s: str, k: int, fill: str) -> List[str]:
        l = len(s)
        if k>l:       
            s+=fill*(k-l)
        if l//k > 0:
            s+=fill*(k-l%k)
        return [s[i:i+k] for i in range(0,l,k)]
    
# https://leetcode.com/problems/divide-a-string-into-groups-of-size-k