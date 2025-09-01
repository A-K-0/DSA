# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def goodNodes(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """

        main = root.val


        def dfs(root,count,main):

            if not root:
                return 0

            if root.val >= main:
                count = 1

            else:
                count = 0

            main = max(main, root.val)

            left = dfs(root.left,count,main)
            right = dfs(root.right,count,main)

            return count + left + right


        return dfs(root,0,main)