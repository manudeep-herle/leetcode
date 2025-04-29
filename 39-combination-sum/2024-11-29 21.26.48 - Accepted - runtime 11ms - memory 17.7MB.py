class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        combinations = set()
        def backtrack(stack, i, curSum):
            if curSum == target:
                combinations.add(tuple(stack))
            elif curSum > target:
                return
            # add element at i
            stack.append(candidates[i])
            curSum += candidates[i]
            backtrack(stack, i , curSum)


            # remove last element on the stack and proceed to next i
            curSum -= stack[-1]
            stack.pop()
            if i+1 < len(candidates):
                backtrack(stack, i+1, curSum)

        backtrack([], 0, 0)
        res = []
        for comb in list(combinations):
            res.append(list(comb))
        return res

