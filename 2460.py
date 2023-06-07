class Solution:
    def applyOperations(self, nums: List[int]) -> List[int]:
    
        for i in range(len(nums)-1):
            if nums[i]==nums[i+1]:
                nums[i]=nums[i]*2
                nums[i+1]=0
        lst1=[]
        lst2=[]
        for i in nums:
            if i!=0:
                lst1.append(i)
            else:
                lst2.append(i)
        return lst1+lst2
