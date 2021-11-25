# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        s = []
        def traverse(root):
            if root is None:
                return
            if root.val>=low and root.val<=high:
                s.append(root.val)
                
            traverse(root.left)
            traverse(root.right)
            
        traverse(root)
        result = 0
        for item in s:
            result+=item
        return result
            
     
