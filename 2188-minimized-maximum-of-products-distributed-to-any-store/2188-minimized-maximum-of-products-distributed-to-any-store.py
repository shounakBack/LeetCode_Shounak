class Solution:
    def minimizedMaximum(self, n: int, quantities: List[int]) -> int:
        def helper(limit):
            curr=quantities[0]
            j=0
            for i in range(n):
                if curr<=limit:
                    j+=1
                    if j==len(quantities):
                        return True
                    else:
                        curr=quantities[j]
                else:
                    curr-=limit
            return False
        low,high=0,max(quantities)
        res=0
        while low<=high:
            mid=(low+high)//2
            if helper(mid):
                res=mid
                high=mid-1
            else:
                low=mid+1
        return res