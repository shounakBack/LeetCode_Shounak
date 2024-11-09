class Solution:
    def getMaximumXor(self, nums: List[int], maximumBit: int) -> List[int]:
        n=len(nums)
        prefix=[0]*n
        prefix[0]=nums[0]
        res=[0]*n
        for i  in range(1,n):
            prefix[i]=prefix[i-1]^nums[i]
        mask=(1<<maximumBit)-1
        for i in range(n):
            res[i]=prefix[n-1-i]^mask
        return res