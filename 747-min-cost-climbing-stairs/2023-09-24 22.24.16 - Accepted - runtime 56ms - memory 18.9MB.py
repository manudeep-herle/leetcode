class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        costMap = {}

        def climb(step):
            # Base case - reach the top (one more than last cost)
            if step >= len(cost):
                return 0
            # If the minimum cost given this starting step in known return it
            if step in costMap:
                return costMap[step]
            else:
            # The cost is minimum between taking 1 step and 2 steps.
                costMap[step] = min(climb(step+1), climb(step+2)) + cost[step]
                return costMap[step]

        climb(0)
        return min(costMap[0], costMap[1])
            
            
        