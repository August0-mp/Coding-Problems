class Solution:
    def maxDifference(self, s: str) -> int:
        freq = {}
        min_even = 100
        max_odd = 1

        for c in s:
            if c not in freq:
                freq[c] = 0
            freq[c] += 1 
        for v in freq.values():
            if v%2==0 and v<min_even:
                    min_even = v
            elif v%2!=0 and v>max_odd:
                    max_odd = v
            
        return max_odd-min_even
            
# https://leetcode.com/problems/maximum-difference-between-even-and-odd-frequency-i