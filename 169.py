class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        value=set(nums)
        for x in value:
            if(nums.count(x))>(len(nums)/2):
                max=x
        return max
