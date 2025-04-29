from collections import Counter

class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        counts = Counter(heights)
        res = 0
        i = 0
        for num in range(1, 101):
            if num in counts:
                count = counts[num]
                end = i+count
                while i < end:
                    if heights[i] != num:
                        res += 1
                    i += 1

        return res        