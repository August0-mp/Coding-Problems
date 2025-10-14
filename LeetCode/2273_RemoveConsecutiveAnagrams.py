class Solution:
    def removeAnagrams(self, words: List[str]) -> List[str]:
        ans = []
        l = len(words)
        i = 0
        while i<l:
            s_i = ''.join(sorted(words[i]))
            ans.append(words[i])
            while i+1<l and s_i == ''.join(sorted(words[i+1])):
                i+=1
            i+=1
        return ans
    
# https://leetcode.com/problems/find-resultant-array-after-removing-anagrams