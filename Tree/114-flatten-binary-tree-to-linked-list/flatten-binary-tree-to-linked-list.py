# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# * We have to take a binary tree and then convert it to a linkedlist in a form of tree just pointing right
# and the linkedlist must be in preorder only.

# EXAMPLE

# 1) Input: root = [1,2,5,3,4,null,6]
#    Output: [1,null,2,null,3,null,4,null,5,null,6] -> pointing only right

# Preorder: [1,2,3,4,5,6] to a tree poinitng right

# INTUITION
# *Firsst try to traverse the tree in preorder manner ROOT -> LEFT -> RIGHT then try to remember previous 
# node.
# *Try to take the value of each node and add it to the right of the prev node and return the root 
# at the end which will give us the right skewed or flattened tree required.


# * PREORDER -> UPDATE TREE -> RETURN ROOT

# EDGECASES

# *If no root return None
# *If only one root return itself



class Solution(object):
    def flatten(self, root: Optional[TreeNode]) -> None:
        """
        :type root: Optional[TreeNode]
        :rtype: None Do not return anything, modify root in-place instead.
        """
        prev = None

        def rightskew(root):

            nonlocal prev

            if not root:
                return

            if prev:
                prev.right = root

                prev.left = None
            
            prev = root

            left,right = root.left,root.right
            rightskew(left)
            rightskew(right)

        rightskew(root)

        return root

        