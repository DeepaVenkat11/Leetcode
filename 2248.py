class Solution:
    def intersection(self, nums: List[List[int]]) -> List[int]:
        lst=[]
        x=nums[0]
        
        for i in x:
            count=0
            for j in nums:
                if i in j:
                    count+=1
            if count==len(nums):
                lst.append(i)
        lst.sort()
        return lst
