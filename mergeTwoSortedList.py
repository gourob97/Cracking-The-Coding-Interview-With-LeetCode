# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        
        result = []
        flp = l1
        slp = l2
        print(l1)
        print(l2)
        while flp and slp:
            if flp.val < slp.val:
                result.append(flp)
                flp = flp.next
            else:
                result.append(slp)
                slp = slp.next
        
        while flp:
            result.append(flp)
            flp = flp.next
        while slp:
            result.append(slp)
            slp=slp.next
        
        if len(result):
            for i in range(len(result)-1):
                result[i].next = result[i+1]
            return result[0]
        return 
            
            
            
        
        
