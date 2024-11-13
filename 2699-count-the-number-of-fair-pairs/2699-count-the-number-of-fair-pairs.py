class Solution:
    def countFairPairs(self, nums: List[int], lower: int, upper: int) -> int:
        def helper(target):
            low,high=0,n-1
            res=0
            while low<high:
                s=nums[low]+nums[high]
                if s<target:
                    res+=high-low
                    low+=1
                else:
                    high-=1
            return res
        n=len(nums)
        nums.sort()
        return helper(upper+1)-helper(lower)