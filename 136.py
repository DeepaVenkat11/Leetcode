class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        for i in nums:
            nums.remove(i)
            if i not in nums:
                return i
                
