# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# * In this question we are going to add all the possibilities from the root node to leaf node altogether not 
#   individually

#   Example:
#     1) Input: root = [1,2,3]
#        Output: 25

#        Subtree1: [1,2] -> num1 = 12
#        Subtree2: [1,3] -> num2 = 13

#        Total = 12 + 13 = 25

#     2) Input: root = [4,9,0,5,1]
#        Output: 1026

#        Subtree1: [4,0] -> num1 = 40
#        Subtree2: [4,9,1] -> num2 = 491
#        Subtree3: [4,9,5] -> num3 = 495

#        Total = 40 + 491 + 495 = 1026

#        * the intuition behind these outputs is that it traverse the whole tree and finds out the way till 
#        the leaves and then at the leaves it will add it to a variable.

#        * Just like this all the possible subtrees are covered and added to a single variable.

#        * The total must not cross (32-bit integer value) and max length can be 10 nodes. Test cases are prepared
#        in a way that they fit in 32 bit integer.

#        EDGECASES:

#        - If a single node is there then return itself
#        - no root return None


class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:

        if not root:
            return None

        Total = 0
        num = ''

        def calc(root,num):

            nonlocal Total

            if not root:
                return 

            if not root.left and not root.right:
                num += str(root.val)
                Total += int(num)
                return Total
            
            if root.left or root.right:
                num += str(root.val)

            calc(root.left,num)
            calc(root.right,num) 
        
        calc(root,'')

        return Total

            





        