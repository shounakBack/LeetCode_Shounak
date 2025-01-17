class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        i,j,n=0,0,len(nums)
        while j<n:
            if nums[j]!=val:
                nums[i]=nums[j]
                i+=1
            j+=1
        return i