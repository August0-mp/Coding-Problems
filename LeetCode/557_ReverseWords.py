class Solution:
    def reverseWords(self, s: str) -> str:
        arr = s.split(sep = ' ')
        l = len(arr)
        for i in range(l):
            arr[i] = arr[i][::-1]

        return ' '.join(arr)

# https://leetcode.com/problems/reverse-words-in-a-string-iii/description/