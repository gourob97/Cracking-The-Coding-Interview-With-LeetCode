# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        if head.next is None:
            return True
        
        l = 0
        curr = head
        
        while curr:
            l+=1
            curr=curr.next
        
        stack = []
        curr = head
        for i in range(l//2):
            stack.append(curr.val)
            curr=curr.next
        
        if l%2==1:
            curr=curr.next
        
      
        while curr and stack:
            if curr.val!=stack[-1]:
                return False
            else:
                stack.pop()
                curr=curr.next
                
        if not stack:
            return True
        return False
                
        
