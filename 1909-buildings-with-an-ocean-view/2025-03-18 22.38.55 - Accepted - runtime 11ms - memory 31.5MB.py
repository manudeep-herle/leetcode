class Solution:
    def findBuildings(self, heights: List[int]) -> List[int]:
        max = 0
        out = collections.deque()
        for r in range(len(heights) - 1, -1, -1):
            if heights[r] > max:
                max = heights[r]
                out.appendleft(r)
        return list(out)
            