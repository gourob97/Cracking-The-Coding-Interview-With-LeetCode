# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.flag = 1
        self.root= None
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        
        if self.flag:
            self.root= root
            self.flag = 0
            
        if root is None:
            return TreeNode(val)
        
        if root.val > val:
            #insert left
            if root.left is None:
                Node = TreeNode(val)
                root.left = Node
                return self.root
            else:
                return self.insertIntoBST(root.left,val)
            
            
        elif root.val < val:
            #insert right
            if root.right is None:
                Node = TreeNode(val)
                root.right = Node
                return self.root
            else:
                return self.insertIntoBST(root.right,val)
            
        
