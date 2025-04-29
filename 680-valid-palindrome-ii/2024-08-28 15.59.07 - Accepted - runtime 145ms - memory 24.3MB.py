class Solution:
    def validPalindrome(self, s: str) -> bool:
        def isPalindrome(l,r, deleted):
            if l >= r:
                return True
            elif s[l] == s[r]:
                return isPalindrome(l+1, r-1, deleted)
            elif not deleted:
                return isPalindrome(l+1, r, True) or isPalindrome(l, r-1, True)
            else:
                return False
        return isPalindrome(0, len(s)-1, False)
        