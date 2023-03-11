#Largest Number At Least Twice of Others

class Solution(object):
    def dominantIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        original= list(nums)
        nums.sort()
        i= nums[len(nums)-1]
        if i>=(2*nums[len(nums)-2]):
            return original.index(i)
        else:
            return -1