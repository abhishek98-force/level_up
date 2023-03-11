


# my original ans but dodnt get pass due to time limit exceeded

class Solution(object):
    def pivotIndex(self, nums):
        ans=-1  
        i=0
        while ans==-1 and i <len(nums):
            if i!=0 and i!=len(nums)-1:               
                    x=0
                    y=0
                    for j in range(0,i):
                        x=x+nums[j]
                    for k in range(i+1, len(nums)):
                        y=y+nums[k]
                    if x==y:
                        ans=i
                        break
            elif i==0: 
                    x=0
                    for j in range(1,len(nums)):
                        x=x+nums[j]
                    if x==0:
                        ans=0
            elif i==len(nums)-1:
                    x=0
                    for j in range(0,len(nums)-1):
                        x=x+nums[j]
                    if x==0:
                        ans=len(nums)-1
            i=i+1
        return ans
        


# modified ans

class Solution(object):
    def pivotIndex(self, nums):
        i=0
        x=0
        y=0
        s=sum(nums)
        while i <len(nums):        
            y=s-x-nums[i]
            if x==y:
                return i
            x=x+nums[i]
            i=i+1
        return -1