# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def recoverTree(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: None Do not return anything, modify root in-place instead.
        """
   

        self.first = None
        self.second = None
        self.prev = None

        def inorder(root):

            if not root:
                return 

            inorder(root.left)

            if self.prev and self.prev.val > root.val:
                if self.first is None:
                    self.first = self.prev
                self.second = root
            self.prev = root

            inorder(root.right)

        inorder(root)

        if self.first and self.second:
            self.first.val, self.second.val = self.second.val, self.first.val


        