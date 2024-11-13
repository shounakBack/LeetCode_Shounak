class Solution:
    def countPairs(self, nums: List[int], target: int) -> int:
        nums.sort()
        res=0
        low,high=0,len(nums)-1
        while low<high:
            s=nums[low]+nums[high]
            if s<target:
                res+=high-low
                low+=1
            else:
                high-=1
        return res