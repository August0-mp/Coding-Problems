class Solution:
    def kthCharacter(self, k: int) -> str:
        word = 'a'
        while len(word)<k:
            l = len(word)
            for i in range(l):
                ch = chr((ord(word[i])+1-ord('a'))%26+ord('a'))
                word += ch
        return word[k-1]
    
# https://leetcode.com/problems/find-the-k-th-character-in-string-game-i