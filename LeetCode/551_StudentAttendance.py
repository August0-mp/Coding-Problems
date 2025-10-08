class Solution:
    def checkRecord(self, s: str) -> bool:
        l = len(s)
        ab = 0
        for i in range(l):
            if s[i] == 'A':
                ab += 1
                if ab>1:
                    return False
            elif s[i] == 'L':
                lt = 0
                while i<l and s[i] == 'L':
                    i+=1
                    lt+=1
                    if lt==3:
                        return False
        return True

# https://leetcode.com/problems/student-attendance-record-i