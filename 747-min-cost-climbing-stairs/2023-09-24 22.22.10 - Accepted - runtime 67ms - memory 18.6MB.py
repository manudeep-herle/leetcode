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
                stepCost = None
                if step < 0:
                    stepCost = 0
                else:
                    stepCost = cost[step]
            # The cost is minimum between taking 1 step and 2 steps.
                costMap[step] = min(climb(step+1), climb(step+2)) + stepCost
                return costMap[step]

        return climb(-1)
            
            
        