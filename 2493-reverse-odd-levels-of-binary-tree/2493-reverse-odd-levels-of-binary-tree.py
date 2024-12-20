# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def reverseOddLevels(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        nex=deque()
        nex.append((root))
        level=0
        while nex:
            curr=nex
            nex=deque()
            for i in range(len(curr)):
                node=curr[i]
                if node.left:
                    nex.append(node.left)
                if node.right:
                    nex.append((node.right))    
            if level%2==1:
                left,right=0,len(curr)-1
                while left<right:
                    temp=curr[right].val
                    curr[right].val=curr[left].val
                    curr[left].val=temp
                    left+=1
                    right-=1
            level+=1
        return root