class Solution:
    def validPalindrome(self, s: str) -> bool:
        l, r = 0, len(s)-1
        def helper(l,r, deleted):
            while l < r:
                if s[l] == s[r]:
                    l += 1
                    r -= 1
                elif not deleted:
                    return helper(l+1, r, True) or helper(l, r-1, True)
                else:
                    return False
            return True
        return helper(l, r, False)
            