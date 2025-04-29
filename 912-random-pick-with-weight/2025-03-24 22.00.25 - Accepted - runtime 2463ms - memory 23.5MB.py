class Solution:

    def __init__(self, w: List[int]):
        # prob list where prob[i] = prob of w[i] + w[j] for j = 0 -> i - 1 
        probSum = 0
        self.probs = []
        weightSum = sum(w)
        for weight in w:
            probSum += weight/weightSum
            self.probs.append(probSum)

    def pickIndex(self) -> int:
        # generate random num rand
        # for i in len(prob), if rand < prob[i]: return i
        rand = random.random()
        for i, prob in enumerate(self.probs):
            if rand < prob:
                return i

# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()