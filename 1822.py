class Solution:
    def arraySign(self, nums: List[int]) -> int:
        product= prod(nums)
        if(product>0):
            x=1
        elif(product==0):
            x=0
        else:
            x=-1
        return x
