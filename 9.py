class Solution:
    def isPalindrome(self, x: int) -> bool:
        y=str(x)
        string=""
        for i in y[::-1]:
            string+=i
        return string==y
