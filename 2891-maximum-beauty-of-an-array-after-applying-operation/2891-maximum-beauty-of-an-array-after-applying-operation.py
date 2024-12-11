class Solution:
    def maximumBeauty(self, nums: List[int], k: int) -> int:
        nums.sort()
        res=-math.inf
        start,end,n=0,0,len(nums)
        for end in range(n):
            while nums[end]-nums[start]>2*k:
                start+=1
            res=max(res,end-start+1)
        return res