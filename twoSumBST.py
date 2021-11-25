# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        q = deque()
        li = []
        q.append(root)
        
        while q:
            node = q.popleft()
            if node.val in li:
                return True
            li.append(k-node.val)
            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)
        
        return False
            
        
