class Solution:
    def countSeniors(self, details: List[str]) -> int:
        count=0
        for x in details:
            if(x[11]+x[12]>'60'):
                count+=1
        return count
