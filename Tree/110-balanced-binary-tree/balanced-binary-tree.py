# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isBalanced(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: bool
        """
        def dfs(node):

            if not node:
                return 0 

            lt = dfs(node.left)
            if lt == -1:
                return -1

            rt = dfs(node.right)
            if rt == -1:
                return -1

            if abs(lt - rt) > 1:
                return -1

            return max(lt,rt)+1

        return dfs(root) != -1





                