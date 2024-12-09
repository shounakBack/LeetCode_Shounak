from heapq import *
class Solution:
    def maxTwoEvents(self, events: List[List[int]]) -> int:
        q=[]
        events.sort()
        res,ans=0,0
        for start,end,val in events:
            while q and start>q[0][0]:
                res=max(res,q[0][1])
                heappop(q)
            ans=max(ans,res+val)
            heappush(q,(end,val))
        return ans