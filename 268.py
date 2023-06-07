class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        maximum=max(nums)
        for i in range (maximum+1):
            if i not in nums:
                return i
            else:
                flag=1
        if flag==1:
            return maximum+1
