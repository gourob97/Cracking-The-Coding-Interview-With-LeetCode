# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque

class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        if root is None:
            return True
        q = deque()
        q.append(root.left)
        q.append(root.right)
        
        while q:
            root1 = q.popleft()
            root2 = q.popleft()
            
            if root1 is None and root2 is None:
                continue
            if root1 is None or root2 is None:
                return False
            if root1.val != root2.val:
                return False
            q.append(root1.left)
            q.append(root2.right)
            q.append(root1.right)
            q.append(root2.left)
            
        return True
