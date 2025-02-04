class Solution:
    def check(self, nums: List[int]) -> bool:
        n0 = nums[0]
        c = 0
        l = len(nums)
        for i in range(l+1):
            if nums[i%l]<n0:
                c+=1
                if c>1:
                    return False
            n0 = nums[i%l]

        return True
# https://leetcode.com/problems/check-if-array-is-sorted-and-rotated