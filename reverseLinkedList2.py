# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        dummy = ListNode(0,head)
        pg = dummy
        curr=head
        
        count = 1
        
        while count<left:
            pg=pg.next
            curr=curr.next
            count+=1
          
        tail = curr
        prev = curr
        curr = curr.next
        while(count<right):
            temp = curr.next
            curr.next=prev
            prev=curr
            curr=temp
            count+=1
        pg.next=prev
        tail.next=curr
        return dummy.next
        
        
     
