class Solution:
    def hasIncreasingSubarrays(self, nums: List[int], k: int) -> bool:
        def isIncreasing(idx: int) -> bool:
            for i in range(idx + 1, idx + k):
                if nums[i - 1] >= nums[i]:
                    return False
            return True

        n = len(nums)
        for i in range(n - k + 1):
            if isIncreasing(i) and i + 2 * k <= n and isIncreasing(i + k):
                return True

        return False

# https://leetcode.com/problems/adjacent-increasing-subarrays-detection-i