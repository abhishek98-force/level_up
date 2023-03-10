# Third Maximum Number
# Given an integer array nums, return the third distinct maximum number in this array. If the third maximum does not exist, return the maximum number.

class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        nums_set=set(nums)
        nums=list(nums_set)
        nums.sort()
        if len(nums)<=2:
            return max(nums)
        else:
            return nums[len(nums)-3]