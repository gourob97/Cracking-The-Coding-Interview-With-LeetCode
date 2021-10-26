# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        l = set()
        def traverse(root, level):
            if root is None:
                return 
            traverse(root.left, level+1)
            l.add(level)
            traverse(root.right,level+1)
            
        traverse(root,0)   
        return len(l)

