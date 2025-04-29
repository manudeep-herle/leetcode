class MinStack:

    def __init__(self):
        self.arr = []
        self.min = +inf
    def push(self, val: int) -> None:
        if val < self.min:
            self.min = val
        self.arr.append(val)
    def pop(self) -> None:
        ret = self.arr.pop(-1)
        if ret == self.min:
            self.min = min(self.arr) if len(self.arr) > 0 else +inf
    def top(self) -> int:
        return self.arr[-1]        
    def getMin(self) -> int:
        return self.min
                


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()