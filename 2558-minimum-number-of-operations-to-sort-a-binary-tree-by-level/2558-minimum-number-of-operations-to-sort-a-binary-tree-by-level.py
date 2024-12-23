# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minimumOperations(self, root: Optional[TreeNode]) -> int:
        def helper(arr):
            swap=0
            sorted_arr=sorted(arr)
            h={}
            for i,n in enumerate(arr):
                h[n]=i
            for j in range(len(arr)):
                if arr[j]!=sorted_arr[j]:
                    swap+=1
                    pos=h[sorted_arr[j]]
                    h[arr[j]]=pos
                    arr[pos]=arr[j]
            return swap
        res=0
        nex=[]
        nex.append(root)
        while nex:
            curr=nex
            nex=[]
            level=[]
            for i in range(len(curr)):
                node=curr[i]
                level.append(node.val)
                if node.left:
                    nex.append(node.left)
                if node.right:
                    nex.append(node.right)
            res+=helper(level)
        return res
            