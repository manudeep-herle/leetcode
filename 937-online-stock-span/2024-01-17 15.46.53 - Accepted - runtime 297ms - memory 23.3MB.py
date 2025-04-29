class StockSpanner:

    def __init__(self):
        self.prices = []
        self.prevLarge = []

    def next(self, price: int) -> int:
        i = len(self.prices) - 1

        self.prices.append(price)
        self.prevLarge.append(i-1)
 
        while i >= 0:
            if self.prices[i] > price:
                break
            else:
                i = self.prevLarge[i]

        self.prevLarge[-1] = i
        return len(self.prices) - i - 1

        


# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)