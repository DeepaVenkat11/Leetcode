class Solution:
    def addDigits(self, num: int) -> int:
        sum=0
        while(num>0):
            digit=num%10
            sum+=digit
            num=num//10
            if(sum>9 and num==0):
                num=sum
                sum=0
        return sum
