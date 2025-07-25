class MinStack(object):

    def __init__(self):
        self.stack = []
        

    def push(self, val):
        self.stack.append(val)
        
    def pop(self):
        if len(self.stack) == 0:
            return None
        else:
            pop = self.stack.pop()
        return pop
        

    def top(self):
        if len(self.stack) == 0:

            h = len(self.stack)
            top = self.stack[h]
        else:
            h = len(self.stack)-1
            top = self.stack[h]
        return top
        

    def getMin(self):
        min_no = min(self.stack)
        return min_no
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()