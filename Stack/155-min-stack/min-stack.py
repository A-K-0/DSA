class MinStack(object):

    def __init__(self):
        self.stack = []
        

    def push(self, val):
        self.stack.append(val)
        
    def pop(self):
        if len(self.stack) == 0:
            return None
        else:
            self.stack.pop()
        return None
        

    def top(self):
        if len(self.stack) == 0:
            return None
        else:
            h = len(self.stack)-1
            top = self.stack[h]
        return top
        

    def getMin(self):
        return min(self.stack)
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()