class Solution(object):
    def decodeString(self, s):
        num_stack = []
        string_stack = []
        temp = ''
        curr_num = 0
        final = ''

        loop = None
        # nums = set(range(1,10))

        for char in s:
            if char.isdigit():
                curr_num = curr_num * 10 + int(char)

            elif char == '[':
                num_stack.append(curr_num)
                string_stack.append(char)
                curr_num = 0 

            elif char == ']':
                temp = ''
                while string_stack and string_stack[-1] != '[':
                    temp = string_stack.pop() + temp
                string_stack.pop()
                loop = num_stack.pop()

                final = temp * loop

                string_stack.append(final)

                        

            else:
                string_stack.append(char)

        return ''.join(string_stack)


        