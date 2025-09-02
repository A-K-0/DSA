# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution(object):
    def isValidBST(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: bool
        """
        def validate(node, min_val, max_val):
            if not node:
                return True
                
            if node.val <= min_val or node.val >= max_val:
                return False
                
            if not node.left and not node.right:
                return True
                        
            if node.left and not node.right:
                if node.val <= node.left.val:
                    return False
                else:
                    return validate(node.left, min_val, node.val)
                    
            elif not node.left and node.right:
                if node.val >= node.right.val:
                    return False
                else:
                    return validate(node.right, node.val, max_val)
                        
            elif node.val > node.left.val and node.val < node.right.val:
                return (validate(node.left, min_val, node.val) and 
                       validate(node.right, node.val, max_val))
            else:
                return False
                
        return validate(root, float('-inf'), float('inf'))