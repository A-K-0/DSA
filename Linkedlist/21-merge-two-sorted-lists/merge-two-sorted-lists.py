# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def mergeTwoLists(self, list1, list2):
        current = ListNode(-1)
        dummy = current

        if list1 is None:
            return list2
        if list2 is None:
            return list1



        while list1 and list2:
            if list1.val < list2.val:
                current.next = list1
                current = list1
                list1 = list1.next

            else:
                current.next = list2
                current = list2
                list2 = list2.next

            
            if list1:
                current.next = list1

            else:
                current.next = list2

        return dummy.next





        