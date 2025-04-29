class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        self.ans = []
        self.solve([], nums)
        return self.ans
    
    def solve(self, curr, options):
        if not options:
            self.ans.append(curr)
            return

        self.solve(curr + options[0:1], options[1:])
        self.solve(curr, options[1:])