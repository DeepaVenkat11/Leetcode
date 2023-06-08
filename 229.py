class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        value=set(nums)
        lst=[]
        for x in value:
            if(nums.count(x))>(len(nums)/3):
                lst.append(x)
        return lst
