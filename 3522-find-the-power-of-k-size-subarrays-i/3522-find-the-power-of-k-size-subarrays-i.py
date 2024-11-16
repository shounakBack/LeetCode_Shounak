class Solution:
    def resultsArray(self, nums: List[int], k: int) -> List[int]:
        n=len(nums)
        res=[]
        for i in range(n-k+1):
            flag=0
            for j in range(i,i+k-1):
                if nums[j+1]!=nums[j]+1:
                    flag=1
                    break
            if flag==0:
                res.append(nums[i+k-1])
            else:
                res.append(-1)
        return res