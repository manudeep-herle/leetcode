class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        count = 0
        moves = 0
        for c in s:
            if c == "(":
                count += 1
            else:
                count -= 1
            
            if count == -1:
                moves += 1
                count = 0
            
        moves += count
        return moves