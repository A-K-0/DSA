# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def hasCycle(self, head):
        dummy = ListNode(-1)
        dummy.next = head
        S = F = dummy 

        while F and F.next and F.next.next:
            F = F.next.next
            S = S.next

            if S is F:
                return True

        
        return False

                