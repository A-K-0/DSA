# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def rightSideView(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: List[int]
        """

        arr = []

        def dfs(root,lvl):

            if not root:
                return None

            if len(arr) == lvl:
                arr.append(root.val)


            if root.right:
                dfs(root.right,lvl+1)

            if root.left:
                dfs(root.left,lvl+1)

        dfs(root,0)

        return arr


            
        