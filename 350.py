class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        lst=[]
        if(len(nums1)<=len(nums2)):
            num1=nums1
            num2=nums2
        else: 
            num1=nums2
            num2=nums1

        for i in num1:
            if(i in num2):
                lst.append(i)
                num2.remove(i)
        return lst
