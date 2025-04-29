class Solution:
    def minOperations(self, logs: List[str]) -> int:
        steps = 0

        for log in logs:
            if log[0] == "." and log[1] == '.':
                if steps > 0:
                    steps -= 1
            elif log[0] == '.':
                steps = steps
            else:
                steps += 1
        
        return steps

        