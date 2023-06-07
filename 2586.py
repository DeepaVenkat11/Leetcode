class Solution:
    def vowelStrings(self, words: List[str], left: int, right: int) -> int:
        count=0
        for word in words[left:right+1]:
                if (word[0]=='a' or word[0]=='e' or word[0]=='i'or      word[0]=='o' or word[0]=='u'):
                    if(word[-1]=='a' or word[-1]=='e' or word[-1] =='i'or word[-1]=='o' or word[-1]=='u'):
                        count+=1
        return count
