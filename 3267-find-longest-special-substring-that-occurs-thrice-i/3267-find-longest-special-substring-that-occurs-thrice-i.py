class Solution:
    def maximumLength(self, s: str) -> int:
        n=len(s)
        f=defaultdict(int)
        res=-math.inf
        for i in range(n):
            count=1
            f[(s[i],count)]+=1
            for j in range(i,n):
                if j+1<n and s[j]==s[j+1]:
                    count+=1
                    f[(s[i],count)]+=1
                else:
                    break
        for key,val in f.items():
            if val>=3:
                res=max(res,key[1])
        if res==-math.inf:
            return -1
        return res