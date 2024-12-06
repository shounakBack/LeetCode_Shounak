class Solution:
    def maxCount(self, banned: List[int], n: int, maxSum: int) -> int:
        seen=set(banned)
        arr_sum,ele=0,0
        for i in range(1,n+1):
            if i not in seen:
                if arr_sum+i<=maxSum:
                    arr_sum+=i
                    ele+=1
                else:
                    break
        return ele