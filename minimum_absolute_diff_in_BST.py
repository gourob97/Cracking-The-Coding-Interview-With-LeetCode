# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    min = 0 
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        
        result = []
        
        def T(root):
            if root is None:
                return 
            T(root.left)
            result.append(root.val)
            T(root.right)
        
        T(root)
        
        min = 9999999
        for i in range(len(result)-1):
            sub = result[i+1]-result[i]
            if min>sub:
                min=sub
        return min
        
        
        
        
