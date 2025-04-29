class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        self.ans = []
        self.candidates = sorted(candidates)
        self.target = target
        self.solve([], 0)
        return self.ans
    
    def solve(self, curr, sum):
        for num in self.candidates:    
            if sum + num == self.target:
                tup = tuple(sorted(curr + [num]))
                if not tup in self.ans:
                    self.ans.append(tup)
                return 
            
            if sum > self.target:
                return 
            
            else:
                self.solve(curr + [num], sum + num)

