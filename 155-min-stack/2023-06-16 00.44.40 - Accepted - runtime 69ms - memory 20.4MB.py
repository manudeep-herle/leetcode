class MinStack:

    def __init__(self):
        self.stack = []
        self.min = float("inf")
        self.minTrace = []
        

    def push(self, val: int) -> None:
        self.stack.append(val)
        if val <= self.min:
            self.minTrace.append(self.min) # push old min onto min trace
            self.min = val # new min is the new value

    def pop(self) -> None:
        x = self.stack.pop()
        if x == self.min:
            self.min = self.minTrace.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.min


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()