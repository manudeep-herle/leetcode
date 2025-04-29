from heapq import heapify, heappush, heappop

class SmallestInfiniteSet:

    def __init__(self):
        self.cur = 1
        self.data = []
        heapify(self.data)
        self.set = set()

    def popSmallest(self) -> int:
        small = None
        if len(self.data):
            small = heappop(self.data)
            self.set.remove(small)
        else:
            small = self.cur
            self.cur += 1
        return small

    def addBack(self, num: int) -> None:
        if num not in self.set and num < self.cur:
            self.set.add(num)
            heappush(self.data, num)
        


# Your SmallestInfiniteSet object will be instantiated and called as such:
# obj = SmallestInfiniteSet()
# param_1 = obj.popSmallest()
# obj.addBack(num)