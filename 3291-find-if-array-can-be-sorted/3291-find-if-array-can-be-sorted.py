class Solution:
    def canSortArray(self, nums: List[int]) -> bool:
        n=len(nums)
        temp=nums.copy()
        for i in range(n):
            for j in range(n-i-1):
                if temp[j]<=temp[j+1]:
                    continue
                else:
                    if bin(temp[j]).count('1')==bin(temp[j+1]).count('1'):
                        temp[j],temp[j+1]=temp[j+1],temp[j]
                    else:
                        return False
        return True