class Solution(object):
    def calculate(self, s):
        if not s:
            return 0

        s = s.replace(" ", "")

        stack = []
        curr = 0
        op = '+'
        operator_set = {'+','-','*','/'}

        for i in range(len(s)):
            char = s[i]
            if char.isdigit():
                curr = curr * 10 + int(char)

            if char in operator_set or i == len(s) - 1:
                if op == '+':
                    stack.append(curr)
                elif op == '-':
                    stack.append(-curr)
                elif op == '*':
                    stack[-1] = int(stack[-1]*curr)
                elif op == '/':
                    stack[-1] = int(stack[-1] / float(curr))
            
                curr = 0
                op = char

        return sum(stack)




                

        