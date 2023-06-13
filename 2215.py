class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        lst1=[]
        lst2=[]
        final=[]
        for i in nums1:
            if i not in nums2:
                lst1.append(i)
        final.append(set(lst1))
        for i in nums2:
            if i not in nums1:
                lst2.append(i)
        final.append(set(lst2))
        return final
        
