# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isSubtree(self, root, subRoot):
        """
        :type root: Optional[TreeNode]
        :type subRoot: Optional[TreeNode]
        :rtype: bool
        """

        if not subRoot:
            return True

        if not root:
            return False

        
        if self.Sametree(root,subRoot):
            return True

        return (self.isSubtree(root.left,subRoot) or self.isSubtree(root.right,subRoot))

        


    def Sametree(self,s,t):

        if not t and not s:
            return True
        

        if s and t and s.val == t.val:
            return self.Sametree(s.left,t.left) and self.Sametree(s.right,t.right)

        return False

        