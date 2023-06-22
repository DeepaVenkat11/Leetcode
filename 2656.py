class Solution:
    def maximizeSum(self, nums: List[int], k: int) -> int:
        maximum = max(nums)
        sum=0
        for i in range(k):
            sum=sum+maximum
            maximum=maximum+1
            
        return sum
