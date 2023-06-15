class Solution:
    def differenceOfSum(self, nums: List[int]) -> int:
        sum1=0
        sum2=0
        for i in nums:
            sum1+=i
        for i in nums:
            if(i>9):
                while(i>0):
                    dig=i%10
                    sum2+=dig
                    i=i//10
            else:
                sum2+=i
        return(sum1-sum2)
