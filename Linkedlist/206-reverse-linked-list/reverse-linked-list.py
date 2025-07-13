# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reverseList(self, head):
        prev_node = None
        Curr_node = head
        
        if head is None:
            return None

        if head.next is None:
            return head

        while Curr_node:
            Next_node = Curr_node.next
            Curr_node.next = prev_node
            prev_node = Curr_node
            Curr_node = Next_node

        
        head = Curr_node
           

        return prev_node




