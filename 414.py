class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        nums=list(set(nums))
        first=max(nums)
        if(len(nums)>=3):
            nums.remove(first)
            second=max(nums)
            nums.remove(second)
            third=max(nums)
            return third
        else:
            return first
