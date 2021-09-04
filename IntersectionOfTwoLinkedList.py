# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        hA = headA
        hB = headB
        lA=0
        lB=0
        while hA:
            lA+=1
            hA=hA.next
        while hB:
            lB+=1
            hB=hB.next
        
        diff = abs(lA-lB)
        
        hA = headA
        hB = headB
        
        
        while diff:
            if lA>lB:
                hA=hA.next
            else: 
                hB=hB.next
            diff-=1
            
          
        while hA:
            if hA == hB:
                return hA
            else:
                hA=hA.next
                hB=hB.next
        return 
            
        
