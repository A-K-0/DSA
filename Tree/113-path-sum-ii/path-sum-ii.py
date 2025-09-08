# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# * In this problem we have to find different paths from root node to the leaf nodes summing upto the TrgetSum

# EXAMPLES:

# 1) Input: root = [5,4,8,11,null,13,4,7,2,null,null,5,1], targetSum = 22
#    Output: [[5,4,11,2],[5,8,4,5]]

#    - from the main tree root we are trying to find out the routes which are adding up to targetSum = 22
#    - [5,4,11,2] -> 5 + 4 + 11 + 2 = 22
#    - [5,8,4,5]  -> 5 + 8 + 4 + 5 = 22

#    - So the result returns this routes

# 2) Input: root = [1,2,3], targetSum = 5
#    Output: []

#    - In this tree we are trying to find out route to add up into 5
#    - [1,2] -> 1 + 2 = 3 X
#    - [1,3] -> 1 + 3 = 4 X

#    - None of them addup to 5 so the result is an empty array

# * Intuition behind this problem is that we must explore different paths in a tree and try to add the
# path sum till leaf nodes and check if the (TargetSum == Sum of the path).

# * Like this explore different paths and then if it matches then add into a result array containing paths.

# * The sum must only complete near a leaf node only, not in between

# EDGECASES:

# - Input: root = [1,2], targetSum = 0
#   Output: []

#   If targetSum is 0 then the result is empty array itself

# - If root is none then return an empty array

class Solution(object):
    def pathSum(self, root, targetSum):
        """
        :type root: Optional[TreeNode]
        :type targetSum: int
        :rtype: List[List[int]]
        """
        res = []

        def pathsum(root,path,total):

            if not root:
                return

            path.append(root.val)
            total += root.val
                

            if not root.left and not root.right:
                if total == targetSum:
                    res.append(list(path))
                        

            pathsum(root.left,path,total)
            pathsum(root.right,path,total)

            path.pop()

        pathsum(root,[],0)

        return res

