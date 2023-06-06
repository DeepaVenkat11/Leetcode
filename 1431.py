class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        maximum=max(candies)
        final=[]
        for i in candies:
            if ((i+extraCandies)>=maximum):
                final.append(True)
            else:
                final.append(False)
        return final
