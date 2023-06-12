class Solution:
    def findNonMinOrMax(self, nums: List[int]) -> int:
        if(len(nums)>2):
           minimum = min(nums)
           maximum = max(nums)
           nums.remove(maximum)
           nums.remove(minimum)
           return(nums[0])
        else:
            return -1
        
