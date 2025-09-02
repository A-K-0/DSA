# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


# k value cannot be greater than n 
# first teaverse through the left subtree after left subtree and minus the value of k
# if k is not equal to 0 by the end the left subtree here for example([5,3,6,2,4,null,null,1], k = 3), if
# k would have been 4 then the answer would have been 4 which is in the right part of subtree

#
class Solution(object):
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        """
        :type root: Optional[TreeNode]
        :type k: int
        :rtype: int
        """

        count = k 
        res = root.val


        def dfs(root):

            nonlocal count,res

            if not root:
                return 

            dfs(root.left)
            count -= 1

            if count == 0:
                res = root.val

                return

            dfs(root.right)

        dfs(root)

        return res



        