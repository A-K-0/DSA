class Solution(object):
    def isValid(self, s):
        hashmap = {')':'(','}':'{',']':'['}

        stack = []

        for char in s:
            if char not in hashmap:
                stack.append(char)

            else:
                if not stack:
                    return False

                else:
                    popped = stack.pop()
                    if popped != hashmap[char]:
                        return False

        return not stack



        