class MinStack:

    def __init__(self):
        self.minimum = None
        self.stack = []

    def push(self, val: int) -> None:
		# calculate the min for each new appended value
        if self.minimum is not None:
            self.minimum = min(self.minimum, val)
        else:
            self.minimum = val
        
        print(self.minimum)    
        self.stack.append(val)

    def pop(self) -> None:
        return_value = self.stack.pop(len(self.stack) - 1)
		
		# if the minimum value has just been removed, recalculate min value
        if return_value == self.minimum:
            self.minimum = min(self.stack) if len(self.stack) > 0 else None
        return return_value

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.minimum


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()