# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def binaryTreePaths(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: List[str]
        """

        op = []

        self.paths(root,op,"")

        return op


    def paths(self,root,op,string):

        if not root:
            return 

        string += str(root.val)+ "->"

        if not root.right and not root.left:
            op.append(string[:-2])

        self.paths(root.left, op,string)
        self.paths(root.right,op,string)


        if not root:
            return 

        
        