class Solution:
    def smallestEvenMultiple(self, n: int) -> int:
        value=n
        i=2
        while(value):
            if(value%2==0 and value%n==0):
                return value
                break
            else:
                value*=i
