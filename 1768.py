class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        string=''
        if len(word1)<=len(word2):
            smallword=word1
            bigword=word2
        else:
            smallword=word2
            bigword=word1
        for i in range(len(smallword)):
            string=string+word1[i]+word2[i]
        n=len(bigword)-len(smallword)
        if n==0:
            return string
        else:
            for i in range(len(smallword),len(bigword)):
                string+=bigword[i]
            return string
