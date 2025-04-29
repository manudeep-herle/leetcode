class MyQueue:

    def __init__(self):
        self.queue = []
        self.index = 0

    def push(self, x: int) -> None:
        self.queue.append(x)
        
    def pop(self) -> int:
        if self.queue and self.index < len(self.queue):
            elem = self.queue[self.index]
            self.index += 1
            return elem

    def peek(self) -> int:
        if self.queue and self.index < len(self.queue):
            return self.queue[self.index]

    def empty(self) -> bool:
        return False if len(self.queue) and self.index < len(self.queue) else True        


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()