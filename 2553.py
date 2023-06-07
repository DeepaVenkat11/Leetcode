class Solution:
    def separateDigits(self, nums: List[int]) -> List[int]:
        lst=[]
        final=[]
        for num in nums:
            num=str(num)
            for i in num:
                lst.append(int(i))
        return lst
