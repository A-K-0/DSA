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

        def numcr():

            num1 = ''
            num2 = ''

            curr1 = l1
            curr2 = l2

            while curr1 or curr2:

                if curr1:
                    n = curr1.val 
                    num1 =  str(n) + num1
                    curr1 = curr1.next

                if curr2:
                    m = curr2.val 
                    num2 = str(m) + num2
                    curr2 = curr2.next

            return int(num1),int(num2)


        num1,num2 = numcr()

        Total = num1 + num2

        dummy = ListNode()
        current = dummy  
        
        if Total == 0:
            dummy = ListNode()
            current = dummy  
            current.next = ListNode(0)

        while Total != 0:
            n = Total % 10
            Total = Total // 10

            current.next = ListNode(n)
            current = current.next

        return dummy.next


            


        