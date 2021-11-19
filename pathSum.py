# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if root is None:
            return False
        
        q = deque()
        q.append((root, targetSum-root.val))
        
        while q:
            node,sum = q.popleft()
            if sum==0:
                if not node.right and not node.left:
                    return True
            if node.left:
                q.append( (node.left, sum-node.left.val))
            if node.right:
                q.append((node.right, sum-node.right.val))
                
        return False
        
