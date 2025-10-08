class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        first_row = {c for c in "qwertyuiopQWERTYUIOP"}
        second_row = {c for c in "asdfghjklASDFGHJKL"}
        third_row = {c for c in "zxcvbnmZXCVBNM"}
        ans = []

        for w in words:
            t = True
            if w[0] in first_row:
                for c in w:
                    if c not in first_row:
                        t = False
                        break
            elif w[0] in second_row:
                for c in w:
                    if c not in second_row:
                        t = False
                        break
            if w[0] in third_row:
                for c in w:
                    if c not in third_row:
                        t = False
                        break

            if t:
                ans.append(w)
        return ans

# https://leetcode.com/problems/keyboard-row/description/