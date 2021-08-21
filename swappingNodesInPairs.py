# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        #print(head.val)
        d = ListNode(0)
        d.next = head
        start = d
       
        while d.next and d.next.next:
            p = d.next
            q = p.next
            
            d.next = q
            p.next = q.next
            q.next = p
            
            d = p 
        
        return start.next
        
