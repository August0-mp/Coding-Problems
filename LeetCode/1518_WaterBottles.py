class Solution:
    def numWaterBottles(self, numBottles: int, numExchange: int) -> int:
        ans = 0
        emptyBottles = 0

        while numBottles > 0:
            ans += numBottles
            emptyBottles += numBottles
            numBottles = emptyBottles//numExchange
            emptyBottles = emptyBottles%numExchange
        
        return ans

# https://leetcode.com/problems/water-bottles