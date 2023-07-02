class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s=list(s)
        t=list(t)
        lent=len(t)
        lens=len(s)
        count=0
        for i in s:
            if i in t:
                count+=1
                t.remove(i)

        if(count==lens and lent==lens):
            return True
        else:
            return False