class Solution:
    def pivotInteger(self, n: int) -> int:
        sum1=0
        for i in range(1,n+1):
            sum1+=i
            sum2=0
            for x in range(i,n+1):
                sum2+=x
            if (sum1==sum2):
                num=i
                break
            else:
                num=-1
        return num   
