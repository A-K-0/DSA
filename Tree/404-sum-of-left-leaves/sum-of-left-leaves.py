# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def sumOfLeftLeaves(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """

        if not root:
            return 0

        return self.dfs(root) 

    def dfs(self,root):

        if not root:
            return 0

        total = 0

        if root.left and not root.left.left and not root.left.right :
            total += root.left.val

        total += self.dfs(root.left)
        total += self.dfs(root.right)


        return total

        



