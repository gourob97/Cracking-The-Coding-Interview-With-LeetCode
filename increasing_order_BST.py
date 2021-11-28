# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    
    
    def increasingBST(self, root: TreeNode) -> TreeNode:
        li = []    
        
        def Traverse(root):
            if root is None:
                return
            Traverse(root.left)
            li.append(root.val)
            Traverse(root.right)
        
        
        Traverse(root)
        
        dummy= TreeNode()
        
        root= dummy
        
        
        for item in li:
            dummy.right =TreeNode(item)
            dummy=dummy.right
            
        return root.right
            
            
            
            
            
        
        
        
