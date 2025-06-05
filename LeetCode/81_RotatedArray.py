class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        i = 0
        l = len(nums)

        if nums[i]==target:
            return True
        elif nums[i]<target:
            while i<l-1:
                i+=1
                if nums[i]==target:
                    return True
        else:
            while i<l-1:
                i+=1
                if nums[l-i]==target:
                    return True
        return False

# https://leetcode.com/problems/search-in-rotated-sorted-array-ii/