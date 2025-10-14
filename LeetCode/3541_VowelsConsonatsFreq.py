class Solution:
    def maxFreqSum(self, s: str) -> int:
        vowels = 'aeiou'
        consonants = 'bcdfghjklmnpqrstvwxyz'
        freq_v = {vowel: 0 for vowel in vowels}
        freq_c = {consonant: 0 for consonant in consonants}
        fV = 0
        fC = 0

        for c in s:
            if c in vowels:
                freq_v[c]+=1
                if freq_v[c]>fV:
                    fV=freq_v[c]
            else:
                freq_c[c]+=1
                if freq_c[c]>fC:
                    fC=freq_c[c]
        return fC+fV
                
# https://leetcode.com/problems/find-most-frequent-vowel-and-consonant