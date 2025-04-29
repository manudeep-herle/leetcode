import re

class Solution:
    def isPalindrome(self, s: str) -> bool:
        reg = re.compile('[^a-zA-Z0-9]')
        s = reg.sub("", s).casefold()
        if s[::-1] == s:
            return True
        else:
            return False