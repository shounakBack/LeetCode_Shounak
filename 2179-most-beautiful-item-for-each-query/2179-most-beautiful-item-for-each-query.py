class Solution:
    def maximumBeauty(self, items: List[List[int]], queries: List[int]) -> List[int]:
        def bs(target):
            out=0
            low,high=0,len(items)-1
            while low<=high:
                mid=(low+high)//2
                if items[mid][0]==target:
                    out=beauty[target]
                    return out
                elif items[mid][0]<target:
                    out=beauty[items[mid][0]]
                    low=mid+1
                else:
                    high=mid-1
            return out
        items.sort()
        n=len(items)
        beauty={}
        max_beauty=0
        for p,b in items:
            max_beauty=max(max_beauty,b)
            beauty[p]=max_beauty
        res=[]
        for q in queries:
            res.append(bs(q))
        return res