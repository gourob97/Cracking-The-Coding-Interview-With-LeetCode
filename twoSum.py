# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        resultList = []
        temp1 = l1
        temp2 = l2
        carry =0
        
        while(temp1!=None or temp2 != None):
            sum=0
            if(temp1 == None):
                fd = 0
            else:
                fd = temp1.val
            if(temp2 == None):
                sd = 0
            else:
                sd = temp2.val
                
            sum= fd + sd + carry
            digit = sum%10
            carry = sum//10
            if(temp1 != None) :
                temp1 = temp1.next
            if(temp2!= None):
                temp2 = temp2.next
            
            resultList.append(ListNode(digit))
        
        if(carry!=0)  :
            resultList.append(ListNode(carry))
       
        for i in range(0,len(resultList)-1):
            resultList[i].next = resultList[i+1]
            #print(resultList[i].next)
        
            
        return resultList[0]
            
            
            
            
            