class Solution(object):
    def preorderTraversal(self, root):
        if not root:
            return []

        stack = [root]
        output = []

        while stack:
            node = stack.pop()
            output.append(node.val)

            if node.right:
                stack.append(node.right)
            if node.left:
                stack.append(node.left)

        return output
