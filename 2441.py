class Solution:
    def findMaxK(self, nums: List[int]) -> int:
        arr=[0]
        for i in range(len(nums)):
            j=i+1
            while(j<len(nums)):
                if(nums[i]+nums[j]==0):
                    arr.append(abs(nums[i]))
                    j+=1
                else:j+=1
        if(max(arr)!=0) :         
            return(max(arr))
        else:
            return -1
