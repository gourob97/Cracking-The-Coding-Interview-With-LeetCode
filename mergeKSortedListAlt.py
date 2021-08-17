# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        
        if not lists or len(lists)==0:
            return None
        
        while len(lists) > 1:
            mergedList = []
            
            for i in range(0,len(lists),2):
                l1 = lists[i]
                l2 = lists[i+1] if len(lists)>i+1 else None
                mergedList.append(self.merge(l1,l2))
            lists = mergedList
        return lists[0]
    
        
    def merge(self,l1,l2):
        first = ListNode()
        dummy = ListNode()
        
        first = dummy
        
        while l1 and l2:
            if l1.val<l2.val:
                dummy.next = l1
                l1 = l1.next
            else:
                dummy.next = l2
                l2 = l2.next
            dummy = dummy.next
            
        if l1:
            dummy.next = l1
        elif l2:
            dummy.next = l2
            
        return first.next
        
        
    
            
