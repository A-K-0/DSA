# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: Optional[ListNode]
        :type l2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """

        Tot = 0
        Carry = 0
        dummy = ListNode(0)
        curr = dummy
        # curr = head

      


        while l1 or l2 or Carry:

            x = l1.val if l1 else 0
            y = l2.val if l2 else 0


            Tot = x + y + Carry
            if l1:

                l1 = l1.next
            if l2:

                l2 = l2.next

            if Tot > 9:
                curr.next = ListNode(Tot % 10)
                Carry = Tot // 10
                curr = curr.next

            else:
                curr.next = ListNode(Tot % 10)
                Carry = 0
                curr =curr.next

        return dummy.next
        

        
            
            
        