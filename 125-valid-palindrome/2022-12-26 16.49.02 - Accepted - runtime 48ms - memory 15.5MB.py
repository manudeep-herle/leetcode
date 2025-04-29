import re

class Solution:
    def isPalindrome(self, s: str) -> bool:
        # Remove all spaces
        # Convert to lowercase
        s = s.casefold().replace(" ", "")
        # Remove all non-alphabets
        reg = re.compile('[^a-zA-Z0-9$]')
        s = reg.sub("",s)
        rev = ""
        for i in range(len(s) - 1, -1, -1):
            rev = rev + s[i]
        if rev == s:
            return True
        else:
            return False