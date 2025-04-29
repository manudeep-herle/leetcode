class RecentCounter:

    def __init__(self):
        self.reqs = []
        self.pointer = 0
    def ping(self, t: int) -> int:
        self.reqs.append(t)
        while t - self.reqs[self.pointer] > 3000:
            self.pointer += 1
        return len(self.reqs) - self.pointer 

        


# Your RecentCounter object will be instantiated and called as such:
# obj = RecentCounter()
# param_1 = obj.ping(t)