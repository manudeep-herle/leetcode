from heapq import heapify, heappush, heappop

class SmallestInfiniteSet:

    def __init__(self):
        self.data = []
        for i in range(1,1001):
            self.data.append(i)
            heapify(self.data)
        self.set = set(self.data)

    def popSmallest(self) -> int:
        small = heappop(self.data)
   
        self.set.remove(small)
   
        return small

    def addBack(self, num: int) -> None:
        if num not in self.set:
            self.set.add(num)
            heappush(self.data, num)
        


# Your SmallestInfiniteSet object will be instantiated and called as such:
# obj = SmallestInfiniteSet()
# param_1 = obj.popSmallest()
# obj.addBack(num)