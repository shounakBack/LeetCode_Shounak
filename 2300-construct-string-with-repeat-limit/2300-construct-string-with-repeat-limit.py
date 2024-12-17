from heapq import *
class Solution:
    def repeatLimitedString(self, s: str, repeatLimit: int) -> str:
        res=""
        q=[]
        f=defaultdict(int)
        for ch in s:
            f[ch]+=1
        for ch,freq in f.items():
            heappush(q,(-ord(ch),freq))
        while q:
            ch,freq=heappop(q)
            used=min(freq,repeatLimit)
            res+=chr(-ch)*used
            if freq>repeatLimit and q:
                ch2,freq2=heappop(q)
                res+=chr(-ch2)
                if freq2>1:
                    heappush(q,(ch2,freq2-1))
                heappush(q,(ch,freq-repeatLimit))
        return res