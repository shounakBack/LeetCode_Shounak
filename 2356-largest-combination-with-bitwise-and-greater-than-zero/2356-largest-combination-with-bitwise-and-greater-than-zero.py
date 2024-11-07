class Solution:
    def largestCombination(self, candidates: List[int]) -> int:
        res=0
        for i in range(24):
            count=0
            for n in candidates:
                if (n & (1<<i))!=0:
                    count+=1
            if count>res:
                res=count
        return res
                    
