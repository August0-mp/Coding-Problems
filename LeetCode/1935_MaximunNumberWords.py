class Solution:
    def canBeTypedWords(self, text: str, brokenLetters: str) -> int:
        words = text.split(" ")
        l = len(words)
        
        for w in words:
            for b in brokenLetters:
                if b in w:
                    l-=1
                    break
        return l

# https://leetcode.com/problems/maximum-number-of-words-you-can-type