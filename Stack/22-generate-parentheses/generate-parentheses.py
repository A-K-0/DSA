class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """

        res = []
        stack = []

        def backtrack(OpenP,CloseP):

            if OpenP == CloseP == n:
                res.append(''.join(stack))
                return

            if OpenP < n:
                stack.append('(')
                backtrack(OpenP+1,CloseP)
                stack.pop()

            if OpenP > CloseP:
                stack.append(')')
                backtrack(OpenP,CloseP+1)
                stack.pop()

        backtrack(0,0)

        return res
            


        