# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        ret = root
        if root is None:
            return TreeNode(val)
            
        while True:
            if root is None:
                ins= TreeNode(val)
                if l:
                    prev.left = ins
                else:
                    prev.right = ins
                return ret
            
            prev = root
            l = False
            
            if val < root.val:
                root = root.left
                l = True
            elif val > root.val:
                root = root.right
                
        
