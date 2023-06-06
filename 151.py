class Solution:
    def reverseWords(self, s: str) -> str:
        s=s.split()[::-1]
        sentence=""
        for word in s:
            sentence+=word+" "
        return sentence.rstrip(sentence[-1])
