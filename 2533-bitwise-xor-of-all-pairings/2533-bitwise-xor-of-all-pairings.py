class Solution:
    def xorAllNums(self, nums1: List[int], nums2: List[int]) -> int:
        n1,n2=len(nums1),len(nums2)
        xor1,xor2=0,0
        if n1%2!=0:
            for ele in nums2:
                xor2^=ele
        if n2%2!=0:
            for ele in nums1:
                xor1^=ele
        res=xor1^xor2
        return res