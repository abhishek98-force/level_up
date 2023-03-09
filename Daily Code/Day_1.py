class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        k=len(nums)
        for i in range(len(nums)-1,-1,-1):   
            if nums[i]==val:
                #nums.remove(nums[i])
                del nums[i]
                k=k-1
        return k