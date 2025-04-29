class Solution:
    def validPalindrome(self, s: str) -> bool:
        # two pointers - l, r
        # func to match l and r.
        def check(l, r, skipped):
            if l >= r:
                return True
            if s[l] == s[r]:
                return check(l+1, r-1, skipped)
            elif skipped:
                return False
            else:
                return check(l+1, r, True) or check(l, r-1, True)
        
        return check(0, len(s) - 1, False)


        