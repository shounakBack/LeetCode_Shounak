from heapq import *
class Solution:
    def shortestSubarray(self, nums: List[int], k: int) -> int:
        q=[]
        s=0
        res=math.inf
        for i,n in enumerate(nums):
            s+=n
            if s>=k:
                res=min(res,i+1)
            while q and s-q[0][0]>=k:
                res=min(res,i-heappop(q)[1])
            heappush(q,((s,i)))
        if res==math.inf:
            return -1
        return res