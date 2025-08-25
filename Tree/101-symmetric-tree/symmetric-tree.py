# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isSymmetric(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: bool
        """

        if not root:
            return True

        return self.sym(root.left,root.right)



    def sym(self,s,t):

        if not s and not t:
            return True

        if not s:
            return False

        if not t:
            return False

        if s.val !=  t.val:
            return False

        return (self.sym(s.left,t.right) and self.sym(s.right,t.left))

            # return False


            

        