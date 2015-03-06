# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @return a ListNode
    def addTwoNumbers(self, l1, l2):
        answer=ListNode(0)
        pointer = answer
        
        
        while (l1 != None or l2 !=None):
            carry = 0
            if (l1 != None):
                sum = pointer.val+l1.val
                pointer.val = sum%10
                carry = sum/10
                l1=l1.next
                
            if (l2 != None):
                sum = pointer.val+l2.val
                pointer.val = sum%10
                carry = carry+sum/10
                l2=l2.next
            
            if (l1!=None or l2!=None or carry!=0):
                pointer.next = ListNode(carry)
                pointer = pointer.next
            
        return answer
            
