class Solution:
    def findPoisonedDuration(self, timeSeries: List[int], duration: int) -> int:
        if len(timeSeries) == 0 or duration == 0:
            return 0
        ans = 0
        poisonedUntil = 0
        for attack in timeSeries:
            if attack < poisonedUntil:
                ans -= poisonedUntil-attack-duration
            else:
                ans+=duration
            poisonedUntil = attack+duration
        return ans

# https://leetcode.com/problems/teemo-attacking