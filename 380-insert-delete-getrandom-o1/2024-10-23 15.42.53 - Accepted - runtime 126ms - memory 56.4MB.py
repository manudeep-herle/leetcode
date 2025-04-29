class RandomizedSet:

    def __init__(self):
        self.map = {}
        self.list = []
        self.lastInd = -1

    def insert(self, val: int) -> bool:
        if val not in self.map:
            self.list.append(val)
            self.map[val] = len(self.list) - 1
            return True
        return False

    def remove(self, val: int) -> bool:
        if val in self.map:
            self.list[self.map[val]] = self.list[-1]
            self.map[self.list[-1]] = self.map[val]
            self.list.pop()
            self.lastInd -= 1
            del self.map[val]
            return True
        return False

    def getRandom(self) -> int:
        rand = random.choice(self.list)
        return rand




# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()