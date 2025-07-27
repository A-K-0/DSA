# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def isPalindrome(self, head):
        stack = []
        dummy = ListNode(-1)
        dummy.next = head
        s = f = dummy
        ctr = 0

        while f and f.next:
            s = s.next
            stack.append(s.val)
            f = f.next.next
            ctr += 1

        
        if f:
            s = s.next

        while s:
            if s.val != stack.pop():
                return False
            s = s.next

        return True




        
        