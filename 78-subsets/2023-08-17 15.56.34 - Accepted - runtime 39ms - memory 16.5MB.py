class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        return self.solve([], nums)
        # return self.ans
    
    def solve(self, curr, options):
        if not options:
            # self.ans.append(curr)
            return [curr]
        # Left branch where we add the immediate next element
        return self.solve(curr + options[0:1], options[1:]) + self.solve(curr, options[1:])
        # Right branch where we skip the immediate next element
        