# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0
        
        if root.left and root.right:
            return 1+ min(self.minDepth(root.left), self.minDepth(root.right))
        
        if root.left is None and root.right is None:
            return 1
        
        if root.left:
            dum=root.left
        else:
            dum=root.right
        
        return 1+ self.minDepth(dum)
