# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:

        newList = []

        for i in range(len(lists)):
            node = lists[i]

            while node:
                newList.append(node.val)
                node = node.next


        newList.sort()
        #print(newList)

        result = []


        for item in newList:
            result.append(ListNode(item))
        if len(result) == 0:
            return 
        for i in range(len(result)-1):
            result[i].next=result[i+1]
        return result[0]
