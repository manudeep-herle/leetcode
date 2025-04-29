class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        i = 0
        while True:
            commonChar = ""
            for s in strs:
                if i >= len(s):
                    return strs[0][0:i]
                elif not commonChar:
                    commonChar = s[i]
                elif s[i] != commonChar:
                    return strs[0][0:i]
            i += 1
        
        