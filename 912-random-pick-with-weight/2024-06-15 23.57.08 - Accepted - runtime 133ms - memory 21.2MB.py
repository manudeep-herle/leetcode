class Solution:

    def __init__(self, w: List[int]):
        self.prefix_sums = []
        prev = 0
        for num in w:
            self.prefix_sums.append(prev + num)
            prev = self.prefix_sums[-1]
        self.total_sum = self.prefix_sums[-1]

    def pickIndex(self) -> int:
        """
        :rtype: int
        """
        target = self.total_sum * random.random()
        # run a binary search to find the target zone
        low, high = 0, len(self.prefix_sums)
        while low < high:
            mid = (low + high) // 2
            if target > self.prefix_sums[mid]:
                low = mid + 1
            else:
                high = mid
        return low
        


# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()