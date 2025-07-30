class Solution(object):
    def evalRPN(self, tokens):
        stack = []
        temp1 = 0
        temp2 = 0
        total = 0

        if not tokens:
            return None

        for token in tokens:

            if token.lstrip('-').isdigit():
                stack.append(int(token))

            if token == '+':
                temp1 = stack.pop()
                temp2 = stack.pop()
                total = temp2 + temp1
                stack.append(total)

            if token == '-':
                temp1 = stack.pop()
                temp2 = stack.pop()
                total = temp2 - temp1
                stack.append(total)

            if token == '*':
                temp1 = stack.pop()
                temp2 = stack.pop()
                total = temp2 * temp1
                stack.append(total)

            if token == '/':
                temp1 = stack.pop()
                temp2 = stack.pop()
                total = int(float(temp2) / temp1)
                stack.append(total)

            total = temp1 = temp2 = 0

        return stack[-1]
            



            

        