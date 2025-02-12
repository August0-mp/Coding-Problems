class Solution:
    def maximumSum(self, nums: List[int]) -> int:
        def sumDigits(n: int) -> int:
            r = 0
            while n > 0:
                r += n % 10
                n //= 10
            return r

        sumList = list(map(sumDigits, nums))

        digitSumMap = {}
        for index, digitSum in enumerate(sumList):
            if digitSum not in digitSumMap:
                digitSumMap[digitSum] = []
            digitSumMap[digitSum].append(nums[index])

        maxSum = -1
        for key in digitSumMap:
            if len(digitSumMap[key]) >= 2:
                sortedNums = sorted(digitSumMap[key], reverse=True)

                currentSum = sortedNums[0] + sortedNums[1]
                if currentSum > maxSum:
                    maxSum = currentSum

        return maxSum

# https://leetcode.com/problems/max-sum-of-a-pair-with-equal-sum-of-digits/