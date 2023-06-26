class Solution:
    def commonFactors(self, a: int, b: int) -> int:
        if(a>b):
            x=b
            y=a
        else:
            x=a
            y=b
        lst=[]
        for i in range(1,x+1):
            if(x%i==0 and y%i==0):
                lst.append(i)
        return (len(lst))
