# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDiffInBST(self, root: Optional[TreeNode]) -> int:
        
        li = []
        
        def inorder(node):
            if node is None:
                return
            inorder(node.left)
            li.append(node.val)
            inorder(node.right)
        
        inorder(root)
        
        minimum = 9999999
        
        for i in range(len(li)-1):
            diff = li[i+1] - li[i] 
            
            if minimum>diff:
                minimum = diff
        
        return minimum
                
                
            
        
        
