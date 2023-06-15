class Solution:
    def getCommon(self, nums1: List[int], nums2: List[int]) -> int:
        lst=[]
        nums1=set(nums1)
        num2=set(nums2)
        num=nums1.intersection(nums2)
        try:
            if(min(list(num))>0 ):
                return min(list(num))
        except:
            return -1
