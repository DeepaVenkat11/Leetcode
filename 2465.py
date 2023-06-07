    def distinctAverages(self, nums: List[int]) -> int:
        lst=[]
        while(len(nums)>=2):
            minimum=min(nums)
            maximum=max(nums)
            avg=(maximum+minimum)/2
            lst.append(avg)
            nums.remove(maximum)
            nums.remove(minimum)
        return(len(set(lst)))
