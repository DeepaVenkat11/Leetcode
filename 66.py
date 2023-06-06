rom typing import List
class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        value=''
        for i in digits:
            value+=str(i)
        value=int(value)+1
        lst=[]
        add=[]
        while(value>0):
            dig=value%10
            lst.append(dig)
            value//=10
        for i in lst[::-1]:
            add.append(i)
        return add
