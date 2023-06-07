class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        value=zip(heights,names)
        lst=[]
        for i,j in sorted(value):
            lst.append(j)
        return lst[::-1]
             
