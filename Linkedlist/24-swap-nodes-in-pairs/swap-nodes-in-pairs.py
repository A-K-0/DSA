# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next



# Input: head = [1,2,3,4]
# Output: [2,1,4,3]

# EVEN
# [1,2] -> [2,1]
# [3,4] -> [4,3]

# * every pair of nodes will change only if thwere are even no of elements present

# ODD
# Input: head = [1,2,3]
# Output: [2,1,3]

# [1,2] -> [2,1]
# [3] -> [3]

# * only swap if there are atleast 2 elements if there is one left out then dont swap with the last element


# EDGE CASES:

# * No elements return none
# * if only one is there return it

# Points to remember:

# - Treat each pair of elements separately, without mixing with others
# - In each iteration treat a pair and point it towards the next one
# - create a dummy or change head in the starting so that there would'nt be problem



class Solution(object):
    def swapPairs(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        curr = ListNode(-1)
        curr = head
        dummy = curr


        if head is None:
            return None 

        while curr and curr.next:
            temp = curr.next.val
            curr.next.val = curr.val
            curr.val = temp

            curr = curr.next.next

        return dummy

        
        