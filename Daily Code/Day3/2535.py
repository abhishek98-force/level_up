#2535. Difference Between Element Sum and Digit Sum of an Array

class Solution(object):
    def differenceOfSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        s=0
        digitsum=0
        for i in nums:
            s=s+i
            if i>9:
                n=i
                while n>0:
                    dsum= n%10
                    n= n//10
                    digitsum= digitsum+dsum
            else:
                digitsum= digitsum+i
        return (s-digitsum)

