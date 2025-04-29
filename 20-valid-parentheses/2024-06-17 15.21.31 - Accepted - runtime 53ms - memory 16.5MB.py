class Solution:
    def isValid(self, s: str) -> bool:
        openedBrackets = []
        bracketPairs = {')': '(', ']': '[', '}': '{'}
        for bracket in s:
            # Check if it's an opening bracket
            if bracket in bracketPairs.values():
                openedBrackets.append(bracket)
            # Closing bracket
            elif openedBrackets and openedBrackets[-1] == bracketPairs[bracket]:
                openedBrackets.pop()
            else:
                return False
        
        return True if not openedBrackets else False