class Solution:
    def distributeCandies(self, candyType: List[int]) -> int:
        candySet = len(set(candyType))
        value = len(candyType) // 2
        if(value<=candySet):
            return value
        else:
            return candySet
