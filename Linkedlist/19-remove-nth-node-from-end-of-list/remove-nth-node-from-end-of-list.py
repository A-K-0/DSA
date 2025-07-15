# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def removeNthFromEnd(self, head, n):


        if head.next is None:
            return None
        
        dummy = ListNode(-1)
        dummy.next = head  

        F = dummy
        S = dummy 



        for i in range(n):
            F = F.next

        while F.next:
            S = S.next
            F = F.next

        S.next = S.next.next



        return dummy.next
            
        