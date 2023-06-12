class Solution:
    def isFascinating(self, n: int) -> bool:
        sum1=2*n
        sum2=3*n
        sum=str(n)+str(sum1)+str(sum2)
        num='123456789'
        flag=0
        if(len(sum)==9):
            for i in num:
                if(i not in sum ):
                   flag=1
                   break

            return flag==0
