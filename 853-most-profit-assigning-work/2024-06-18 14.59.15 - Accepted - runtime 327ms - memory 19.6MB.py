class Solution:
    def maxProfitAssignment(self, difficulty: List[int], profit: List[int], worker: List[int]) -> int:
        # combine the profit and difficulty lists (jobs list), sort jobs list in ascending order based on profit
        res = i = 0 
        jobs = list(zip(profit, difficulty))
        jobs.sort()
        # Sort workers by their ability in descending order
        worker.sort(reverse = True)
        # Pop the jobs list, for each job assign as many workers as possible.
        # Break when workers list is empty or jobs list is empty
        while jobs and i < len(worker):
            (profit_, difficulty_) = jobs.pop()
            while i < len(worker) and worker[i] >= difficulty_:
                res += profit_
                i += 1
        return res