# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def levelOrder(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: List[List[int]]
        """

        arr= []

        def dfs(root,lvl):

            if not root :
                return None

            if lvl == len(arr):
                arr.append([])

            arr[lvl].append(root.val)
            dfs(root.left,lvl+1)
            dfs(root.right,lvl+1)

        dfs(root,0)
            
        return arr



        
        