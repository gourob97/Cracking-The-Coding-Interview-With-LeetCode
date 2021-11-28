# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def increasingBST(self, root: TreeNode) -> TreeNode:
        self.dummy = TreeNode()
        self.prev = self.dummy
        
        
        def inorder(node):
            
            if node is None:
                return
            
            inorder(node.left)
            
            self.prev.left = None
            self.prev.right = node
            self.prev = node
            
            inorder(node.right)
            
        
        inorder(root)
        self.prev.right = None
        self.prev.left = None
        
        return self.dummy.right
        