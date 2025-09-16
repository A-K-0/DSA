# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def sortedListToBST(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[TreeNode]
        """
        arr= []
        count = 0

        def create_array(head,count):

            while head != None:
                arr.append(head.val)
                head = head.next
                count += 1
            return arr


        def create_tree(left,right):

            if left > right:
                return None

            mid = (left + right )// 2

            root = TreeNode(arr[mid])

            root.left = create_tree(left,mid-1)

            root.right = create_tree(mid + 1, right)

            return root

        
        create_array(head,0)

        left = 0
        right = len(arr) - 1

        

        root = create_tree(left,right)

        return root

        

        