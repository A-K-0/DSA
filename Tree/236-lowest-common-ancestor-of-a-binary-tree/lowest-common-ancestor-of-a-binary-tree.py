# In this question we are going to find the lowest common ancestor of 2 nodes p and q
# it means that if we get 2 nodes p and q. We go towards the root and search for a node which has both the 
# nodes as common children nodes

# EXAMPLES:

# 1) Input: root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 1
# Output: 3

# Explanation: The LCA of nodes 5 and 1 is 3.
# As you can see in the tree the first two children nodes are 5 and 1 which are p and q. Which are
# children of 3, so 3 is the common ancestor node.

# 2) root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 4
# Output: 5

# Explanation: The LCA of nodes 5 and 4 is 5, since a node can be a descendant of itself according to the LCA definition. In this problem one node can be ancestor itself too. here 5 and 4 are from 3 can be said but as 
# we can also say that one node can be its ancestor too so we have to give it to 5 not 3.


# INTUITION:

# 1) So the intuition i came up with is using DFS ,where we go from the root node left and right subtree.
# 2) When I encounter the p or q value will use a nonlocal variable to update the p and q true or false.
# 3) So will maintain the current value of its once they both are true, which means i have got them will
#    backtrack.
# 4) In backtracking will check if the roots are same or if the root is equal to p or q which will return
#    whichever matches so through this we can find if p or q is root of itself or not.






# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        def DFS(root,p,q):


            if not root:
                return None

            if root ==  p or root == q:
                return root

            left = DFS(root.left,p,q)
            right = DFS(root.right,p,q)

            if left and right:
                return root

            return left if left else right

        ansroot = DFS(root,p,q)

        return ansroot