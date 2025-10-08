class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        l = len(word)

        if l<2:
            return True
        
        # All non-capital letters
        if ord(word[0])>96:
            for w in word:
                if ord(w)<97:
                    return False
            return True
        
        # All capital letters
        if ord(word[1])<97:
            for w in word:
                if ord(w)>96:
                    return False
            return True
        
        else:
            for w in word[1:]:
                if ord(w)<97:
                    return False
            return True

# https://leetcode.com/problems/detect-capital
