class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        lst=[]
        for i in range(len(nums)-1):
            j=i+1
            while(j<len(nums)):
                if (nums[i]+nums[j])==target:
                    lst.append(i)
                    lst.append(j)
                    break
                else:
                    j+=1
        return(lst)
