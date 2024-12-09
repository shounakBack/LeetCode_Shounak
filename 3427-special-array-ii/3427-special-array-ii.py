class Solution:
    def isArraySpecial(self, nums: List[int], queries: List[List[int]]) -> List[bool]:
        n=len(nums)
        res=[]
        prefix=[0]*n
        for i in range(1,n):
            if nums[i-1]%2==nums[i]%2:
                prefix[i]=prefix[i-1]+1
            else:
                prefix[i]=prefix[i-1]
        for start,end in queries:
            temp=((prefix[end]-prefix[start])==0)
            res.append(temp)
        return res