class Solution:
    def maximumSubarraySum(self, nums: List[int], k: int) -> int:
        start,end,n=0,0,len(nums)
        f=defaultdict(int)
        s=0
        res=-math.inf
        while end<n:
            ch=nums[end]
            f[ch]+=1
            s+=ch
            if end-start+1<k:
                end+=1
            elif end-start+1==k:
                if len(f)==k:
                    res=max(res,s)
                ch=nums[start]
                s-=ch
                f[ch]-=1
                if f[ch]==0:
                    del f[ch]
                start+=1
                end+=1
        if res==-math.inf:
            return 0
        return res